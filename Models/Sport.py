
import time


class Sport:
    def __init__(self, data_dict):
        self.id = data_dict.get("id")
        self.isVisible = data_dict.get("isVisible", True)
        self.dateCreated = data_dict.get("dateCreated", time.time())
        self.dateUpdated = data_dict.get("dateUpdated", time.time())
        self.name = data_dict.get("name")
        self.firstName = data_dict.get("firstName")
        self.lastName = data_dict.get("lastName")
        self.type = data_dict.get("type")
        self.subType = data_dict.get("subType")
        self.details = data_dict.get("details")
        self.isFree = data_dict.get("isFree", False)
        self.status = data_dict.get("status")
        self.mode = data_dict.get("mode")
        self.imgUrl = data_dict.get("imgUrl")
        self.sport = data_dict.get("sport")
