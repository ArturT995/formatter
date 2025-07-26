#!/bin/bash

powershell.exe -command "Get-Clipboard" > input.txt

python3 main.py

cat output.txt | clip.exe

echo "Chat formatting complete! Output copied to clipboard."