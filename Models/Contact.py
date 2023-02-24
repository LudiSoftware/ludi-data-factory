
import uuid


class Contact:
    def __init__(self, json_obj={}):
        self.id = json_obj.get('id', str(uuid.uuid1()))
        self.contactId = json_obj.get('contactId', [])
        self.name = json_obj.get('name', [])
        self.email = json_obj.get('email', [])
        self.phone = json_obj.get('phone', [])
        self.relationship = json_obj.get('relationship', [])