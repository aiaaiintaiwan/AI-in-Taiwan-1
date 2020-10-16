import 
# !/usr/bin/env python
# -*-coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from policy.mobile_policy import MobilePolicy
from policy.attention_policy import AttentionPolicy
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.form_policy import FormPolicy

from rasa_core.policies.embedding_policy import EmbeddingPolicy


def train_dialogue_keras(domain_file=f"configs/depression_domain.yml",
                         model_path=f"../models/dialogue_keras",
                         training_data_file=f"configs/depression_story.md"):

    fallback = FallbackPolicy(
        fallback_action_name="utter_unknown",
        nlu_threshold=0.3,
        core_threshold=0.4
    )

    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=8),
                            MobilePolicy(epochs=50, batch_size=4), fallback, FormPolicy()])

    training_data = agent.load_data(training_data_file)
    agent.train(
            training_data,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent


if __name__ == '__main__':
    train_dialogue_keras()
