$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "          Installing AVX CLI                      " -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan

$RepoUrl = "git+https://github.com/Aryan-202/avx.git"

function Install-With-Pipx {
    Write-Host "📦 Found pipx! Installing avx using pipx (Recommended)..." -ForegroundColor Yellow
    pipx install $RepoUrl
    Write-Host "✅ AVX installed successfully!" -ForegroundColor Green
}

function Install-With-Uv {
    Write-Host "📦 Found uv! Installing avx using uv..." -ForegroundColor Yellow
    uv tool install $RepoUrl
    Write-Host "✅ AVX installed successfully!" -ForegroundColor Green
}

function Install-With-Pip {
    Write-Host "📦 Found pip! Installing avx using pip..." -ForegroundColor Yellow
    pip install --user $RepoUrl
    Write-Host "✅ AVX installed successfully!" -ForegroundColor Green
    Write-Host "⚠️  Note: Make sure your Python Scripts folder is in your PATH." -ForegroundColor DarkYellow
}

if (Get-Command "pipx" -ErrorAction SilentlyContinue) {
    Install-With-Pipx
} elseif (Get-Command "uv" -ErrorAction SilentlyContinue) {
    Install-With-Uv
} elseif (Get-Command "pip" -ErrorAction SilentlyContinue) {
    Install-With-Pip
} else {
    Write-Host "Error: Python package manager (pipx, uv, or pip) not found." -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org/downloads/ and try again." -ForegroundColor Red
    exit 1
}

Write-Host "`nYou can now run 'avx --help' to get started!" -ForegroundColor Cyan
