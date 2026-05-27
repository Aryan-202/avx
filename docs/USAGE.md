# AVX Usage Guide

Welcome to the **AVX Usage Guide**! This comprehensive guide will help you get started with AVX and master all its features for efficient file conversion and management.

## Table of Contents

1. [Quick Start](#quick-start)
2. [Installation](#installation)
3. [Core Commands](#core-commands)
4. [Advanced Usage](#advanced-usage)
5. [Examples & Workflows](#examples--workflows)
6. [Troubleshooting](#troubleshooting)
7. [FAQ](#faq)

---

## Quick Start

### Installation (One-Liner)

**For Linux/macOS:**
```bash
curl -fsSL https://raw.githubusercontent.com/Aryan-202/avx/main/scripts/install.sh | bash
```

**For Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/Aryan-202/avx/main/scripts/install.ps1 | iex
```

### Verify Installation

```bash
avx --help
```

This should display the help menu with all available commands.

### First Conversion

Convert a file in 30 seconds:
```bash
avx convert input.png -o output.jpg
```

---

## Installation

### Prerequisites

- **Python:** Version 3.13 or higher
- **Operating System:** Windows, macOS, Linux, or FreeBSD
- **Package Manager:** One of `pip`, `pipx`, or `uv` (for manual installation)

### Installation Methods

#### Method 1: Automated Script (Recommended)

The easiest way to install AVX with a single command.

**Windows (Command Prompt):**
```cmd
curl -sSL https://raw.githubusercontent.com/Aryan-202/avx/main/scripts/install.bat -o install.bat && install.bat
```

**Windows (PowerShell):**
```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Aryan-202/avx/main/scripts/install.ps1" -OutFile "install.ps1"; .\install.ps1
```

**macOS / Linux:**
```bash
curl -sSL https://raw.githubusercontent.com/Aryan-202/avx/main/scripts/install.sh | bash
```

#### Method 2: Using pipx (Recommended for Manual Install)

```bash
pipx install git+https://github.com/Aryan-202/avx.git
```

**Why pipx?** It installs AVX in an isolated environment, preventing conflicts with other Python packages.

#### Method 3: Using uv

```bash
uv tool install git+https://github.com/Aryan-202/avx.git
```

**Why uv?** It's fast, efficient, and great for isolated CLI tool installations.

#### Method 4: Using pip

```bash
pip install --user git+https://github.com/Aryan-202/avx.git
```

**Note:** Ensure your Python user `Scripts` (Windows) or `bin` (macOS/Linux) directory is in your PATH.

#### Method 5: From PyPI (Coming Soon)

```bash
pip install avx
```

---

## Core Commands

### 1. `avx ls` - List Files

Display files and directories in your current location.

**Basic Usage:**
```bash
avx ls
```

**With Hidden Files:**
```bash
avx ls --all
# or
avx ls -a
```

**Options:**
- `-a`, `--all`: Show hidden files (those starting with `.`)

**Output Example:**
```
📁 Directory Listing
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name              Type          Size          Modified
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
report.docx       File          245 KB        2024-01-15 10:30 AM
images            Directory     -             2024-01-14 03:45 PM
data.csv          File          52 KB         2024-01-15 02:20 PM
```

---

### 2. `avx convert` - Convert Files

The core command of AVX. Convert files between supported formats.

**Basic Usage:**
```bash
avx convert <input_file> -o <output_file>
```

**Examples:**

**Document Conversion:**
```bash
# Convert DOCX to PDF
avx convert report.docx -o report.pdf

# Convert PPTX to PDF
avx convert presentation.pptx -o presentation.pdf
```

**Image Conversion:**
```bash
# Convert PNG to JPG
avx convert photo.png -o photo.jpg

# Convert JPG to PNG
avx convert image.jpg -o image.png

# Convert JPEG to PNG
avx convert photo.jpeg -o photo.png
```

**Using Wildcards (Batch Conversion):**
```bash
# Convert all PNG files to JPG in the current directory
avx convert "*.png" -o ".jpg"

# Convert all DOCX files to PDF
avx convert "*.docx" -o ".pdf"
```

**Output to Directory:**
```bash
# Convert files and place them in a specific directory
avx convert "*.png" -o ./converted_images/

# All PNGs will be converted to JPGs in the output directory
avx convert "*.png" -o ./output/.jpg
```

**Options:**
- `-o`, `--output` (required): Specify the output file path, extension, or directory

**Supported Conversions:**

| From | To | Requirements |
|------|-----|-----|
| `.docx` | `.pdf` | Pandoc or LibreOffice |
| `.pptx` | `.pdf` | Pandoc or LibreOffice |
| `.png` | `.jpg`, `.jpeg` | Pillow (included) |
| `.jpg` | `.png` | Pillow (included) |
| `.jpeg` | `.png`, `.jpg` | Pillow (included) |
| `.gif` | `.png`, `.jpg` | Pillow (included) |

**Command Details:**
- Automatically detects input and output formats from file extensions
- Validates source file existence before conversion
- Returns clear error messages for unsupported conversions
- Supports both single files and batch operations with wildcards

---

### 3. `avx tree` - Directory Tree Visualization

Visualize your directory structure in a hierarchical, tree-based format.

**Basic Usage:**
```bash
avx tree
```

**Specify a Directory:**
```bash
avx tree ./src
avx tree /home/user/documents
```

**Options:**
- `-d`, `--dirs-only`: Show only directories, exclude files
- `-L <level>`, `--level <level>`: Limit depth to a specific level (e.g., 2 for two levels deep)

**Examples:**

```bash
# Show full tree structure
avx tree

# Show only directories up to 2 levels deep
avx tree -d -L 2

# Show structure of src folder with 3-level depth
avx tree ./src -L 3

# Show only directories in project
avx tree . --dirs-only
```

**Output Example:**
```
📁 Directory Tree
src/
├── avx/
│   ├── commands/
│   │   ├── convert.py
│   │   ├── ls.py
│   │   └── tree.py
│   ├── converters/
│   │   ├── image.py
│   │   ├── document.py
│   │   └── audio.py
│   └── cli.py
├── tests/
│   ├── test_convert.py
│   └── test_ls.py
└── README.md
```

---

### 4. `avx batch` - Bulk File Conversion

Convert multiple files in a directory at once.

**Basic Usage:**
```bash
avx batch <input_directory> --format <target_format> [options]
```

**Examples:**

```bash
# Convert all images in a folder to JPG
avx batch ./photos --format jpg

# Convert all DOCX files to PDF and save to output folder
avx batch ./documents --format pdf -o ./pdfs

# Convert all images in assets to PNG
avx batch ./assets --format png -o ./assets/png_versions
```

**Options:**
- `-f`, `--format` (required): Target format (e.g., pdf, jpg, png)
- `-o`, `--output`: Output directory (optional; defaults to current directory)

**Supported Batch Conversions:**
- Image batches: `jpg`, `png`, `gif`, `webp`
- Document batches: `pdf`
- Video/Audio: `mp4`, `mp3`, etc. (with FFmpeg installed)

---

### 5. `avx info` - File Information

Display detailed metadata about a file.

**Basic Usage:**
```bash
avx info <file_path>
```

**Examples:**

```bash
# Get info about an image
avx info photo.jpg

# Get info about a PDF
avx info document.pdf

# Get info about a video
avx info video.mp4
```

**Output Example:**

```
📄 File Information: photo.jpg
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
File Name:        photo.jpg
File Path:        /home/user/photos/photo.jpg
File Type:        JPEG Image
File Size:        2.3 MB (2,408,231 bytes)
Created:          2024-01-15 14:30:22
Modified:         2024-01-15 14:30:22
Permissions:      -rw-r--r--
Dimensions:       1920x1080 pixels
Color Space:      RGB
DPI:              72x72
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Advanced Usage

### Chaining Commands for Workflows

Combine multiple AVX commands to create powerful workflows.

**Example 1: Find and Convert Images**

```bash
# 1. List all PNG files
avx ls -a

# 2. Convert all PNGs to JPG
avx convert "*.png" -o ".jpg"

# 3. Check the results
avx tree
```

**Example 2: Batch Process with Verification**

```bash
# 1. Check what's in the documents folder
avx tree ./documents

# 2. Convert all DOCX to PDF
avx batch ./documents --format pdf -o ./documents/pdfs

# 3. Verify file info
avx info ./documents/pdfs/report.pdf
```

### Wildcard & Pattern Matching

AVX supports glob patterns for batch operations.

```bash
# Convert all PNGs in current directory
avx convert "*.png" -o ".jpg"

# Convert specific pattern
avx convert "report*.docx" -o ".pdf"

# Match files in subdirectories
avx convert "**/*.png" -o ".jpg"
```

### Using Environment Variables

While not built-in, you can use shell variables for dynamic conversions:

```bash
# Linux/macOS
INPUT_FORMAT="png"
OUTPUT_FORMAT="jpg"
avx convert "*.$INPUT_FORMAT" -o ".$OUTPUT_FORMAT"

# Windows (PowerShell)
$format = "jpg"
avx convert "*.png" -o ".$format"
```

---

## Examples & Workflows

### Workflow 1: Document Management

Convert and organize documents efficiently.

```bash
# 1. View all documents
avx tree ./documents

# 2. Convert all Word documents to PDF
avx batch ./documents --format pdf -o ./documents/pdf

# 3. View file information
avx info ./documents/pdf/report.pdf
```

### Workflow 2: Image Processing

Batch convert images for web usage.

```bash
# 1. List all original images
avx ls ./images

# 2. Convert all images to optimized JPG
avx batch ./images --format jpg -o ./images/optimized

# 3. Check the results
avx tree ./images -L 2
```

### Workflow 3: Multi-Format Conversion

Convert files through multiple formats if needed.

```bash
# 1. Convert DOCX to PDF
avx convert report.docx -o report.pdf

# 2. Verify conversion
avx info report.pdf

# 3. Convert PDF to image (if needed)
avx convert report.pdf -o report.png
```

### Workflow 4: Directory-Based Organization

Organize and convert files by type.

```bash
# 1. View directory structure
avx tree . -L 2

# 2. Convert all images
avx batch ./media/images --format jpg -o ./media/images/converted

# 3. Convert all documents
avx batch ./media/documents --format pdf -o ./media/documents/pdfs

# 4. Verify everything
avx ls ./media
```

---

## Troubleshooting

### Common Issues & Solutions

#### Issue: "Command not found: avx"

**Solution:** AVX is not in your PATH. Try:

```bash
# Verify installation
python -m pip show avx

# Reinstall with pipx
pipx install git+https://github.com/Aryan-202/avx.git

# Or reinstall with pip
pip install --user --upgrade git+https://github.com/Aryan-202/avx.git
```

#### Issue: "Unsupported conversion: PNG to GIF"

**Solution:** This conversion may not be supported yet. Check supported conversions above or open an issue on GitHub.

#### Issue: "FileNotFoundError: Input file not found"

**Solution:** Ensure the file path is correct:

```bash
# Check current directory
avx ls

# Use absolute path
avx convert /full/path/to/file.png -o output.jpg

# Check file exists
avx info file.png
```

#### Issue: "DOCX to PDF conversion failing"

**Solution:** Install required dependencies:

```bash
# Install Pandoc
# macOS:
brew install pandoc

# Linux (Ubuntu/Debian):
sudo apt-get install pandoc

# Windows (with Chocolatey):
choco install pandoc
```

#### Issue: "Permission Denied" on Output File

**Solution:** Ensure write permissions:

```bash
# Use a different output directory
avx convert input.png -o ~/Desktop/output.jpg

# Or check permissions
ls -la ./output_folder
```

#### Issue: "Out of Memory" with Large Files

**Solution:** AVX has memory limitations with very large files. Consider:
- Splitting large files before conversion
- Running conversion on a machine with more RAM
- Using system-native tools for extremely large files

---

## FAQ

### Q: What file formats does AVX support?

**A:** AVX currently supports:
- **Images:** PNG, JPG, JPEG, GIF
- **Documents:** DOCX, PPTX, PDF (via Pandoc/LibreOffice)
- **More coming:** Video, Audio, Data formats with additional plugins

See the [Supported Conversions](#supported-conversions) section for the full list.

### Q: Do I need Python installed to use AVX?

**A:** No! You can use the standalone binary version available for Windows, macOS, and Linux. However, the Python package version requires Python 3.13+.

### Q: Can I use AVX in Python scripts?

**A:** Yes! AVX is designed as an embeddable engine. You can import it directly:

```python
from avx.commands.convert import convert_files

# Convert programmatically
convert_files("input.png", "output.jpg")
```

### Q: How do I convert multiple files at once?

**A:** Use the `batch` command or wildcards with `convert`:

```bash
# Option 1: Batch command
avx batch ./images --format jpg

# Option 2: Wildcard conversion
avx convert "*.png" -o ".jpg"
```

### Q: What are the system requirements?

**A:** 
- **OS:** Windows 10+, macOS 10.15+, Linux (any modern distro), FreeBSD
- **Python:** Version 3.13+ (for pip/pipx installation)
- **Dependencies:** Pandoc/LibreOffice for document conversion, FFmpeg for audio/video

### Q: Is AVX free to use?

**A:** Yes! AVX is released under the MIT License. You can use, modify, and distribute it freely.

### Q: How do I get help or report a bug?

**A:** 
- Open an issue on [GitHub](https://github.com/Aryan-202/avx)
- Check the [Troubleshooting](#troubleshooting) section
- Review [AVX Documentation](../README.md)

### Q: Can I extend AVX with custom converters?

**A:** Yes! AVX is designed to be extensible. You can create custom conversion plugins by:
1. Creating a new converter module in `avx/converters/`
2. Following the existing converter patterns
3. Registering it in the conversion router

See the [Contributing Guide](../CONTRIBUTING.md) for details.

### Q: Why is conversion slow for large files?

**A:** Large file conversion depends on several factors:
- File size and complexity
- System CPU and RAM
- External tool performance (Pandoc, FFmpeg, etc.)
- Disk I/O speed

For very large files, consider:
- Using native system tools
- Running on a machine with better specs
- Breaking files into smaller chunks

### Q: Does AVX support cloud storage (S3, Google Drive, etc.)?

**A:** Not yet. AVX currently works with local files. Cloud storage support is planned for future releases.

---

## Additional Resources

- **[Installation Guide](./installation_guidence.md)** - Detailed installation instructions
- **[Commands Reference](./commands.md)** - Complete command documentation
- **[Roadmap & TODO](./TODO.md)** - Future features and development plans
- **[Main README](../README.md)** - Project overview and architecture
- **[Contributing Guide](../CONTRIBUTING.md)** - How to contribute to AVX
- **[GitHub Repository](https://github.com/Aryan-202/avx)** - Source code and issue tracker

---

## Support & Community

Have questions or need help?

- **GitHub Issues:** [Report bugs or request features](https://github.com/Aryan-202/avx/issues)
- **Discussions:** [Ask questions in Discussions](https://github.com/Aryan-202/avx/discussions)
- **Email:** [Support email if available]
- **Social Media:** [Links if available]

---

**Last Updated:** January 2025  
**AVX Version:** 0.1.0+  
**License:** MIT

Happy converting! 🚀
