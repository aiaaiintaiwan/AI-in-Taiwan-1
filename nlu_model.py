# !/usr/bin/env python
# -*-coding: utf-8 -*-
"""This is train model and test nlu model script."""
import warnings
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
# from rasa_nlu.model import Metadata
from rasa_nlu.model import Interpreter
import pprint as aa
# from rasa_nlu_gao.training_data import load_data
# from rasa_nlu_gao import config
# from rasa_nlu_gao.model import Trainer
# from rasa_nlu_gao.model import Interpreter
# import monpa
# import tensorflow as tf
import os
import logging
import datetime
warnings.simplefilter(action='ignore', category=FutureWarning)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}



def train_nlu(data, configs, model_dir):
    """Train model."""
    training_data = load_data(data)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    trainer.persist(model_dir, fixed_model_name='depression')



if __name__ == '__main__':
    # data = f"stocks_new.json"
    data = f"depression_data.json"
    try:
        print('start')
        train_nlu(f"{data}",
                  f"configs/config_CKIP_mitie_sklearn.yml",
                  f"../models/nlu")
    except Exception as e:
        print(str(e))
    # input()