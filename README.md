# Google Contacts Sync

Created on: Jul 2, 2023
Author: vpatel9202, Assisted by: OpenAI Chatbot
Project discussion: [ChatGPT link will be added later]

---

## Project Description

This project aims to sync Google Contacts information between two Google accounts. The script is written in Python and uses the Google People API for interacting with Google Contacts. It merges contacts data from both accounts, with precedence given to the most recent data when conflicts arise. The script also propagates contact deletions from one account to the other.

The script is set up to run automatically at specified intervals via GitHub Actions, using a custom Docker container. The state of contacts for synchronization purposes is stored in a SQLite database.

This project is designed with privacy and data security in mind. All sensitive data is stored securely using GitHub Secrets and environment variables.

## How to Use

### Obtain Refresh Tokens Using for Automatic Syncing

The stand-alone script `get_refresh_tokens.py` is used to generate refresh tokens for the Google People API. These tokens are necessary for the main synchronization script to access your Google Contacts data. Here are the steps to generate and store these refresh tokens:

1. Before running the script, you will need to fill in your Google client ID and client secret for both accounts in src/credentials.py. These values are obtained from the Google Cloud Console when you create OAuth 2.0 credentials for your project.

2. To run the script, navigate to the `src` directory and execute the following command: ```python get_refresh_tokens.py```

    *Note: This script initiates the OAuth 2.0 flow, which includes opening a new tab in your default web browser. You will be prompted to log into each Google account and grant the necessary permissions.*

After granting permissions, the script will automatically update the refresh tokens in `src/credentials.py`. The tokens are stored in variables named `ACCOUNT1_REFRESH_TOKEN` and `ACCOUNT2_REFRESH_TOKEN`.

After this process, your `credentials.py` file should contain valid refresh tokens that allow the synchronization script to access your Google Contacts data.

The refresh tokens do not expire, but they become invalid if the user revokes permissions for the app. If you ever need to refresh the tokens, simply run the get_refresh_tokens.py script again.

**IMPORTANT**: The `credentials.py` file contains sensitive information. Do not share this file or commit it to a public repository. Always double-check that this file is listed in your .gitignore file to prevent accidental commits.

## Acknowledgements

This project was made possible with assistance from OpenAI's GPT-4 model, which helped with code generation and troubleshooting throughout the project.
