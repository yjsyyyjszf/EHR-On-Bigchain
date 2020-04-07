# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/



from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import infermedica_api

class ActionMed(Action):
    def name(self):
        return 'action_medicine'

    def run(self, dispatcher, tracker, domain):
        api = infermedica_api.API(app_id='f1acb630',
                                  app_key='41b6c31e0d5158d1dbab51958f216cfc')
        choices = {}
        buttons = []
        symp = tracker.get_slot('symptom')
        request = infermedica_api.Diagnosis(sex='male', age='25')

        symp = api.parse(symp).to_dict()
        symp_id = symp['mentions'][0]['id']
        request.add_symptom(symp_id, 'present')

        request = api.diagnosis(request)
        items = request.question.items

        for choice in items:
            choices[choice['id']] = choice['name']

        response = request.question.text

        for key, value in choices.items():
            title = value
            request.add_symptom(key, 'present')
            request = api.diagnosis(request)
            text = request.question.text
            buttons.append({"title": title, "payload": text})
            response = "Let's try this medicine"

        dispatcher.utter_button_message(response, buttons)
        return [SlotSet('symptom', symp)]


