import time
import uuid

class Base:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', str(uuid.uuid1()))
        self.dateCreated = kwargs.get('dateCreated', str(time.time()))
        self.dateUpdated = kwargs.get('dateUpdated', str(time.time()))
        self.name = kwargs.get('name', "Tryouts: Fall2023/Spring2024")
        self.type = kwargs.get('type', "competitive")
        self.subType = kwargs.get('subType', "youth")
        self.details = kwargs.get('details', "This is a no joke tryout joel!")
        self.isFree = kwargs.get('isFree', False)
        self.status = kwargs.get('status', "open")
        self.mode = kwargs.get('mode', "edit")
        self.imgUrl = kwargs.get('imgUrl', "")
        self.sport = kwargs.get('sport', "soccer")
        self.chatEnabled = kwargs.get('chatEnabled', True)