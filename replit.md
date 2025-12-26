# Jumpscare Discord Bot

## Overview
A Discord bot that has a random chance to trigger jumpscare embeds when users send messages.

## Features
- 1/5 chance to trigger a jumpscare on any message
- Use `$jumpscare` command to force a jumpscare

## Setup
The bot requires a Discord bot token to run:
1. Create a Discord application at https://discord.com/developers/applications
2. Create a bot and copy the token
3. Add the token as a secret named `TOKEN` in Replit

## Project Structure
- `client.py` - Main bot client, handles events and runs the bot
- `main.py` - Contains the Jumpscare class with message logic

## Running
The bot runs via the "Discord Bot" workflow in the console output.

## Dependencies
- discord.py - Discord API wrapper
- python-dotenv - Environment variable loading
