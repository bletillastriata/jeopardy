import csv
import os
import datetime

os.chdir('/home/grey')

from clues.models import Clue

with open('final_api_data') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		date = row['airdate'][0:10]
		date_t = datetime.datetime.strptime(date, '%Y-%m-%d').date()

		p = Clue(
				clue_id = row['id'],
				answer = row['answer'],
				question = row['question'],
				value = row['value'],
				airdate = date_t,
				cate_id = row['category_id'],
				category_info = row['category'],
				category = row['category_name']
			)
		p.save()