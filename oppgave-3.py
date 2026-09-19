# Oppgave 3 - Funksjoner og dokumentasjon
from datetime import date, datetime, time, timedelta


# Helper functions
def parse_date(date_string: str) -> date:
    """Return a date from input as dd.mm.yyyy text. Raises ValueError if invalid."""
    return date.strptime(date_string, "%d.%m.%Y")


def parse_time(time_string: str) -> tuple:
    return time.strptime(time_string, "%H:%M")


def separator() -> None:
    print(30 * "-")


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
            break
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


#
def end_time(start_time: time, add_minutes: int) -> time:
    default_date = parse_date("01.01.1977")
    startingtime = datetime.combine(default_date, start_time)
    duration = timedelta(minutes=add_minutes)
    return datetime.time(startingtime + duration)


def calculate_days(start_date: date, end_date: date) -> int:
    '''Return an absolute no of days between two input dates calculated as end-date - start-date '''
    return abs((end_date - start_date).days)


def sort_list_of_dates(dates: list[date]) -> list[date]:
        return sorted(dates)

# Main program and data below
dates_unsorted = [
    date(2026, 10, 1),
    date(2026, 9, 5),
    date(2026, 12, 12),
    date(2026, 5, 27),
    date(2011, 9, 3)
]

def main():
    valid_date = ask_for_date("Tast inn en dato: ")
    print(f"You have entered {valid_date}, and it is a valid date")
    separator()
    startingtime = (ask_for_time("Please input start time (hh:mm): "))
    minutes_used = ask_for_minutes("Please input the amount of minutes passed: ")
    new_time = end_time(startingtime, minutes_used).strftime("%H:%M")
    print(f"The time is {new_time} after {minutes_used} minutes have passed")
    separator()
    from_date = ask_for_date("Please enter a date (dd.mm.yyyy): ")
    to_date = ask_for_date("Please enter another date (dd.mm.yyyy): ")
    no_of_days_diff = calculate_days(from_date, to_date)
    print(f"It's {no_of_days_diff} days between the dates you gave")
    separator()
    dates_sorted = sort_list_of_dates(dates_unsorted)
    for d in dates_sorted:
        print(d.strftime("%d.%m.%Y"))
#===== MAIN PROGRAM =============================

if __name__ == "__main__":
    main()
