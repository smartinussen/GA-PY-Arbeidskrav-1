# Oppgave 3 - Funksjoner og dokumentasjon
from datetime import date, datetime, time, timedelta

# Helper functions
def parse_date(date_string: str) -> date:
    """Return a date from input as dd.mm.yyyy text. Raises ValueError if invalid."""
    return date.strptime(date_string, "%d.%m.%Y")


def parse_time(time_string: str ) -> tuple:
    return time.strptime(time_string, "%H:%M")

# Input functions
def ask_for_minutes(prompt: str) -> int:
    """Ask until the user gives a valid input: int."""
    while True:
        user_input: str = input(prompt)
        try:
            add_minutes = int(user_input)
            if not add_minutes > 0:
                print("Wrong input: Only positive integers accepted")
                continue
            return add_minutes
        except ValueError:
            print("Wrong input: Only positive integers accepted")


def ask_for_date(prompt: str) -> date:
    while True:
        date_input = input(prompt)
        try:
            return parse_date(date_input)
        except ValueError as err:
            print(f"Invalid value. Please use a valid date in dd.mm.yyyy format\nValueError: {err}")


def ask_for_time(prompt) -> time:
    while True:
        start_time = input(prompt)
        try:
            return parse_time(start_time)
        except ValueError as err:
            print(f"Invalid value. Please enter a valid time in hh:mm format\nValueError: {err}")

def end_time(start_time: time, add_minutes: int) -> time:
    default_date = parse_date("01.01.1977")
    startingtime = datetime.combine(default_date, start_time)
    duration = timedelta(minutes=add_minutes)
    return datetime.time(startingtime + duration)


#==================================


#----------------------------------------------
# Testing of functions
# print(ask_for_date("Tast inn en dato dd.mm.yyyy: "))
# startingtime = (ask_for_time("Tast inn starttidspunkt: "))
# minutestest = timedelta(minutes=(ask_for_minutes("Tast inn antall minutter brukt: ")))
#
# temp1 = datetime.combine(default_date, startingtime)
# new_time = temp1 + minutestest
# print(datetime.time(new_time))

#add_time = ask_for_time("Tast inn tidspunkt: ")
#add_minutes = ask_for_minutes("Tast inn minutter brukt: ")
# print(end_time(add_time, add_minutes))

print(end_time(time.strptime("xx:00", "%H:%M"), 33))