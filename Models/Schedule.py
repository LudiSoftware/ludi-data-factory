
class Event:
    def __init__(self, schedule_obj={}):
        self.eventName = schedule_obj.get('eventName', "Practice")
        self.startDate = schedule_obj.get('startDate', "02/01/2023")
        self.startTime = schedule_obj.get('startTime', "5:15pm")
        self.endDate = schedule_obj.get('endDate', "05/12/2023")
        self.endTime = schedule_obj.get('endTime', "7:00pm")
        self.day = schedule_obj.get('day', "monday")
        self.isRecurring = schedule_obj.get('isRecurring', False)
        self.location = schedule_obj.get('location', None)
        self.field = schedule_obj.get('field', "2A")

class Schedule:
    def __init__(self, schedule_obj={}):
        self.name = schedule_obj.get('name', "Spring Practice")
        self.startDate = schedule_obj.get('startDate', "02/01/2023")
        self.endDate = schedule_obj.get('endDate', "05/12/2023")
        self.monday = schedule_obj.get('monday', Event({"isRecurring": True}).__dict__)
        self.tuesday = schedule_obj.get('tuesday', Event({"isRecurring": True}).__dict__)
        self.wednesday = schedule_obj.get('wednesday', Event({"isRecurring": True}).__dict__)
        self.thursday = schedule_obj.get('thursday', Event({"isRecurring": True}).__dict__)
        self.friday = schedule_obj.get('friday', Event({"isRecurring": True}).__dict__)
        self.saturday = schedule_obj.get('saturday', Event({"isRecurring": True}).__dict__)
        self.sunday = schedule_obj.get('sunday', Event({"isRecurring": True}).__dict__)

