# Changelog

All notable changes to **AI Security Training Lab** will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

### Changed
- Upgraded all attack and mitigation scripts to use OpenAI Python SDK v1.0+ format
- Refactored API client creation to new `client.chat.completions.create()` structure
- Made OpenAI model configurable via `OPENAI_MODEL` environment variable
- Updated `.env.example` to include `OPENAI_MODEL`
- Updated requirements.txt for new OpenAI SDK versions
- Updated README Quickstart instructions to reflect new setup


### Added
- Initial project setup
- Attack and mitigation scripts for OWASP Top 10 for LLM Applications
- Dockerfile for containerized runs
- .env.example file for secure API key management
- README with Quickstart and Tool Sections
- Code of Conduct
- Project folder structure `/owasp/llm/`
- Initial TODO.md for roadmap tracking
- Requirements.txt for dependency management


### Fixed
- (no fixes yet)

---

## [v0.9-beta] - 2025-04-28

### Added
- Beta release of AI Security Training Lab for internal testing and community feedback
- Prepared for v1.0 launch with professional Git workflow

---

> Built and maintained by [@citizenjosh](https://github.com/citizenjosh) 🚀
