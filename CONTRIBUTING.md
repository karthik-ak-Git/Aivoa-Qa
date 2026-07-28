# Contributing to PharmaQMS Knowledge Base

Thank you for your interest in contributing to the PharmaQMS Knowledge Base. This document provides guidelines for contributing to this project.

---

## How to Contribute

### Reporting Issues

If you find inaccuracies, gaps, or issues in the knowledge base:

1. Check existing [issues](https://github.com/your-org/pharmaqms-knowledge-base/issues) first
2. Open a new issue with:
   - Clear title describing the issue
   - File path(s) affected
   - Description of the problem
   - Suggested fix (if applicable)
   - Source/reference for corrections

### Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes following the guidelines below
4. Commit with a descriptive message
5. Push to your fork and submit a pull request

### Content Guidelines

#### Source Requirements
- All facts must cite authoritative sources (FDA, ICH, EMA, WHO, USP, etc.)
- Include source URLs where available
- Assign confidence scores (0.0–1.0) to all claims
- Never fabricate information

#### Formatting Standards
- Use Markdown with consistent heading hierarchy
- Include metadata blocks at the end of each document
- Use tables for structured data
- Include JSON schemas for machine-readable data

#### File Naming
- Use `snake_case.md` for knowledge files
- Use `kebab-case.md` for documentation files
- Use descriptive, specific names

### Content Structure

Each knowledge file should include:

```markdown
# Title

## Overview
Brief description of content scope.

## Main Content
Organized sections with tables, lists, and structured data.

## Source Citations
References to authoritative sources.

## Metadata
JSON metadata block for machine readability.
```

### JSON Schema Standards

All structured data should follow JSON Schema:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["field1", "field2"],
  "properties": {
    "field1": { "type": "string" },
    "field2": { "type": "string" }
  }
}
```

---

## Pull Request Process

1. Update documentation if adding new content areas
2. Ensure all source citations are included
3. Add metadata blocks to new files
4. Update `knowledge_base_index.json` if adding new directories
5. Request review from maintainers

---

## Code of Conduct

See [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

---

## Questions?

Open an issue or contact the maintainers.
