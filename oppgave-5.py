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


    def __repr__(self) -> str:
        return f"id: {self.record_id} - {self.title} - {self.category} - {self.date.strftime("%d.%m.%Y")} - {self.estimated_minutes} - {self.status}"

    def completed(self):
        self.status = "completed"

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


def mark_activity_completed(actid: str) -> str | None:
    for act in activities:
        if act.record_id == actid and act.status.lower() == "completed":
            return "is_completed"
        elif act.record_id == actid:
            act.completed()
            return "completed"
    return None



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


# Second version of get_filtered_activities, assisted by AI with suggestion and explanation on getattr.
def get_filtered_activities(activities: list[Activity], field: str, criteria: str) -> list[Activity]:
    results = []
    for act in activities:
        if criteria.lower() == getattr(act, field).lower():
            results.append(act)
    return results

# TODO - Move variable assignment to menu same as menu option 4
def sort_activites(activitylist: list[Activity], criteria) -> list[Activity]:
    if criteria == "d":
        sort_by = "date"
    elif criteria == "m":
        sort_by = "estimated_minutes"
    return sorted(activitylist, key=lambda s: getattr(s, sort_by), reverse=True)


# Helper functions
def parse_date(date_string: str) -> dateclass:
    """Return a date from input as dd.mm.yyyy text. Raises ValueError if invalid."""
    return dateclass.strptime(date_string, "%d.%m.%Y")

def calc_total_est_time(actlist: list[Activity]) -> int:
    return sum(act.estimated_minutes for act in actlist)



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
                print("You selected: Register activities")
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
                    else:
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
                print("You selected: Sort activities by date or duration")
                while True:
                    user_input = ask_for_text("Enter 'd' to sort by date, or 'm' to sort by duration: ")
                    if user_input not in ("d", "m"):
                        print("Wrong choice, try again")
                        continue
                    sorted_activities = sort_activites(activities, user_input)
                    if not sorted_activities:
                        print("No activities found. Returning")
                        break
                    for act in range(len(sorted_activities)):
                        print(sorted_activities[act])
                    break

            case "6":
                print("You selected: Mark activity as completed")
                for act in range(len(activities)):
                    print(activities[act])
                while True:
                    actid = ask_for_text("Which activity do you want to mark as completed (uuid) or 'r' to return: ")
                    if actid.lower() == "r":
                        break
                    result = mark_activity_completed(actid)
                    if result == "is_completed":
                        print(f"Activity {actid} is already completed. Try another")
                        continue
                    elif result == "completed":
                        print(f"Activity {actid} was marked as 'completed'")
                    else:
                        print(f"Activity {actid} was not found. Try again")

            case "7":
                print("You selected: Show no.of activities, total estimated time and no. of completed")
                total_activities = len(activities)
                if not total_activities:
                    print("No activities found")
                    continue
                hours_est, minutes_est = divmod(calc_total_est_time(activities), 60)
                total_completed_activities = len(get_filtered_activities(activities, "status", "completed"))
                separator()
                print(f"You have {total_activities} activites registered, of which {total_completed_activities} is 'completed'")
                print(f"Total estimated time: {hours_est} hours and {minutes_est} mins")


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
    activities.append(Activity("Tittel 1", "Kategori 1", parse_date("01.09.2026"), 45, "coMpleted"))
    activities.append(Activity("Tittel 2", "Kategori 1", parse_date("23.09.2026"), 60, "completed"))
    activities.append(Activity("Tittel 3", "Kategori 2", parse_date("26.09.2026"), 60, "planned"))
    activities.append(Activity("Tittel 4", "Kategori 2", parse_date("21.09.2026"), 58, "plaNNed"))
    activities.append(Activity("Tittel 5", "Kategori 3", parse_date("29.09.2026"), 30, "planned"))
    activities.append(Activity("Tittel 6", "Kategori 3", parse_date("30.09.2026"), 90, "planneD"))
    main()
