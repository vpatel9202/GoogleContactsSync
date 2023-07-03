"""
get_refresh_tokens.py
Created on: Jul 2, 2023
Author: vpatel9202, Assisted by: OpenAI Chatbot

This standalone script is used to generate refresh tokens for the Google People API.
It uses OAuth 2.0 to authorize the application and get refresh tokens.
It prompts the user to input the refresh tokens, and then updates them in credentials.py.
"""

from getpass import getpass
from google_auth_oauthlib.flow import InstalledAppFlow
from utils.logger import logger

SCOPES = ['https://www.googleapis.com/auth/contacts']

def get_refresh_token(client_id, client_secret, account_name):
    """Initiates OAuth 2.0 flow and returns a refresh token."""
    try:
        print(f"Log in with your {account_name} Google account.")
        flow = InstalledAppFlow.from_client_config(
            {"installed":
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "access_type": "offline"
                }
            },
            SCOPES
        )
        creds = flow.run_local_server(port=0)
        logger.info('Refresh token generated successfully for %s account.', account_name)
        return creds.refresh_token
    except Exception as e:
        logger.error('Error occurred while generating refresh token for %s account: %s', account_name, e)
        raise

def write_credentials(filename, client_id1, client_secret1, refresh_token1, client_id2, client_secret2, refresh_token2):
    """Writes the credentials to a file."""
    credentials_dict = {
        'ACCOUNT1_CLIENT_ID': client_id1,
        'ACCOUNT1_CLIENT_SECRET': client_secret1,
        'ACCOUNT1_REFRESH_TOKEN': refresh_token1,
        'ACCOUNT2_CLIENT_ID': client_id2,
        'ACCOUNT2_CLIENT_SECRET': client_secret2,
        'ACCOUNT2_REFRESH_TOKEN': refresh_token2
    }
    try:
        with open(filename, 'w') as f:
            for key,value in credentials_dict.items():
                f.write(f"{key} = '{value}'\n")
        logger.info('New refresh tokens written to credentials.py successfully')
    except Exception as e:
        logger.error('Error occurred while writing credentials to file: %s', e)
        raise

def main():
    from credentials import (
        ACCOUNT1_CLIENT_ID,
        ACCOUNT1_CLIENT_SECRET,
        ACCOUNT2_CLIENT_ID,
        ACCOUNT2_CLIENT_SECRET,
    )

    logger.info('Getting refresh tokens, please follow the prompts in your web browser...')
    user_refresh_token1 = get_refresh_token(ACCOUNT1_CLIENT_ID, ACCOUNT1_CLIENT_SECRET, 'first')
    input("Press Enter to continue with the second Google account...")
    user_refresh_token2 = get_refresh_token(ACCOUNT2_CLIENT_ID, ACCOUNT2_CLIENT_SECRET, 'second')

    write_credentials('credentials.py',
                      ACCOUNT1_CLIENT_ID, ACCOUNT1_CLIENT_SECRET, user_refresh_token1,
                      ACCOUNT2_CLIENT_ID, ACCOUNT2_CLIENT_SECRET, user_refresh_token2)
    logger.info('credentials.py has been updated with new refresh tokens.')

if __name__ == "__main__":
    main()
