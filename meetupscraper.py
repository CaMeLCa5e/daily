import requests

class MeetupEventScraper:
	def __init__(self):
		self.groups = ['nyc-python',
						'django-nyc'
		]

	def scrape_these_groups(self, key):
		meetup_dict = {}
		for group in self.groups:
			meetup_dict[group] = 'https://api.meetup.com/2/events?' \
			+ 'key=' + key \
			+ '&group_urlname=' + group + '&page=20'
		return meetup_dict

	def parse_events_json(self, key):

		group_events = {}
		for group in self.scrape_these_groups(key):
			r = requests.get(self.scrape_these_groups(key)[group])
			event_list = []
			for event in r.json()['results']:
				event_list.append( \
					(event['name'],))