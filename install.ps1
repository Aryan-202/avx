$ErrorActionPreference = 'Stop'

Write-Host "==========================================="
Write-Host "Installing AVX..."
Write-Host "==========================================="

$Architecture = $env:PROCESSOR_ARCHITECTURE.ToLower()
if ($Architecture -eq "amd64") {
    $Arch = "amd64"
} elseif ($Architecture -eq "arm64") {
    $Arch = "arm64"
} else {
    Write-Host "Unsupported architecture: $Architecture"
    exit 1
}

$BinaryUrl = "https://github.com/Aryan-202/avx/releases/latest/download/avx-windows-${Arch}.exe"
$InstallDir = "$env:USERPROFILE\.local\bin"

if (-not (Test-Path -Path $InstallDir)) {
    New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
}

$DestPath = Join-Path -Path $InstallDir -ChildPath "avx.exe"

Write-Host "Downloading AVX from $BinaryUrl..."
Invoke-WebRequest -Uri $BinaryUrl -OutFile $DestPath

Write-Host "`nAVX installed successfully to $DestPath"
Write-Host "Make sure $InstallDir is in your PATH."
Write-Host "You can now use the 'avx' command anywhere."
