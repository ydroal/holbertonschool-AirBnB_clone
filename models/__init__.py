#!/usr/bin/python3
'''Module to create instance of FileStorage'''

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
