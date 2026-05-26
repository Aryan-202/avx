$ErrorActionPreference = 'Stop'

# Enforce TLS 1.2 to prevent Invoke-WebRequest connection errors with GitHub
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

Write-Host "Starting AVX Installation..." -ForegroundColor Cyan

$Architecture = $env:PROCESSOR_ARCHITECTURE.ToLower()
Write-Progress -Activity "AVX Installation" -Status "Checking architecture ($Architecture)" -PercentComplete 10
Start-Sleep -Milliseconds 400

if ($Architecture -eq "amd64") {
    $Arch = "amd64"
} elseif ($Architecture -eq "arm64") {
    $Arch = "arm64"
} else {
    Write-Host "Unsupported architecture: $Architecture" -ForegroundColor Red
    exit 1
}

$BinaryUrl = "https://github.com/Aryan-202/avx/releases/latest/download/avx-windows-${Arch}.exe"
$InstallDir = "$env:USERPROFILE\.local\bin"

Write-Progress -Activity "AVX Installation" -Status "Preparing directory: $InstallDir" -PercentComplete 30
Start-Sleep -Milliseconds 400

if (-not (Test-Path -Path $InstallDir)) {
    New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
}

$DestPath = Join-Path -Path $InstallDir -ChildPath "avx.exe"

Write-Progress -Activity "AVX Installation" -Status "Downloading AVX from GitHub..." -PercentComplete 50

Invoke-WebRequest -Uri $BinaryUrl -OutFile $DestPath

Write-Progress -Activity "AVX Installation" -Status "Finalizing configuration" -PercentComplete 90
Start-Sleep -Milliseconds 400

Write-Progress -Activity "AVX Installation" -Status "Installation Complete" -PercentComplete 100
Start-Sleep -Milliseconds 300
Write-Progress -Activity "AVX Installation" -Completed

$avxLogo = @"

    ___ _    ___  __
   /   | |  / / |/ /
  / /| | | / /|   / 
 / ___ | |/ //   |  
/_/  |_|___//_/|_|  

"@

Write-Host $avxLogo -ForegroundColor Cyan

Write-Host "AVX installed successfully to $DestPath" -ForegroundColor Green
Write-Host "Make sure " -NoNewline; Write-Host $InstallDir -ForegroundColor Yellow -NoNewline; Write-Host " is in your PATH."
Write-Host "You can now use the 'avx' command anywhere.`n"
