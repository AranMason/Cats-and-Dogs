import urllib.request as urllib
import json
import os
import time

with open('scryfall-default-cards.json', encoding='utf-8') as json_file:
	data = json.load(json_file)

	# print(data[0]['image_uris']['art_crop'])
	# print(data[2]['color_identity'])

	length = len(data)

	for card in data:

		#print("Downloaded {progress} of {length}".format(length=length, progress=))

		time.sleep(0.1) # Add a small delay to respect Scryfalls rate limiting requests.

		card_color_id = card['color_identity']

		if len(card_color_id) is 0:
			card_color_id = ['colorless']


		for color_id in card_color_id:

			image_uri = card['image_uris']['art_crop']

			directory = 'data/{folder}'.format(folder=color_id)

			if not os.path.exists(directory):
				os.mkdir(directory)

			file_name = "{card_name} - {multiverse_id}".format(card_name=card['name'], multiverse_id=card['oracle_id'])

			card_file_name = "{folder}/{card_name}.jpg".format(card_name=file_name, folder=directory)

			if not os.path.isfile(card_file_name):
				image = urllib.urlretrieve(image_uri, card_file_name)