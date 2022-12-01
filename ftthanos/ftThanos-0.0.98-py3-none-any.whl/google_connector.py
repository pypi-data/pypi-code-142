from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class google_connector():
	def __init__(self, **kwargs):
		"""
			Build your connector object. Gdrive function and Gsheet function activate.
		"""
		SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']
		self.creds = None
		# The file token.json stores the user's access and refresh tokens, and is
		# created automatically when the authorization flow completes for the first
		# time.
		if os.path.exists('token.json'):
			self.creds = Credentials.from_authorized_user_file('token.json', SCOPES)
		# If there are no (valid) credentials available, let the user log in.
		if not self.creds or not self.creds.valid:
			if self.creds and self.creds.expired and self.creds.refresh_token:
				self.creds.refresh(Request())
			else:
				flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
				self.creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open('token.json', 'w') as token:
			token.write(self.creds.to_json())

	def show_folders(self, *args):
		"""
			Return list of file from your root drive if no argument.
			Return list of file from the drive repertory passed in first arguements
		"""
		service = build('drive', 'v3', credentials=self.creds)
		if len(args):
			query = f"'{args[0]}' in parents"
		else:
			query = None
		results = service.files().list(q=query, pageSize=999, fields="nextPageToken, files(id, name)").execute()
		items = results.get('files', [])
		return (items)

	def create_folders(self, name, *args):
		try:
		# create drive api client
			service = build('drive', 'v3', credentials=self.creds)
			file_metadata = {
			'name': name,
			'mimeType': 'application/vnd.google-apps.folder',
			}
			if len(args) > 0:
				file_metadata.update({
					'parents' : [args[0]]
					})
			file = service.files().create(body=file_metadata, fields='id'
			).execute()
			print(F'Folder ID: "{file.get("id")}".')
			return file.get('id')
		except HttpError as error:
			print(F'An error occurred: {error}')

	def copy_file(self, name, file_id, parent_id):
		try:
		# create drive api client
			service = build('drive', 'v3', credentials=self.creds)
			file_metadata = {
			'name': name,
			'parents': parent_id,
			'starred': False,
			}
			file = service.files().copy(body=file_metadata, fileId=file_id).execute()
			print(file)
			return file.get('id')
		except HttpError as error:
			print(F'An error occurred: {error}')

	def update_values(self, spreadsheet_id, cell_range, cell_values):
		try:
			service = build('sheets', 'v4', credentials=self.creds)
			data = {
			'values': cell_values
			}
			result = service.spreadsheets().values().update(
			spreadsheetId=spreadsheet_id,
			range=cell_range,
			valueInputOption='USER_ENTERED',
			body=data
			).execute()
			return result
		except HttpError as error:
			print(f"An error occurred: {error}")
			return error


