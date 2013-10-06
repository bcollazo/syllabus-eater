#!/usr/bin/env python
from __future__ import print_function
from alchemyapi import AlchemyAPI
import json

alchemyapi = AlchemyAPI()

# CONSTANTS
PROF_KWS = {'prof.', 'professor', 'instructor', 'teacher', 'lecturer'}
EMAIL_REGEXP = '' #TODO: Kido fill in
PHONE_REGEXP = '' #TODO: Kido fill in

# INITIALIZE EMPTY CLASS
course = {"code": (None, 0),
	"title": (None, 0),
	"prof_name": (None, 0),
	"email": (None, 0),
	"phone": (None, 0),
	"meeting_times": (None, 0),
	"location": (None, 0),
	"important_dates": (None, 0),
	"grading_scheme":(None, 0)}


f = open('../public/uploads/18510.txt', 'r')
demo_text = f.read()
n = len(demo_text)
demo_text_sentences = demo_text.split(".")
for i in demo_text_sentences

	demo_text = i.strip()
	if demo_text == "":
		print("Text '"+i+"' is empty")
		continue
	print("Text to be processed:", i) 



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



