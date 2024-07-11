import datetime

class BirthdayReminder:
    def __init__(self, birthdays):
        self.birthdays = birthdays

    def check_birthdays(self):
        today = datetime.datetime.now().strftime("%m/%d")
        print(f"Today's date: {today}")

        for name, birthdate in self.birthdays.items():
            if birthdate[:-5] == today:
                print(f"Happy Birthday to: {name}")

birthdays = {
    "ryan": "06/01/1993",
    "danny": "06/03/1993",
    "john": "07/07/2004",
    "jim": "07/05/2019"
}

reminder = BirthdayReminder(birthdays)
reminder.check_birthdays()
