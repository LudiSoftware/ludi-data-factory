


class CustomAttribute:
    def __init__(self, json_obj={}):
        self.key = json_obj.get('key', "")
        self.value = json_obj.get('value', "")


