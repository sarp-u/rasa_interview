# common_questions mülakatta genel sorular için
# technical_questions mülakattaki teknik soruları için
# employee_satisfaction_questions hr tarafından yapılan memnuniyet tarzı olaylarda
# question1 = raw_data["technical_questions"][i]["question"] formatında çağrılabilir

import random
import json
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher


class ActionAskQuestions(Action):
    def name(self) -> Text:

        return "action_interview_questions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        f = open("C:\\Users\\Medepia\\PycharmProjects\\rasaProject\\rasa_tr\\actions\\test.json", encoding="utf8")
        raw_data = json.load(f)
        common = raw_data["common_questions"]
        technical = raw_data["technical_questions"]
        employee_satisfaction = raw_data["employee_satisfaction_questions"]
        intent = tracker.latest_message['intent'].get('name')
        print(intent)
        number = random.randint(0, 49)

        dispatcher.utter_message(text=common[number]['question'])

        return []

# aynı dosya içerisinde deneneip en kötü ihtimalle action içine gömme