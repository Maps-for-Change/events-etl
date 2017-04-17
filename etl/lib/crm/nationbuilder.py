# encoding=utf8

import os
import requests
import json
import datetime
import etl.lib.base.scraper as scraper
from pytz import timezone

class EventsScraper(scraper.Scraper):
    EVENTS_URI = "/api/v1/sites/%s/pages/events"
    
    def __init__(self, url, access_token=None, slug=None, calendar_id=None, event_types = {}, supergroup = None, subgroup = None):
        """
        url: base url for NationBuilder websites.
        access_token: Access Token for NB sites
        campaign_id: if you want to focus on a particular campaign 
        event_types: Dict of event types for description substrings. {"Phonebank": "phonebank"}
        """
        self.url = url[:-1] if url.endswith('/') else url
        self.access_token = access_token
        self.calendar_id = calendar_id
        self.slug = slug
        
        self.event_types = event_types
        
        self.clean_data = None
        self.raw_data = None
        
        self.supergroup = supergroup
        self.subgroup = subgroup
    
    def run(self):
        """
        This orchestrates the various methods
        """
        self.raw_data = self.retrieve()
        self.clean_data = self.clean(self.raw_data)
        self.minified_data = self.translate(self.clean_data)
        self.osdified_data = self.osdify(self.minified_data)

    def retrieve(self):
        """
        This is where the items will be processed
        by getting the data out
        """
        data = []
        # BASE
        next_url = self.EVENTS_URI % self.slug
        time_now = datetime.datetime.now().strftime('%Y-%m-%d')
        
        while next_url is not None:
            req = None
            next_url = self.url + next_url
            
            print(next_url)
            params = {'access_token': self.access_token, 'calendar_id': self.calendar_id, 'limit': 1, 'starting': time_now} if self.calendar_id is not None \
                        else {'access_token': self.access_token, 'limit': 1, 'starting': time_now}
            
            req = requests.get(next_url, params=params)
            
            if req is not None:
                json_msg = json.loads(req.text)
                next_url = json_msg['next']
                
                data = data + json_msg['results']
                # print(str(next_url))
            else:
                next_url = None


        return data
        # while has_more is not None:
        #     
        #     has_more = False;
        # 
        # if req.status_code != 200:
        #     raise ValueError("Error in retrieving ", req.status_code)
        # else:
        #     print(req.text)
        #     return json.loads(req.text)['results']

            
    def clean(self, raw):
        """
        This will clean the information out that is
        considered private information
        """
        # Nothing to clean
        return raw
        
    def translate(self, data):
        """
        This prepares the data for a singular 
        cleaned format
        """
        translated = []
        for item in data:
            
            venue = ' '.join( filter(None, [ \
                      item['venue']['name'],\
                      item['venue']['address']['address1'],\
                      item['venue']['address']['address2'],\
                      item['venue']['address']['city'],\
                      item['venue']['address']['state'],\
                      item['venue']['address']['zip'] \
                    ]))

            
            event_types = []
            for k in self.event_types:
                if (item['intro'].lower() + item['title'].lower()).find(k.lower()) >= 0:
                    event_types.append(self.event_types[k])
            
            translated.append({
                'supergroup': self.supergroup,
                'group': self.subgroup,
                'event_type': event_types,
                'title': item['title'],
                'url': self.url + item['path'],
                'venue': venue,
                'lat': item['venue']['address']['lat'],
                'lng': item['venue']['address']['lng'],
                'start_time': item['start_time'],
                'tz': None
            })
        #endof for item in data:
            
        return translated
        
        
    def osdify(self, data):
        """
        Translate the data to OSDI format
        """
