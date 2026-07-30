"""OCR Service — extracts text from PDFs, images, and documents using PyMuPDF + pytesseract."""

import io
import os
import tempfile
from pathlib import Path
from typing import Optional
from app.core.logger import get_logger

logger = get_logger("services.ocr")

SUPPORTED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "tiff", "tif", "bmp", "txt", "md", "csv", "docx"}

try:
    import pytesseract
    for _candidate in [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
        str(Path.home() / "AppData" / "Local" / "Tesseract-OCR" / "tesseract.exe"),
    ]:
        if os.path.isfile(_candidate):
            pytesseract.pytesseract.tesseract_cmd = _candidate
            break
except ImportError:
    pass


def _extract_pdf_fitz(raw_bytes: bytes) -> str:
    import fitz
    doc = fitz.open(stream=io.BytesIO(raw_bytes), filetype="pdf")
    pages = []
    for page in doc:
        pages.append(page.get_text())
    doc.close()
    return "\n".join(pages)


def _extract_pdf_pdfminer(raw_bytes: bytes) -> str:
    from pdfminer.high_level import extract_text
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(raw_bytes)
        tmp.flush()
        text = extract_text(tmp.name)
    os.unlink(tmp.name)
    return text


def _extract_image_tesseract(raw_bytes: bytes) -> Optional[str]:
    try:
        from PIL import Image
        import pytesseract
        image = Image.open(io.BytesIO(raw_bytes))
        text = pytesseract.image_to_string(image, lang="eng")
        return text.strip() or None
    except ImportError:
        logger.warning("pytesseract or Pillow not installed — cannot OCR images")
        return None
    except Exception as e:
        logger.warning(f"Tesseract OCR failed: {e}")
        return None


def _extract_pdf_tesseract(raw_bytes: bytes) -> Optional[str]:
    try:
        import fitz
        import pytesseract
        from PIL import Image
        doc = fitz.open(stream=io.BytesIO(raw_bytes), filetype="pdf")
        pages = []
        for i, page in enumerate(doc):
            pix = page.get_pixmap(dpi=200)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            text = pytesseract.image_to_string(img, lang="eng")
            pages.append(f"--- Page {i + 1} ---\n{text.strip()}")
        doc.close()
        result = "\n\n".join(pages)
        return result.strip() or None
    except ImportError:
        logger.warning("fitz or pytesseract not installed — cannot OCR PDF")
        return None
    except Exception as e:
        logger.warning(f"PDF Tesseract OCR failed: {e}")
        return None


def _extract_docx(raw_bytes: bytes) -> str:
    from docx import Document
    doc = Document(io.BytesIO(raw_bytes))
    return "\n".join(p.text for p in doc.paragraphs)


def extract_text_from_bytes(raw_bytes: bytes, filename: str = "unknown") -> dict:
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    result = {"text": "", "method": "unknown", "page_count": 1, "success": False}

    if ext in ("txt", "md", "csv"):
        text = raw_bytes.decode("utf-8", errors="replace")
        result.update(text=text, method="direct", success=True)
        return result

    if ext == "pdf":
        try:
            text = _extract_pdf_fitz(raw_bytes)
            if text.strip():
                result.update(text=text, method="fitz", success=True)
                return result
        except ImportError:
            pass
        except Exception as e:
            logger.warning(f"PyMuPDF failed: {e}")

        try:
            text = _extract_pdf_pdfminer(raw_bytes)
            if text.strip():
                result.update(text=text, method="pdfminer", success=True)
                return result
        except ImportError:
            pass
        except Exception as e:
            logger.warning(f"pdfminer failed: {e}")

        try:
            text = _extract_pdf_tesseract(raw_bytes)
            if text:
                result.update(text=text, method="tesseract_pdf_ocr", success=True)
                return result
        except Exception as e:
            logger.warning(f"PDF render+OCR failed: {e}")

        result.update(text="[Could not extract text from PDF]", method="failed", success=False)
        return result

    if ext in ("png", "jpg", "jpeg", "tiff", "tif", "bmp"):
        text = _extract_image_tesseract(raw_bytes)
        if text:
            result.update(text=text, method="tesseract_ocr", success=True)
            return result
        result.update(text="[Could not OCR image]", method="failed", success=False)
        return result

    if ext == "docx":
        try:
            text = _extract_docx(raw_bytes)
            result.update(text=text, method="docx", success=True)
            return result
        except ImportError:
            pass
        except Exception as e:
            logger.warning(f"DOCX extraction failed: {e}")
        result.update(text="[Could not extract DOCX - python-docx not installed]", method="failed", success=False)
        return result

    text = raw_bytes.decode("utf-8", errors="replace")
    result.update(text=text, method="fallback_decode", success=True)
    return result
