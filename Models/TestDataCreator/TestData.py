import random
from datetime import datetime, timedelta

firstNames = ['John', 'Jane', 'Michael', 'Sarah', 'David', 'Emily', 'Daniel', 'Laura', 'Jessica', 'Kevin', 'Amanda', 'Eric', 'Melissa', 'Brian', 'Rachel', 'Alex', 'Olivia', 'Steven', 'Natalie', 'Andrew', 'Samantha', 'Joshua', 'Megan', 'Thomas', 'Lauren', 'Jacob', 'Ashley', 'Mark', 'Jennifer', 'Tyler', 'Katie', 'Adam', 'Stephanie', 'Nicholas', 'Madison', 'James', 'Emma', 'Robert', 'Molly', 'Ryan', 'Taylor', 'Brandon', 'Kayla', 'Christopher', 'Hannah']
lastNames = ['Smith', 'Johnson', 'Brown', 'Taylor', 'Wilson', 'Davis', 'Lee', 'Green', 'Evans', 'King', 'Baker', 'Morgan', 'Reed', 'Carter', 'Phillips', 'Campbell', 'Parker', 'Cooper', 'Peterson', 'Cox', 'Bailey', 'Murphy', 'Rivera', 'Gomez', 'Gray', 'Hughes', 'Stewart', 'Long', 'Garcia', 'Diaz', 'Lopez', 'Gonzalez', 'Rodriguez', 'Perez', 'Wright', 'Anderson', 'Clark', 'Allen', 'Adams', 'Bennett', 'Coleman', 'Duncan', 'Foster', 'Grant', 'Harris', 'Ingram']
# define a list of adjectives
adjectives = ['sleepy', 'happy', 'sad', 'bouncy', 'fierce', 'mellow', 'jolly', 'wise', 'funky', 'silly']
# define a list of nouns
nouns = ['unicorn', 'penguin', 'koala', 'panda', 'lion', 'tiger', 'monkey', 'dog', 'cat', 'rabbit']

age_groups = ['U6', 'U7', 'U8', 'U9', 'U10', 'U12', 'U13', 'U14', 'U15', 'U16', 'U17', 'U18', 'U20']
team_years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']
soccer_club_names = [
    "FC Barcelona", "Real Madrid CF", "Club Atlético de Madrid", "Valencia CF", "Sevilla FC", "Villarreal CF", "Real Betis", "Real Sociedad", "Athletic Club", "Deportivo Alavés", "SD Eibar", "Getafe CF", "CD Leganés", "Levante UD", "RCD Mallorca", "CA Osasuna", "Real Valladolid", "SD Huesca", "RC Celta", "RC Deportivo",
    "RC Recreativo", "Málaga CF", "Real Zaragoza", "UD Almería", "Córdoba CF", "Cádiz CF", "Rayo Vallecano", "Real Oviedo", "Racing de Santander", "CD Tenerife", "UD Las Palmas", "Real Sporting", "Elche CF", "UD Salamanca", "Hércules CF", "CD Numancia", "CD Castellón", "UE Lleida", "CE Sabadell", "CD Logroñés", "CF Extremadura", "UD Melilla", "CF Badalona", "CF Villanovense", "CD Toledo", "UD San Sebastián de los Reyes", "SD Amorebieta", "CD Calahorra", "FC Andorra", "CP Villarrobledo", "UD Socuéllamos"]
