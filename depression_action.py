# !/usr/bin/env python
# -*-coding: utf-8 -*-
"""This is View action script."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import AllSlotsReset
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.events import Restarted
from rasa_core_sdk.forms import FormAction
# from rasa_core_sdk.executor import CollectingDispatcher
import sqlite3
import logging
import re
import random


class Action_Output(Action):
    """Action1."""
    def name(self):
        return "action_recom"

    def run(self, dispatcher, tracker, domain):
        print(self.name())
        print(tracker.current_slot_values())
        books = ["雖然想死，但還是想吃辣炒年糕",
                 "雖然想死，但還是想吃辣炒年糕2",
                 "活著的理由",
                 "有時候，不加油也沒關係",
                 "被討厭的勇氣",
                 "被討厭的勇氣2"]
        r = random.randint(0, 5)
        dispatcher.utter_message(f"推薦你看這本書{books[r]}")

        return []