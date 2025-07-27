#!/bin/bash

powershell.exe -command "Get-Clipboard | Out-File -FilePath input.txt -Encoding UTF8"

python3 main.py

powershell.exe -command "Get-Content output.txt | Set-Clipboard"

echo "Chat formatting complete! Output copied to clipboard."