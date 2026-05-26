@echo off
echo ===========================================
echo Installing AVX globally...
echo ===========================================

:: Check if uv is installed
where uv >nul 2>nul
if %ERRORLEVEL% equ 0 (
    echo Using 'uv' for fast installation...
    uv tool install . --force
    echo.
    echo AVX installed successfully via uv!
    echo You can now use the 'avx' command anywhere.
    exit /b 0
)

:: Check if pipx is installed
where pipx >nul 2>nul
if %ERRORLEVEL% equ 0 (
    echo Using 'pipx' for isolated installation...
    pipx install . --force
    echo.
    echo AVX installed successfully via pipx!
    echo You can now use the 'avx' command anywhere.
    exit /b 0
)

:: Fallback to pip
echo 'uv' or 'pipx' not found. Falling back to standard pip...
pip install .
echo.
echo AVX installed successfully!
echo You can now use the 'avx' command anywhere.
exit /b 0
