#!/usr/bin/env python
from __future__ import print_function
from alchemyapi import AlchemyAPI
import json

f = open('../public/uploads/18510.txt', 'r')

demo_text = f.read()

n = len(demo_text)
demo_text_sentences = demo_text.split(".")
m = len(demo_text_sentences)
c = -1
while (c < m - 1):
	c += 1
	demo_text = demo_text_sentences[c]
	if demo_text.strip() == "":
		print("Text '"+demo_text+"' is empty")
		continue
	print("Text to be processed:", demo_text)



	#demo_url = 'http://blog.programmableweb.com/2011/09/16/new-api-billionaire-text-extractor-alchemy/'
	#demo_html = '<html><head><title>Python Demo | AlchemyAPI</title></head><body><h1>Did you know that AlchemyAPI works on HTML?</h1><p>Well, you do now.</p></body></html>'
		 

	alchemyapi = AlchemyAPI()

	print('############################################')
	print('#   Entity Extraction Example              #')
	print('############################################')

	response = alchemyapi.entities('text',demo_text, { 'sentiment':1 })

	if response['status'] == 'OK':
		print('## Response Object ##')
	#	print(json.dumps(response, indent=4))

		print('')
		print('## Entities ##')
		for entity in response['entities']:
			print('text: ', entity['text'])
			print('type: ', entity['type'])
			print('relevance: ', entity['relevance'])
			print('')
	else:
		print('Error in entity extraction call: ', response['statusInfo'])

	print('')
	print('############################################')
	print('#   Keyword Extraction Example             #')
	print('############################################')

	response = alchemyapi.keywords('text',demo_text, { 'sentiment':1 })

	if response['status'] == 'OK':
		print('## Response Object ##')
	#	print(json.dumps(response, indent=4))

		print('')
		print('## Keywords ##')
		for keyword in response['keywords']:
			print('text: ', keyword['text'])
			print('relevance: ', keyword['relevance'])
			print('')
	else:
		print('Error in keyword extaction call: ', response['statusInfo'])


	print('')
	print('############################################')
	print('#   Concept Tagging Example                #')
	print('############################################')

	response = alchemyapi.concepts('text',demo_text)

	if response['status'] == 'OK':
		print('## Object ##')
	#	print(json.dumps(response, indent=4))


		print('')
		print('## Concepts ##')
		for concept in response['concepts']:
			print('text: ', concept['text'])
			print('relevance: ', concept['relevance'])
			print('')
	else:
		print('Error in concept tagging call: ', response['statusInfo'])

	print('')
	print('############################################')
	print('#   Text Categorization Example            #')
	print('############################################')

	response = alchemyapi.category('text',demo_text)

	if response['status'] == 'OK':
		print('## Response Object ##')
	#	print(json.dumps(response, indent=4))


		print('')
		print('## Category ##')
		print('text: ', response['category'])
		print('score: ', response['score'])
		print('')
	else:
		print('Error in text categorization call: ', response['statusInfo'])



