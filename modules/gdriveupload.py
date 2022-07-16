"""Uploads generated invoice to the Invoices folder on GoogleDrive
"""

from __future__ import print_function

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

def upload_to_folder(filename):
    """
    from: https://developers.google.com/drive/api/guides/folder#create
    Upload a file to the specified folder and prints file ID, folder ID
    Args: Id of the folder
    Returns: ID of the file uploaded

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    print(f'Uploading file {filename} to drive...\n')
    creds, _ = google.auth.load_credentials_from_file('creds.json')

    try:
        # create gmail api client
        service = build('drive', 'v3', credentials=creds)

        folder_id = '1_C-fAnZgSmfio28gpGks6ZPZRlW9G981'
        file_metadata = {
            'name': filename,
            'parents': [folder_id]
        }
        media = MediaFileUpload(filename,
                                mimetype=None, resumable=True)
        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, media_body=media,
                                      fields='id').execute()
        fileid = file.get('id')
        print('Operation completed.\n')
    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None
    end(fileid)


def end(fileid):
    """lists links to different folders/files

    Args:
        fileid (str): id for a created invoice if an invoice was created.
        Defaults to None.
    """
    print('-----Links-----')
    print('Open created invoice:')
    print(f"https://drive.google.com/file/d/{fileid}/view?usp=sharing")
    print('Open invoices folder:')
    print('https://drive.google.com/drive/folders/1_C-fAnZgSmfio28gpGks6ZPZRlW9G981?usp=sharing')
    print('Open spreadsheets folder:')
    print('https://drive.google.com/drive/folders/1pOgtupYWIjwE0W5tDjbob2cMwOyht9K6?usp=sharing\n')
