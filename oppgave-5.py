# Miniprosjekt: Aktivitetsplanlegger
import uuid
from datetime import date as dateclass


class Activity:
    def __init__(self, title: str, category: str, date: dateclass, estimated_minutes: int, status: str):
        self.record_id = uuid.uuid4().hex[:8]
        self.title = title
        self.category = category
        self.date = date
        self.estimated_minutes = estimated_minutes
        self.status = status

    def __str__(self) -> str:
        return f"id: {self.record_id} - {self.title} - {self.category} - {self.date} - {self.estimated_minutes} - {self.status}"

    def __repr__(self) -> str:
        return f"id: {self.record_id} - {self.title} - {self.category} - {self.date} - {self.estimated_minutes} - {self.status}"


activities: list[Activity] = []


def separator() -> None:
    print(30 * "-")


def ask_for_text(prompt: str) -> str:
    """Ask until the user gives a valid input: str."""
    while True:
        text_input: str = input(prompt)
        if text_input.strip() != "":
            return text_input.strip()
        print("Wrong or missing input. Try again")


def ask_for_int(prompt: str) -> int:  # This reports expect int | None but only int can be returned
    """Ask until the user gives a valid input: int."""
    while True:
        user_input: str = input(prompt)
        try:
            number = int(user_input)
            if not number > 0:
                print("Wrong input: Only positive integers accepted")
                continue
            return number
        except ValueError:
            print("Wrong input: Only positive integers accepted")


def ask_for_date(prompt: str) -> dateclass:
    """Ask until the user give a valid date input: dd.mm.yyyy """
    while True:
        date_input = input(prompt)
        try:
            return parse_date(date_input)
        except ValueError as err:
            print(f"Invalid value. Please use a valid date in dd.mm.yyyy format\nValueError: {err}")


def ask_for_status(prompt: str) -> str:
    """Ask until the user gives a valid input: str."""
    while True:
        text_input: str = input(prompt)
        if text_input.lower().strip() == "planned" or text_input.lower().strip() == "completed":
            return text_input.strip()
        print("Wrong/missing input. Only 'planned' or 'completed' is accepted")

# First version of the filtering function
# def get_filtered_activities(activities: list[Activity], field: str, criteria: str) -> list[Activity]:
#     results = []
#     if field == "title":
#         for act in activities:
#             if act.title.lower() in criteria.lower():
#                 results.append(act)
#     elif field == "category":
#         for act in activities:
#             if act.category.lower() in criteria.lower():
#                 results.append(act)
#     return results


# Second version, assisted by AI with suggestion and explanation on getattr.
def get_filtered_activities(activities: list[Activity], field: str, criteria: str) -> list[Activity]:
    results = []
    for act in activities:
        if criteria.lower() == getattr(act, field).lower():
            results.append(act)
    return results


# Helper functions
def parse_date(date_string: str) -> dateclass:
    """Return a date from input as dd.mm.yyyy text. Raises ValueError if invalid."""
    return dateclass.strptime(date_string, "%d.%m.%Y")


def main() -> None:
    while True:
        print(10 * "-", "    MENU     ", 10 * "-")
        print("1. Register new activities")
        print("2. Show all activities")
        print("3. Search for title or category")
        print("4. Filter by status")
        print("5. Sort by date or duration")
        print("6. Mark activity as completed")
        print("7. Show no. of activities, total est. time and no. of completed")
        print("8. Save activities to file")
        print("9. Read activites from file")
        print("Q. Quit program")
        print(10 * "-", " END OF MENU ", 10 * "-")
        menu_input = input("Please select an action (1-9 or 'Q'): ").lower()

        match menu_input:
            case "1":
                # print("You selected: Register activities")
                print("Register a new activity")
                separator()
                act_title = ask_for_text("Please enter a title: ")
                act_category = ask_for_text("Please enter a category: ")
                act_date = ask_for_date("Enter a date for the activity: ")
                act_duration = ask_for_int("Please enter duration in mins: ")
                act_status = ask_for_status("Register status ('planned' or 'completed'): ").lower()
                activities.append(Activity(act_title, act_category, act_date, act_duration, act_status))
            case "2":
                print("You selected: Show activities")
                for act in range(len(activities)):
                    print(activities[act])
            case "3":
                print("You selected: Search for activity or category")
                while True:
                    choice = ask_for_text("Enter 't' for title search, or 'c' for category search: ").lower()
                    if choice not in ("t", "c"):
                        print("Wrong choice, try again")
                        continue
                    if choice == "t":
                        choice = "title"
                    else:
                        choice = "category"
                    criteria = ask_for_text("Enter search criteria: ").lower()
                    results = get_filtered_activities(activities, choice, criteria)
                    if not results:
                        print("No results found")
                        break
                    else:
                        for result in results:
                            print(result)
                        break
            case "4":
                print("You selected: Filter by status")
                while True:
                    user_input = ask_for_text("Enter 'p' or 'c' to show planned or completed activities: ").lower()
                    if user_input not in ("p", "c"):
                        print("Wrong choice, try again")
                        continue
                    if user_input == "p":
                        criteria = "planned"
                    elif user_input == "c":
                        criteria = "completed"
                    results = get_filtered_activities(activities, "status", criteria)
                    if not results:
                        print("No results found")
                        break
                    else:
                        for result in results:
                            print(result)
                        break

            case "5":
                print("You selected: Sort by date or duration")
            case "6":
                print("You selected: Mark activity as completed")
            case "7":
                print("You selected: Show no.of activities, total estimated time and no. of completed")
            case "8":
                print("You selected: Save activities to file")
            case "9":
                print("You selected: Read activites from file")
            case "q":
                print("You selected: Quit program. Have a nice day")
                break
            case _:
                print(f"Incorrect alternative > {menu_input} <: Try again")


if __name__ == "__main__":
    activities.append(Activity("Tittel 1", "Kategori 1", parse_date("23.09.2026"), 45, "coMpleted"))
    activities.append(Activity("Tittel 2", "Kategori 1", parse_date("23.09.2026"), 45, "completed"))
    activities.append(Activity("Tittel 3", "Kategori 2", parse_date("26.09.2026"), 45, "planned"))
    activities.append(Activity("Tittel 4", "Kategori 2", parse_date("26.09.2026"), 45, "plaNNed"))
    activities.append(Activity("Tittel 5", "Kategori 3", parse_date("29.09.2026"), 45, "planned"))
    activities.append(Activity("Tittel 6", "Kategori 3", parse_date("29.09.2026"), 45, "planneD"))
    main()
