# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional

#from rasa_core.events import AllSlotsReset
#from rasa_core.events import Restarted
from rasa_sdk import Tracker
#from bot import RestaurentAPI
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import smtplib, ssl
import re
import pandas as pd
#from rasa.core.tracker_store import TrackerStore
#from rasa.core.event_channel import EventChannel
#from rasa.core.trackers import ActionExecuted, DialogueStateTracker, EventVerbosity
import requests
#from rasa_core.domain import Domain
import psycopg2
from collections import Counter
import math, random
#import datetime
#import urllib.request
#import flask
#import datetime




class CustomerForm(FormAction):

    def name(self) -> Text:

        return "customer_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
 
        msg1 = [ "email", "name", "number"]
        return msg1

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "email": [
                self.from_entity(
                    entity="email"
                ),
                self.from_text(),
            ],
            "name": [
                self.from_entity(entity="name"),
                self.from_text(),
            ],
            "number": [self.from_entity(entity="contact"), self.from_text()],
        }
          

    def validate_number(self, value:Text, dispatcher:CollectingDispatcher, tracker:Tracker, domain: Dict[Text, Any])->Any:
        if len(value) > 9 and len(value) < 11 and value.isdigit() == True:
            return {"contact": value}
        else:
            dispatcher.utter_template("utter_wrong_contact", tracker)
            return {"contact": None}



    def validate_email(self, value:Text, dispatcher:CollectingDispatcher, tracker:Tracker, domain: Dict[Text, Any])->Any:
        ans=re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
        mo=ans.search(value)
        if mo != None:
            return {"email": value}
        else:
            dispatcher.utter_template("utter_wrong_email", tracker)
            return {"email": None}


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        
        dispatcher.utter_template("utter_submit", tracker)  
        return []
