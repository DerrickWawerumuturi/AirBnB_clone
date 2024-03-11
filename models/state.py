#!/usr/bin/python3
""" The state that the user in in"""
from models.base_model import BaseModel

class State(BaseModel):
    """
    class state inherits from basemodel
    """
    def __init__(self):
        self.name = ""
