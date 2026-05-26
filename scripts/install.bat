@echo off
setlocal enabledelayedexpansion

powershell -NoProfile -Command "Write-Host 'Starting AVX Installation...' -ForegroundColor Cyan"

:: Check architecture
if /i "%PROCESSOR_ARCHITECTURE%"=="AMD64" (
    set ARCH=amd64
) else if /i "%PROCESSOR_ARCHITECTURE%"=="ARM64" (
    set ARCH=arm64
) else (
    powershell -NoProfile -Command "Write-Host 'Unsupported architecture: %PROCESSOR_ARCHITECTURE%' -ForegroundColor Red"
    exit /b 1
)

set BINARY_URL=https://github.com/Aryan-202/avx/releases/latest/download/avx-windows-!ARCH!.exe
set INSTALL_DIR=%USERPROFILE%\.local\bin

powershell -NoProfile -Command "Write-Host 'Preparing directory: !INSTALL_DIR!' -ForegroundColor White"
if not exist "!INSTALL_DIR!" mkdir "!INSTALL_DIR!"

powershell -NoProfile -Command "Write-Host 'Downloading AVX from GitHub...' -ForegroundColor White"
curl.exe -# -fSL "!BINARY_URL!" -o "!INSTALL_DIR!\avx.exe"

powershell -NoProfile -Command "Write-Host 'Finalizing configuration...' -ForegroundColor White"

powershell -NoProfile -Command "$logo = @\"`n    ___ _    ___  __`n   /   | |  / / |/ /`n  / /| | | / /|   / `n / ___ | |/ //   |  `n/_/  |_|___//_/|_|  `n\"@; Write-Host $logo -ForegroundColor Cyan"

powershell -NoProfile -Command "Write-Host 'AVX installed successfully to !INSTALL_DIR!\avx.exe' -ForegroundColor Green; Write-Host 'Make sure ' -NoNewline; Write-Host '!INSTALL_DIR!' -ForegroundColor Yellow -NoNewline; Write-Host ' is in your PATH.'; Write-Host 'You can now use the ''avx'' command anywhere.`n'"
