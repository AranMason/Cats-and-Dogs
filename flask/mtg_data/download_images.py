import urllib.request as urllib
import json
import os

with open('scryfall-default-cards.json', encoding='utf-8') as json_file:
	data = json.load(json_file)

	# print(data[0]['image_uris']['art_crop'])
	# print(data[2]['color_identity'])

	for card in data:

		color_id = card['color_identity']

		folder_name = ''.join(str(x) for x in card['color_identity'])

		if(folder_name is ''):
			folder_name = 'colorless'

		image_uri = card['image_uris']['art_crop']

		card_name = card['name']

		directory = 'data/{folder}'.format(folder=folder_name)

		if not os.path.exists(directory):
			os.mkdir(directory)

		card_file_name = "{folder}/{card_name}.jpg".format(card_name=card_name, folder=directory)

		if not os.path.isfile(card_file_name):
			image = urllib.urlretrieve(image_uri, card_file_name)