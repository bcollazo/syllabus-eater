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
course = {"id": (None, 0),
	"title": (None, 0),
	"prof_name": (None, 0),
	"email": (None, 0),
	"phone": (None, 0),
	"meeting_times": (None, 0),
	"location": (None, 0),
	"important_dates": (None, 0),
	"grading_scheme": (None, 0)}

	

def getEntities(demo_text):
#	print('############################################')
#	print('#   Entity Extraction Example              #')
#	print('############################################')
	entities = []
	response = alchemyapi.entities('text',demo_text, { 'sentiment':1 })

	if response['status'] == 'OK':
#		print('## Response Object ##')
#		print(json.dumps(response, indent=4))
		for entity in response['entities']:
			entities.extend([entity])
#			print('text: ', entity['text'])
#			print('type: ', entity['type'])
#			print('relevance: ', entity['relevance'])
		return entities
	else:
		print('Error in entity extraction call: ', response['statusInfo'])
		return None

def getKeywords(demo_text):
#	print('############################################')
#	print('#   Keyword Extraction Example             #')
#	print('############################################')
	keywords = []
	response = alchemyapi.keywords('text',demo_text, { 'sentiment':1 })

	if response['status'] == 'OK':
#		print('## Response Object ##')
#		print(json.dumps(response, indent=4))
		for keyword in response['keywords']:
			keywords.append(keyword)
#			print('text: ', keyword['text'])
#			print('relevance: ', keyword['relevance'])
		return keywords
	else:
		print('Error in keyword extaction call: ', response['statusInfo'])
		return None


def getConcepts(demo_text):
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


def getCategory(demo_text):
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


def processSyllabus():
	f = open('../public/uploads/18510.txt', 'r')
	demo_text = f.read()
	n = len(demo_text)
	demo_text_sentences = demo_text.split("\n")
	for i in demo_text_sentences:

		sentence = i.strip()
		if sentence == "":
			print("Text '"+i+"' is empty")
			continue
		print("")
		print("Sentence to be processed:", i)

		entities = getEntities(sentence)

		keywords = getKeywords(sentence)

		if entities != None:
			print("Entities:", [u["text"] for u in entities])
		if keywords != None:
			print("Keywords:", [u["text"] for u in keywords])


processSyllabus()
