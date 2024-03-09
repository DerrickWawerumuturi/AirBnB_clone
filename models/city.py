""" City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """  CLASS city inherits from BaseModel"""
    def __init__(self):
        """ attributes: state_id, name"""
        self.state_id = ""
        self.name =  ""