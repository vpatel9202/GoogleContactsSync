# Google Contacts Sync

Created on: Jul 2, 2023
Author: vpatel9202, Assisted by: OpenAI Chatbot
Project discussion: [ChatGPT link will be added later]

## Project Description

This project aims to sync Google Contacts information between two Google accounts. The script is written in Python and uses the Google People API for interacting with Google Contacts. It merges contacts data from both accounts, with precedence given to the most recent data when conflicts arise. The script also propagates contact deletions from one account to the other.

The script is set up to run automatically at specified intervals via GitHub Actions, using a custom Docker container. The state of contacts for synchronization purposes is stored in a SQLite database.

This project is designed with privacy and data security in mind. All sensitive data is stored securely using GitHub Secrets and environment variables.

## How to Use

Instructions for how to use the script will be provided here once the project is complete.

## Acknowledgements

This project was made possible with assistance from OpenAI's GPT-4 model, which helped with code generation and troubleshooting throughout the project.
