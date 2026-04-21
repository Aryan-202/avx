# Contributing to AVX

First off, thank you for considering contributing to AVX! It's people like you that make AVX an amazing universal file management and conversion utility.

The following is a set of guidelines for contributing to AVX. These are primarily guidelines, not strict rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Code of Conduct
This project and everyone participating in it is governed by the [AVX Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs
Bugs are tracked as GitHub issues. When creating an issue, please explain the problem and include additional details to help maintainers reproduce the problem:

* Use a clear and descriptive title.
* Describe the exact steps which reproduce the problem.
* Provide the version of AVX and the operating system you are using.
* Include screenshots or logs if applicable.
* State what external tools you have installed (e.g., FFmpeg, Pandoc).

### Suggesting Enhancements
Enhancement suggestions are also tracked as GitHub issues. Please provide:

* A clear and descriptive title.
* A step-by-step description of the suggested enhancement.
* Explaining why this enhancement would be useful to the majority of AVX users.

### Pull Requests
The process described here has several goals:
* Maintain AVX's core routing and conversion architecture cleanly.
* Ensure code quality and stability.

**Process:**
1. Fork the repo and create your branch from `main`.
2. Map your new integration correctly within the existing domains (Document, Image, Audio, etc).
3. If you've added code that should be tested, write tests.
4. If you've changed CLI commands or domains, update the documentation in `docs/` and `README.md`.
5. Create a Pull Request with a clear description of what problem your PR solves.

## Project Setup & Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-org/avx.git
   cd avx
   ```
2. **Set up the environment (using Modern PEP standard tools like `uv` or `pip`):**
   ```bash
   uv pip install -e ".[dev]"
   ```
3. **Run the utility locally:**
   ```bash
   avx --help
   ```

## Development Architecture Guidelines
* Always place formatting and conversion execution logic securely within the `converters/` directory modules.
* The CLI should NEVER execute conversion logic directly; all actions must route through the framework's core.
* Do not forcibly cross format domains unless explicitly governed by the Universal Rule Engine logic.
