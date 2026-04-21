# AVX Commands Reference

AVX is a command-line tool for file management and format conversion. This document outlines the available commands, their usage, and standard options.

## Global Options

The following global options are supported across all AVX commands:

* `--help`, `-h`: Show the help message and exit.
* `--version`: Show version information.

---

## Core Commands

### 1. `avx ls`

List files and folders in the current directory.

**Usage:**
```bash
avx ls [options]
```

**Options:**
* `-a`, `--all`: Show hidden files (files starting with `.`).

**Command Details:**
* Displays files in a structured table.
* Provides file details including name, type (File/Directory), size, and last modified date.
* Utilizes a color-coded output for improved readability.

### 2. `avx convert`

Convert files between supported formats.

**Usage:**
```bash
avx convert <input_file> -o <output_file>
```

**Options:**
* `-o`, `--output` (required): Specify the output file path.

**Supported Conversions:**
* `.docx` to `.pdf` (Note: May require Pandoc installed as an external dependency)
* `.png` to `.jpg`
* `.jpg` to `.png`
* `.jpeg` to `.png` or `.jpg`

**Examples:**
```bash
avx convert report.docx -o report.pdf
avx convert image.png -o image.jpg
avx convert photo.jpg -o photo.png
```

**Command Details:**
* Automatically detects input and output formats based on the file extensions.
* Validates source file existence before attempting conversion.
* Returns clear error messages for unsupported conversion types.

---

## Extended Commands (Upcoming & New)

### 3. `avx tree`

Visualize the directory structure in a nested, tree-based format.

**Usage:**
```bash
avx tree [directory] [options]
```

**Options:**
* `-d`, `--dirs-only`: Display directories only, omitting files.
* `-L <level>`, `--level <level>`: Limit the display depth to the specified integer.

**Examples:**
```bash
avx tree ./src
avx tree -L 2
```

### 4. `avx batch`

Perform bulk conversions on multiple files within a target directory.

**Usage:**
```bash
avx batch <input_directory> --format <target_format> [options]
```

**Options:**
* `-f`, `--format` (required): Specify the target file format (e.g., pdf, jpg).
* `-o`, `--output`: Specify an output directory for the converted files. If omitted, the converted files are placed in the current directory.

**Examples:**
```bash
avx batch ./assets/images --format jpg -o ./assets/converted_images
```

### 5. `avx info`

Display detailed metadata and file properties. 

**Usage:**
```bash
avx info <file_path>
```

**Command Details:**
* Interrogates the file to show precise size, creation date, modification date, owner permissions, and resolution/format details (for images or documents).

**Examples:**
```bash
avx info sample.pdf
```

---

## Application Limitations
* Certain conversions will require external system dependencies.
* File sizes exceeding standard memory limitations may require additional processing time.
