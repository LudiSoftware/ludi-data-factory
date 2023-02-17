from datetime import datetime, timedelta
import random


class Schedule:

    def __init__(self, schedule_obj=None):
        self.startDate = schedule_obj.get('startDate', None)
        self.startTime = schedule_obj.get('startTime', None)
        self.endDate = schedule_obj.get('endDate', None)
        self.endTime = schedule_obj.get('endTime', None)
        self.location = schedule_obj.get('location', None)
        self.field = schedule_obj.get('field', None)


def generate_test_schedules(num_objects):
    schedule_list = []
    for i in range(num_objects):
        start_date = datetime.now() + timedelta(days=random.randint(1, 365))
        start_time = datetime.strptime(f"{random.randint(0, 23)}:{random.randint(0, 59)}", "%H:%M").time()
        end_date = start_date + timedelta(days=random.randint(1, 7))
        end_time = datetime.strptime(f"{random.randint(0, 23)}:{random.randint(0, 59)}", "%H:%M").time()

        schedule = Schedule({
            'startDate': start_date.date(),
            'startTime': start_time,
            'endDate': end_date.date(),
            'endTime': end_time
        })

        schedule_list.append(schedule)

    return schedule_list