team_names = [    "Panthers",    "Tigers",    "Bulldogs",    "Eagles",    "Sharks",    "Lions",    "Wolves",    "Hawks",    "Cougars",    "Knights",    "Mustangs",    "Wildcats",    "Dragons",    "Storm",    "Titans",    "Raiders",    "Warriors",    "Falcons",    "Vikings",    "Ravens",    "Jets",    "Bills",    "Dolphins",    "Patriots",    "Chiefs",    "Broncos",    "Rams",    "49ers",    "Cardinals",    "Cowboys",    "Giants",    "Eagles",    "Redskins",    "Buccaneers",    "Saints",    "Seahawks",    "Packers",    "Bears",    "Lions",    "Vikings",    "Texans",    "Colts",    "Titans",    "Jaguars",    "Ravens",    "Bengals",    "Browns",    "Steelers",    "Raiders",    "Chargers",    "Chiefs",    "Broncos",    "Braves",    "Indians",    "Cubs",    "Red Sox",    "White Sox",    "Yankees",    "Mets",    "Dodgers",    "Giants",    "Phillies",    "Athletics",    "Angels",    "Mariners",    "Rangers",    "Blue Jays",    "Expos",    "Padres",    "Astros",    "Cardinals",    "Marlins",    "Rockies",    "Diamondbacks",    "Devils",    "Maple Leafs",    "Canadiens",    "Oilers",    "Red Wings",    "Flyers",    "Rangers",    "Blackhawks",    "Bruins",    "Sharks",    "Lightning",    "Penguins",    "Islanders",    "Canucks",    "Flames",    "Jets",    "Capitals",    "Predators",    "Wild",    "Sabres",    "Golden Knights",    "Kraken"]
soccer_positions = ["Goalkeeper", "Right back", "Center back", "Left back", "Defensive midfielder", "Central midfielder", "Attacking midfielder", "Right winger", "Striker", "Left winger"]
dominate_foot = ["Right", "Left", "Both"]
tryout_tags = ["00001", "00002"]

email_list = [    'john.doe@example.com',    'jane.doe@example.com',    'jimmy.smith@example.com',    'susan.baker@example.com',    'mike.wilson@example.com',    'karen.hall@example.com',    'david.young@example.com',    'elizabeth.gray@example.com',    'steve.parker@example.com',    'tina.carter@example.com',    'george.andrews@example.com',    'rachel.cooper@example.com',    'andrew.smith@example.com',    'samantha.green@example.com',    'peter.white@example.com',    'carol.jones@example.com',    'jason.miller@example.com',    'natalie.davis@example.com',    'kevin.harris@example.com',    'emily.thomas@example.com']
phone_numbers = [    '555-555-5555',    '123-456-7890',    '234-567-8901',    '345-678-9012',    '456-789-0123',    '567-890-1234',    '678-901-2345',    '789-012-3456',    '890-123-4567',    '901-234-5678',    '432-109-8765',    '543-210-9876',    '654-321-0987',    '765-432-1098',    '876-543-2109',    '987-654-3210',    '012-345-6789',    '543-210-9876',    '987-654-3210',    '246-802-4680']
birthdays = ['{:02d}/{:02d}/2008'.format(m, d) for m, d in zip(range(1, 13), range(1, 21, 1))]
_numbers_one = list(range(100))
numbers = [str(num).zfill(2) for num in _numbers_one]
days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

coach_img_urls = ['https://randomuser.me/api/portraits/men/46.jpg', 'https://randomuser.me/api/portraits/men/32.jpg', 'https://randomuser.me/api/portraits/men/30.jpg', 'https://randomuser.me/api/portraits/men/24.jpg', 'https://randomuser.me/api/portraits/women/23.jpg', 'https://randomuser.me/api/portraits/men/22.jpg', 'https://randomuser.me/api/portraits/men/18.jpg', 'https://www.famousbirthdays.com/headshots/nick-saban-1.jpg', 'https://randomuser.me/api/portraits/men/3.jpg', 'https://randomuser.me/api/portraits/men/9.jpg']
player_img_urls = ['https://randomuser.me/api/portraits/women/70.jpg', 'https://randomuser.me/api/portraits/women/66.jpg', 'https://randomuser.me/api/portraits/women/57.jpg', 'https://randomuser.me/api/portraits/women/55.jpg', 'https://randomuser.me/api/portraits/women/54.jpg', 'https://randomuser.me/api/portraits/women/52.jpg', 'https://randomuser.me/api/portraits/women/41.jpg', 'https://randomuser.me/api/portraits/women/47.jpg', 'https://randomuser.me/api/portraits/women/35.jpg', 'https://randomuser.me/api/portraits/women/43.jpg', 'https://randomuser.me/api/portraits/women/45.jpg', 'https://randomuser.me/api/portraits/women/31.jpg', 'https://randomuser.me/api/portraits/women/25.jpg', 'https://randomuser.me/api/portraits/men/16.jpg', 'https://randomuser.me/api/portraits/women/13.jpg', 'https://randomuser.me/api/portraits/men/12.jpg', 'https://randomuser.me/api/portraits/women/11.jpg', 'https://www.famousbirthdays.com/headshots/naomi-osaka-1.jpg', 'https://www.famousbirthdays.com/headshots/lionel-messi-2.jpg', 'https://randomuser.me/api/portraits/women/10.jpg']

