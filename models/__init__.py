#!/usr/bin/python3

from models.engine.file_storage import FileStorage

def initialize_storage():
    global storage
    if storage is None:
        storage = FileStorage()

storage = None
initialize_storage()
storage.reload()
