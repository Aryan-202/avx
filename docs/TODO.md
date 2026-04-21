# AVX Project Roadmap and Future Scope

This document outlines the strategic vision, architectural expansions, and future feature implementations planned for the AVX CLI tool. 

## 1. Domain-Based Conversion Architecture

Attempting ubiquitous file conversion without contextual boundaries is inefficient. The upcoming architectural shift will involve segregating supported formats into specialized domains. Conversions will be supported within the same domain, systematically mapped to dedicated conversion engines for optimal performance.

### Proposed Domains and Target Operations

*   **Document Conversions**
    *   *Targets:* `docx`, `pdf`, `txt`, `md`, `html`, `odt`
    *   *Key Pipelines:* `docx` ↔ `pdf`, `docx` ↔ `md`, `md` ↔ `html`, `pdf` → `txt`
    *   *Engines Required:* Integration with Pandoc or LibreOffice headless modes.

*   **Image Conversions**
    *   *Targets:* `png`, `jpg`/`jpeg`, `webp`, `bmp`, `tiff`, `gif`
    *   *Key Pipelines:* Full bidirectional conversion across all supported image types.
    *   *Engines Required:* Pillow (Python Imaging Library).

*   **Audio Conversions**
    *   *Targets:* `mp3`, `wav`, `flac`, `aac`, `ogg`, `m4a`
    *   *Key Pipelines:* Routine transcoding between common audio formats.
    *   *Engines Required:* FFmpeg integrations.

*   **Video Conversions**
    *   *Targets:* `mp4`, `mkv`, `avi`, `mov`, `webm`
    *   *Key Pipelines:* Format shifting without severe re-encoding latency where possible.
    *   *Engines Required:* FFmpeg integrations.

*   **Data Serialization Formats**
    *   *Targets:* `csv`, `json`, `xml`, `xlsx`
    *   *Key Pipelines:* `csv` ↔ `json`, `csv` ↔ `xlsx`, `json` ↔ `xml`
    *   *Engines Required:* Standard library JSON/CSV modules and Pandas/OpenPyXL.

*   **Archive Formats**
    *   *Targets:* `zip`, `tar`, `gz`
    *   *Key Pipelines:* Interchange between compression algorithms and format packaging.

## 2. Universal Rule Engine and Categorization

Implement a robust routing mechanism that intercepts the CLI commands and delegates execution appropriately:

1.  Identify the input extension and the requested output extension.
2.  Map extensions to their established domain array.
3.  Validate request logic (e.g., blocking cross-domain commands like image-to-audio).
4.  Route valid combinations directly to the requisite converter toolset.

## 3. Advanced CLI Capabilities

Expand command parsing to support bulk operations, recursive tasks, and intelligent automation:

*   **Batch Operations:** Allow wildcard inputs targeting multiple files simultaneously (e.g., `avx convert *.png -o jpg`).
*   **Directory Conversions:** Recursively process folders and replicate the directory tree in an output location with transcoded files.
*   **Auto-Output Prediction:** Intelligently predict the most logical destination file if the output argument is omitted (e.g., mapping `avx convert file.docx` to generate `file.pdf` directly).

## 4. Professional Architectural Enhancements

To scale AVX into a production-grade utility engine, the following structural upgrades are prioritized:

*   **Plugin-Based Architecture:** Rebuild the converter module system to use discoverable plugins. This modularity ensures safe feature isolation and promotes open-source contribution for new formats.
*   **Environmental Auto-Discovery:** Build automatic environment scanning to verify paths for external binaries (such as FFmpeg or Pandoc). Fall back gracefully with clear installation instructions if dependencies are missing.
*   **Parallel Batch Processing:** Introduce concurrent task execution (via threaded or multiprocessing queues) to optimize CPU utilization during high-volume conversions.
*   **Dynamic Visual Feedback:** Standardize the use of the `rich` library to display dynamic, accurate progress bars, especially for large file streams or grouped batch events.
