from typing import List
import os
import csv
from src.account import (
	Transfers,
	Transfer, 
	TransferType, 
	Currency,
	transfers as trans,
)


class CsvLoader:

	def __init__(self)-> None:
		self.transfers = []

	def fmt_note(self, note: str)-> str:
		words = []
		for word in note.split(" "):
			if word == "":
				continue
			if "\t" in word:
				word = word.replace("\t", " ")

			words.append(word.strip())

		return " ".join(words)

	def load_folder(self, folder_path: str)-> None:
		[
			self.load_file(file.path) 
			for file in os.scandir(folder_path)
			if file.is_file() and ".csv" in file.path
		]

	def load_file(self, file_path: str)-> None:
		with open(file_path, "r") as file:
			reader = csv.reader(file, delimiter=",", skipinitialspace=True)
			for i, row in enumerate(reader):
				if i == 0:
					continue

				if len(row) == 0:
					continue
				
				acc_details = row[2].split(" ")

				self.transfers.append({
					"date": row[1],
					"account_number": acc_details[1],
					"sort_code": acc_details[0],
					"amount": row[3], 
					"category": row[4], 
					"note": self.fmt_note(row[5]),
				})

	def as_transfer_list(self)-> List[Transfer]:
		return [
			Transfer(
				t["amount"],
				Currency.GBP,
				TransferType.DEPOSIT if float(t["amount"]) > 0 else TransferType.WITHDRAWAL,
				t["category"], 
				t["note"],
				t["date"],
			) for t in self.transfers
		]

	def as_transfers(self)-> Transfers:
		return trans(self.as_transfer_list())