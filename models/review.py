""" Review """
from models.base_model import BaseModel

class Review(BaseModel):
    """ class Review inherits from """
    def __init__(self):
        self.place_id = ""
        self.user_id = ""
        self.text =  ""