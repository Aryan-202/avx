# AVX Project Roadmap and Future Scope

This document outlines the strategic vision, architectural expansions, and future feature implementations planned for the AVX CLI tool. 

## ✅ Completed Milestones

### 1. Domain-Based Conversion Architecture (Completed)
We have successfully mapped conversions into specialized domains with 1-to-1 conversion files dynamically generated and tested:
*   **Document Conversions**: `docx`, `pdf`, `md`, `html`
*   **Image Conversions**: `png`, `jpg`/`jpeg`, `webp`, `bmp`, `tiff`, `gif`
*   **Audio Conversions**: `mp3`, `wav`, `flac`, `aac`, `ogg`, `m4a`
*   **Video Conversions**: `mp4`, `mkv`, `avi`, `mov`, `webm`
*   **Data Serialization Formats**: `csv`, `json`

### 2. Universal Rule Engine and Categorization (Completed)
Implemented a robust routing mechanism that intercepts the CLI commands and delegates execution appropriately using the dynamic `get_converter_func` and domain validation.

### 3. Advanced CLI Capabilities (Completed)
Expanded command parsing to support:
*   **Batch Operations:** Support for wildcards via `glob` (e.g., `avx convert *.png -o jpg`).
*   **Directory Conversions:** Recursively processing folders and outputting to directories.
*   **Auto-Output Prediction:** Intelligently predicting the most logical destination file if the output argument is omitted.

---

## 🚀 Future Roadmap (Phase 5)

### Professional Architectural Enhancements
To scale AVX into a production-grade utility engine, the following structural upgrades are prioritized:

*   **Plugin-Based Architecture:** Rebuild the converter module system to use discoverable plugins. This modularity ensures safe feature isolation and promotes open-source contribution for new formats.
*   **Environmental Auto-Discovery:** Build automatic environment scanning to verify paths for external binaries (such as FFmpeg or Pandoc). Fall back gracefully with clear installation instructions if dependencies are missing.
*   **Parallel Batch Processing:** Introduce concurrent task execution (via threaded or multiprocessing queues) to optimize CPU utilization during high-volume batch conversions.
*   **Dynamic Visual Feedback:** Standardize the use of the `rich` library to display dynamic, accurate progress bars, especially for large file streams, large video files, or grouped batch events.
*   **Archive Formats Extraction/Compression:**
    *   *Targets:* `zip`, `tar`, `gz`
    *   *Key Pipelines:* Interchange between compression algorithms and format packaging directly within the CLI.
