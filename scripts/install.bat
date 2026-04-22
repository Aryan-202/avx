@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul

echo ==================================================
echo           Installing AVX CLI                      
echo ==================================================

set REPO_URL="git+https://github.com/Aryan-202/avx.git"

:: Check for pipx
where pipx >nul 2>nul
if %ERRORLEVEL% equ 0 (
    echo 📦 Found pipx! Installing avx using pipx ^(Recommended^)...
    pipx install %REPO_URL%
    if !ERRORLEVEL! equ 0 (
        echo ✅ AVX installed successfully!
        goto success
    )
)

:: Check for uv
where uv >nul 2>nul
if %ERRORLEVEL% equ 0 (
    echo 📦 Found uv! Installing avx using uv...
    uv tool install %REPO_URL%
    if !ERRORLEVEL! equ 0 (
        echo ✅ AVX installed successfully!
        goto success
    )
)

:: Check for pip
where pip >nul 2>nul
if %ERRORLEVEL% equ 0 (
    echo 📦 Found pip! Installing avx using pip...
    pip install --user %REPO_URL%
    if !ERRORLEVEL! equ 0 (
        echo ✅ AVX installed successfully!
        echo ⚠️  Note: Make sure your Python Scripts folder is in your PATH.
        goto success
    )
)

echo Error: Python package manager ^(pipx, uv, or pip^) not found or installation failed.
echo Please install Python from https://www.python.org/downloads/ and try again.
exit /b 1

:success
echo.
echo You can now run 'avx --help' to get started!
exit /b 0
