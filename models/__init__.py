#!/usr/bin/python3
""" importing modules and calling reload()"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
