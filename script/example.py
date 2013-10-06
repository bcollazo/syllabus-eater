#!/usr/bin/env python
from __future__ import print_function
from alchemyapi import AlchemyAPI
import unicodedata
import json

alchemyapi = AlchemyAPI()

# CONSTANTS
PROF_KWS = {'prof.', 'professor', 'instructor', 'teacher', 'lecturer'}
WEEKDAYS = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'mon', 'tue', 'wed', 'thurs', 'fri'}
MONTHS = {'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'november', 'december', 'jan', 'feb', 'mar', 'apr', 'jun', 'jul', 'aug', 'sep', 'dec'}
DATES_KWS = {'date', 'dates', 'meeting', 'meetings', 'appointment', 'appointments', 'office', 'hours'}.union(WEEKDAYS).union(MONTHS)
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
	"grading_scheme": (None, 0),
	"website":(None, 0)}


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
			keywords.extend([keyword])
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


def getString(unic):
	return unicodedata.normalize('NFKD', unic).encode('ascii','ignore')

def addImpDate(sentence):
	if course["important_dates"][0] == None:
		course["important_dates"] = ([sentence], 1) #TODO: LOL... VERY CONFIDENT...
	else:
		course["important_dates"] = (course["important_dates"][0] + [sentence], 1)


def processSyllabus():
	f = open('public/uploads/127.0.0.1/6046.txt', 'r')
	demo_text = f.read()
	n = len(demo_text)
	demo_text_sentences = demo_text.split(". ")
	for i in demo_text_sentences:

		sentence = i.strip()
		if sentence == "":
			print("Text '"+i+"' is empty")
			continue

		entities = getEntities(sentence)
		keywords = getKeywords(sentence)
			
		if keywords != None:
			if len(DATES_KWS.intersection({u["text"].lower() for u in keywords})) != 0:
				addImpDate(sentence)
#				print("")
#				print("Sentence to be processed:", i)
				if entities != None:
					pass
#					print("\t\tEntities:", [u["text"] for u in entities])
#					print("\t\tKeywords:", [u["text"] for u in keywords])

	print(json.dumps(course, indent=4))

if __name__ == "__main__": 
	processSyllabus()
