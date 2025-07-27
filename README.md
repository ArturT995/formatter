# Discord chat formatter
My project for the Boot.dev hackathon. Formats browser discord markdown into simple text.

## Intro

Hello! This is my first personal project, I decided to keep it simple.

I am using obsidian for note taking and sometimes see some useful messages on discord, but when copying them directly I get a big mess. Pasting the input as plain text still looks bad, so I decided to make a program that formats the text to be more readable.

The program is intended to be used with Windows WSL.

### Before formatting:

<img width=50% height=50% alt="Code_7qg0GoN3Tj" src="https://github.com/user-attachments/assets/6d8dc91c-85c4-4376-a822-3541ecf0d0dd" />

### After formatting:

<img width=50% height=50% alt="Code_y0NwjJpOxn" src="https://github.com/user-attachments/assets/566a7355-ffa3-4870-afa4-e5fa781991b9" />

## Set-up
(In WSL)
git clone https://github.com/ArturT995/formatter

copy some messages from discord.

run `./format_chat.sh` on console

(if you are using a different OS you can copy the clipboard text into input.txt and then run `python3 main.py`, then copy the result from output.txt)


You will now have the result in your clipboard now and can see how it looked before and after in input.txt and output.txt

You can copy this into your note taking app
