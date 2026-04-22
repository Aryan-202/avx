# AVX Installation Guide

## Prerequisites

Before installing the AVX CLI, ensure your system meets the following requirements:
- **Python:** Version 3.13 or higher.
- **Package Manager:** `pipx` (recommended), `uv`, or `pip`.

---

## Automated Installation (Recommended)

For convenience, automated scripts are provided to handle the installation process. These scripts automatically detect your available package managers and securely install the CLI directly from the source.

### Windows (Command Prompt)
Open Command Prompt and execute the following command to download and run the installer:

```cmd
curl -sSL https://raw.githubusercontent.com/Aryan-202/avx/main/scripts/install.bat -o install.bat && install.bat
```

### Windows (PowerShell)
Open PowerShell and execute the following command:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Aryan-202/avx/main/scripts/install.ps1" -OutFile "install.ps1"; .\install.ps1
```
*(Note: If you encounter execution policy errors, you may need to run `powershell -ExecutionPolicy Bypass -File .\install.ps1` instead).*

### macOS / Linux
Open your terminal and execute the following command:

```bash
curl -sSL https://raw.githubusercontent.com/Aryan-202/avx/main/scripts/install.sh | bash
```

---

## Manual Installation

Alternatively, you can manually install the AVX CLI directly from the GitHub repository using your preferred Python package manager.

### Using pipx (Recommended)
`pipx` is the recommended tool for installing Python command-line applications in isolated environments.

```bash
pipx install git+https://github.com/Aryan-202/avx.git
```

### Using uv
If you have `uv` installed, you can use its tool installation command for a fast, isolated setup:

```bash
uv tool install git+https://github.com/Aryan-202/avx.git
```

### Using pip
You can use the standard package installer, `pip`. It is highly recommended to use the `--user` flag.

```bash
pip install --user git+https://github.com/Aryan-202/avx.git
```
*(Note: When using `pip`, ensure that your Python user `Scripts` (Windows) or `bin` (macOS/Linux) directory is added to your system's PATH variable).*

---

## Verifying the Installation

After the installation completes successfully, you can verify that AVX is ready to use by checking its help output:

```bash
avx --help
```

This command will print the available commands and options for the CLI, confirming the installation was successful.
