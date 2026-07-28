from app.core.logger import get_logger

logger = get_logger("services.validation")


class ResponseValidationService:
    """Validates AI responses for quality, completeness, and grounding."""

    HALLUCINATION_INDICATORS = [
        "as an ai",
        "i believe",
        "in my opinion",
        "it seems likely",
        "i think",
        "generally speaking",
        "it is well known",
        "studies have shown",
        "research suggests",
        "it is believed",
    ]

    def validate(
        self,
        response: str,
        citations: list[dict],
        confidence: float,
    ) -> dict:
        issues = []
        adjusted_confidence = confidence

        if not response or not response.strip():
            issues.append("empty_response")
            adjusted_confidence = 0.0

        response_lower = response.lower() if response else ""
        for indicator in self.HALLUCINATION_INDICATORS:
            if indicator in response_lower:
                issues.append(f"hallucination_indicator:{indicator}")
                adjusted_confidence *= 0.8
                break

        if not citations:
            issues.append("missing_citations")
            adjusted_confidence *= 0.7
        elif len(citations) == 1:
            adjusted_confidence *= 0.95

        if response and len(response) < 20:
            issues.append("response_too_short")
            adjusted_confidence *= 0.85

        if adjusted_confidence < 0.1 and issues:
            adjusted_confidence = 0.1

        if issues:
            logger.warning(f"Validation issues found: {issues}")

        return {
            "is_valid": "empty_response" not in issues,
            "issues": issues,
            "adjusted_confidence": round(max(0.0, min(1.0, adjusted_confidence)), 3),
        }
