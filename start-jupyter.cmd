@echo off
rem Startet JupyterLab aus der uv-Umgebung dieses Projekts.
rem Die Umgebung liegt absichtlich ausserhalb von OneDrive.
setlocal
set "UV_PROJECT_ENVIRONMENT=%USERPROFILE%\.venvs\nlproc-alv-b"
rem Windows-Zertifikatspeicher nutzen, weil Norton HTTPS-Verbindungen prueft.
set "UV_NATIVE_TLS=true"
cd /d "%~dp0"
uv run jupyter lab %*