coach_note_player = [    "She has great ball control and can quickly get out of tight spaces.",    "He needs to work on his defensive skills, but has great potential as a forward.",    "She's one of the most consistent players on the team and is always a threat to score.",    "He needs to focus more on passing and playing as a team player.",    "She has a great work ethic and always gives 110% in practice and games.",    "He has great speed and can beat defenders one-on-one with ease.",    "She needs to work on her left foot, but her right foot is a cannon.",    "He has a great sense of positioning and always seems to be in the right place at the right time.",    "She's a bit of a risk taker on the field, but it pays off when she scores goals.",    "He's a natural leader on and off the field and sets a great example for the rest of the team."]
coach_note_team = [
    "I'm starting to think we should change our name to 'The Losers.'",
    "It's like they're not even trying out there.",
    "You know what our team needs? A miracle.",
    "I'm not saying we're terrible, but I'm pretty sure the other teams feel sorry for us.",
    "I'm not mad, I'm just disappointed. Actually, no, I'm definitely mad too.",
    "It's like they don't even know the rules of the game.",
    "I'm starting to think we should just forfeit the rest of the season.",
    "At this point, I'm pretty sure my grandmother could play better than these guys.",
    "I don't know what they're doing out there, but it's not soccer.",
    "It's like they're allergic to the ball or something."
]
class DataGeneration:

    @staticmethod
    def get_random(list_of_items):
        return random.choice(list_of_items)
    @staticmethod
    def generate_full_name():
        return str(random.choice(firstNames) + " " + random.choice(lastNames))
    @staticmethod
    def get_first_name(fullname:str):
        return fullname.split()[0]
    @staticmethod
    def get_last_name(fullname:str):
        return fullname.split()[1]
    @staticmethod
    def generate_username():
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        username = adjective + '_' + noun
        return username
    @staticmethod
    def generate_email():
        return random.choice(email_list)
    @staticmethod
    def generate_phone_number():
        return random.choice(phone_numbers)
    @staticmethod
    def generate_birthday():
        return random.choice(birthdays)
    @staticmethod
    def generate_number():
        return random.choice(numbers)
    @staticmethod
    def generate_tryout_tag():
        # generate a random integer between 0 and 99999
        num = random.randint(0, 99999)
        # convert the integer to a string with leading zeroes
        num_str = str(num).zfill(5)
        return num_str
    @staticmethod
    def generate_player_rank(rosterSize:int=20):
        # generate a random integer between 0 and 99999
        num = random.randint(0, rosterSize)
        return num
    @staticmethod
    def generate_coach_note_player():
        return random.choice(coach_note_player)
    @staticmethod
    def generate_team_name():
        return random.choice(team_names)
    @staticmethod
    def generate_coach_note_team():
        return random.choice(coach_note_team)
    @staticmethod
    def generate_position():
        return random.choice(soccer_positions)
    @staticmethod
    def generate_foot():
        return random.choice(dominate_foot)
    @staticmethod
    def generate_age_group():
        return random.choice(age_groups)
    @staticmethod
    def generate_team_year():
        return random.choice(team_years)
    @staticmethod
    def generate_player_img_url():
        return random.choice(player_img_urls)
    @staticmethod
    def generate_coach_img_url():
        return random.choice(coach_img_urls)
    @staticmethod
    def random_time():
        hour = random.randint(1, 12)
        minute = random.randint(0, 59)
        am_pm = random.choice(['AM', 'PM'])
        hour_str = str(hour).zfill(2)
        minute_str = str(minute).zfill(2)
        time_str = f"{hour_str}:{minute_str} {am_pm}"
        return time_str
    @staticmethod
    def random_time_range():
        start_hour = random.randint(1, 12)
        end_hour = random.randint(start_hour, 12)
        minute = random.randint(0, 59)
        am_pm = random.choice(['AM', 'PM'])
        start_hour_str = str(start_hour).zfill(2)
        end_hour_str = str(end_hour).zfill(2)
        minute_str = str(minute).zfill(2)
        start_time_str = f"{start_hour_str}:{minute_str} {am_pm}"
        end_time_str = f"{end_hour_str}:{minute_str} {am_pm}"
        return start_time_str, end_time_str
    @staticmethod
    def random_date_range(months:int=4):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=months * 30)
        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        random_date = start_date + timedelta(days=random_days)
        start_date_str = start_date.strftime("%m/%d/%Y")
        end_date_str = random_date.strftime("%m/%d/%Y")
        return start_date_str, end_date_str
    @staticmethod
    def get_age_for_birthday(birthdate:str):
        from F import DATE
        birthdate = DATE.parse_str_to_datetime(birthdate)
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    @staticmethod
    def generate_coachRef(userId:str=None, toDict:bool=True):
        from Models.Users.Coach import CoachRef
        coach = CoachRef()
        if userId:
            coach.id = userId
            coach.coachId = userId
        if toDict:
            return coach.__dict__
        return coach
    @staticmethod
    def generate_playerRef(toDict:bool=True):
        from Models.Users.Player import PlayerRef
        player = PlayerRef()
        if toDict:
            return player.__dict__
        return player
    @staticmethod
    def generate_roster(num_players:int=20) -> dict:
        from Models.Roster import Roster
        roster = Roster()
        roster.season = DataGeneration.generate_team_year()
        player_refs = []
        for i in range(num_players):
            newPlayerRef = DataGeneration.generate_playerRef()
            player_refs.append(newPlayerRef)
        roster.players = player_refs
        return roster.__dict__

    @staticmethod
    def generate_coach_roster(coachId, roster):
        from Models.Roster import CoachRosters
        item = {"coachId": coachId, "rosters": [roster]}
        coachRoster = CoachRosters(item)
        return coachRoster.__dict__


    @staticmethod
    def generate_coaches(num_players: int = 1) -> [dict]:
        coach_refs = []
        for i in range(num_players):
            newCoachRef = DataGeneration.generate_coachRef()
            coach_refs.append(newCoachRef.__dict__)
        return coach_refs
    @staticmethod
    def generate_team() -> dict:
        from Models.Team import Team
        team = Team()
        return team.__dict__
    @staticmethod
    def generate_teamRef() -> dict:
        from Models.Team import TeamRef
        team = TeamRef()
        return team.__dict__

    @staticmethod
    def generate_tryout(team_obj:dict=None):
        from Models.TryOut import TryOut
        if not team_obj:
            team_obj = DataGeneration.generate_team()
        tryout = TryOut(team_obj)
        return tryout.__dict__

    @staticmethod
    def generate_practice_event(day="monday", toDict:bool=True):
        from Models.Schedule import Event
        startTime, endTime = DataGeneration.random_time_range()
        startDate, endDate = DataGeneration.random_date_range()
        event = Event()
        event.isRecurring = True
        event.startDate = startDate
        event.endDate = endDate
        event.startTime = startTime
        event.endTime = endTime
        event.eventName = "Practice"
        event.day = day
        if toDict:
            return event.__dict__
        return event
    @staticmethod
    def generate_practice_schedule(name="Spring Practice Schedule") -> dict:
        from Models.Schedule import Schedule
        start_date, end_date = DataGeneration.random_date_range()
        schedule = Schedule()
        schedule.name = name
        scheduleObj = schedule.__dict__
        for day in days_of_week:
            # create a json object of Event
            tempEvent = DataGeneration.generate_practice_event(day=day, toDict=True)
            tempEvent['startDate'] = start_date
            tempEvent['endDate'] = end_date
            scheduleObj[day] = tempEvent
        return scheduleObj

    @staticmethod
    def generate_tryout_event(day="monday", toDict: bool = True):
        from Models.Schedule import Event
        startTime, endTime = DataGeneration.random_time_range()
        startDate, endDate = DataGeneration.random_date_range(1)
        event = Event()
        event.isRecurring = False
        event.startDate = startDate
        event.endDate = endDate
        event.startTime = startTime
        event.endTime = endTime
        event.eventName = "Try-Outs"
        event.day = day
        if toDict:
            return event.__dict__
        return event

    @staticmethod
    def generate_tryout_schedule(name="Tryouts: 2023/2024") -> dict:
        from Models.Schedule import Schedule
        start_date, end_date = DataGeneration.random_date_range(1)
        schedule = Schedule()
        schedule.name = name
        scheduleObj = schedule.__dict__
        for day in days_of_week:
            # create a json object of Event
            tempEvent = DataGeneration.generate_tryout_event(day=day, toDict=True)
            tempEvent['startDate'] = start_date
            tempEvent['endDate'] = end_date
            scheduleObj[day] = tempEvent
        return scheduleObj