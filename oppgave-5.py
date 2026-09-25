# Miniprosjekt: Aktivitetsplanlegger
import csv
import uuid
from datetime import date as dateclass


class Activity:
    def __init__(
        self,
        title: str,
        category: str,
        date: dateclass,
        estimated_minutes: int,
        status: str,
    ):
        self.record_id = uuid.uuid4().hex[:8]
        self.title = title
        self.category = category
        self.date = date
        self.estimated_minutes = estimated_minutes
        self.status = status

    def __repr__(self) -> str:
        return f"id: {self.record_id} - {self.title} - {self.category} - {self.date.strftime('%d.%m.%Y')} - {self.estimated_minutes} - {self.status}"

    def mark_completed(self) -> None:
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


def ask_for_int(
    prompt: str,
) -> int:  # This reports expect int | None but only int can be returned
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
    """Ask until the user give a valid date input: dd.mm.yyyy"""
    while True:
        date_input = input(prompt)
        try:
            return parse_date(date_input)
        except ValueError as err:
            print(
                f"Invalid value. Please use a valid date in dd.mm.yyyy format\nValueError: {err}"
            )


def ask_for_status(prompt: str) -> str:
    """Ask until the user gives a valid input: str."""
    while True:
        text_input: str = input(prompt)
        if (
            text_input.lower().strip() == "planned"
            or text_input.lower().strip() == "completed"
        ):
            return text_input.lower().strip()
        print("Wrong/missing input. Only 'planned' or 'completed' is accepted")


def mark_activity_completed(actid: str) -> str | None:
    for act in activities:
        if act.record_id == actid and act.status.lower() == "completed":
            return "is_completed"
        elif act.record_id == actid:
            act.mark_completed()
            return "completed"
    return None


# First version of the filtering function - Left in for assignment
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
def get_filtered_activities(
    activitylist: list[Activity], field: str, criteria: str
) -> list[Activity]:
    results = []
    for act in activitylist:
        if criteria.lower() == getattr(act, field).lower():
            results.append(act)
    return results


def sort_activities(activitylist: list[Activity], criteria: str) -> list[Activity]:
    return sorted(activitylist, key=lambda s: getattr(s, criteria), reverse=True)


def load_activities(actdict: csv.DictReader) -> None:
    valid_rows = []
    err_message = ""
    for row_num, row in enumerate(actdict, start=2):
        if not row["title"]:
            err_message = f"File has errors: Missing title in row {row_num} - {row}\nCorrect any issues and try again. File not imported"
            break
        elif not row["category"]:
            err_message = f"File has errors: Missing category in row {row_num} - {row}\nCorrect any issues and try again. File not imported"
            break
        elif row["status"].lower() not in ["planned", "completed"]:
            err_message = f"File has errors: Wrong status in row {row_num} - {row}\nCorrect any issues and try again. File not imported"
            break
        try:
            valid_rows.append(
                Activity(
                    row["title"],
                    row["category"],
                    dateclass.fromisoformat(row["date"]),
                    int(row["estimated_minutes"]),
                    row["status"].lower(),
                )
            )
        except ValueError as err:
            err_message = f"File has errors: Wrong data in row {row_num} - '{row}' \nSpecific error: {err}\nCorrect any issues and try again. File not imported"
            break
    if err_message:
        print(err_message)
        return None
    if not valid_rows:
        print("The file contains no activities. No data imported")
        return None
    activities.extend(valid_rows)
    print(f"File was successfully imported. {len(valid_rows)} records created ")


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
                print("You selected: Register activity")
                separator()
                act_title = ask_for_text("Please enter a title: ")
                act_category = ask_for_text("Please enter a category: ")
                act_date = ask_for_date("Enter a date for the activity: ")
                act_duration = ask_for_int("Please enter duration in mins: ")
                act_status = ask_for_status(
                    "Register status ('planned' or 'completed'): "
                )
                activities.append(
                    Activity(
                        act_title, act_category, act_date, act_duration, act_status
                    )
                )

            case "2":
                print("You selected: Show activities")
                separator()
                if not activities:
                    print("No activities found. Returning to menu")
                else:
                    for act in activities:
                        print(act)

            case "3":
                print("You selected: Search for activity or category")
                separator()
                if not activities:
                    print("No activities found. Returning to menu")
                else:
                    while True:
                        choice = ask_for_text(
                            "Enter 't' for title search, or 'c' for category search: "
                        ).lower()
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
                separator()
                if not activities:
                    print("No activities found. Returning to menu")
                else:
                    while True:
                        user_input = ask_for_text(
                            "Enter 'p' or 'c' to show planned or completed activities: "
                        ).lower()
                        if user_input not in ("p", "c"):
                            print("Wrong choice, try again")
                            continue
                        if user_input == "p":
                            criteria = "planned"
                        else:
                            criteria = "completed"
                        results = get_filtered_activities(
                            activities, "status", criteria
                        )
                        if not results:
                            print("No results found")
                            break
                        else:
                            for result in results:
                                print(result)
                            break

            case "5":
                print("You selected: Sort activities by date or duration")
                separator()
                if not activities:
                    print("No activities found. Returning to menu")
                else:
                    while True:
                        user_input = ask_for_text(
                            "Enter 'd' to sort by date, or 'm' to sort by duration: "
                        )
                        if user_input.lower() not in ("d", "m"):
                            print("Wrong choice, try again")
                            continue
                        if user_input.lower() == "d":
                            criteria = "date"
                        else:
                            criteria = "estimated_minutes"
                        sorted_activities = sort_activities(activities, criteria)
                        for act in sorted_activities:
                            print(act)
                        break

            case "6":
                print("You selected: Mark activity as completed")
                separator()
                if not activities:
                    print("No activities found. Returning to menu")
                else:
                    for act in activities:
                        print(act)
                    while True:
                        actid = ask_for_text(
                            "Which activity do you want to mark as completed (uuid) or 'r' to return: "
                        )
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
                print(
                    "You selected: Show no.of activities, total estimated time and no. of completed"
                )
                separator()
                if not activities:
                    print("No activities found. Returning to menu")
                else:
                    total_activities = len(activities)
                    hours_est, minutes_est = divmod(calc_total_est_time(activities), 60)
                    total_completed_activities = len(
                        get_filtered_activities(activities, "status", "completed")
                    )
                    separator()
                    print(
                        f"You have {total_activities} activites registered, of which {total_completed_activities} is 'completed'"
                    )
                    print(
                        f"Total estimated time: {hours_est} hours and {minutes_est} mins"
                    )

            case "8":
                print("You selected: Save activities to file")
                separator()
                if not activities:
                    print("No activities found. Returning to menu")
                else:
                    filename = "activities_export.csv"
                    try:
                        with open(filename, "w", encoding="utf-8") as csv_file:
                            header = [
                                "title",
                                "category",
                                "date",
                                "estimated_minutes",
                                "status",
                            ]
                            writer = csv.DictWriter(csv_file, fieldnames=header)

                            writer.writeheader()
                            writer.writerows(
                                {
                                    "title": activity.title,
                                    "category": activity.category,
                                    "date": activity.date,
                                    "estimated_minutes": activity.estimated_minutes,
                                    "status": activity.status.lower(),
                                }
                                for activity in activities
                            )
                        print(f"File {filename} was successfully written")
                    except PermissionError:
                        print(
                            f"Error: You do not have permission to write '{filename}'."
                        )
                    except OSError as e:
                        print(f"System error occurred: {e}")

            case "9":
                print("You selected: Read activites from file")
                separator()
                filename = ask_for_text(
                    "Please enter filename incl. extension (like example.csv): "
                )
                try:
                    with open(filename, "r", encoding="utf-8") as csv_file:
                        csv_importer = csv.DictReader(csv_file)
                        load_activities(csv_importer)
                except PermissionError:
                    print(f"Error: You do not have permission to read '{filename}'.")
                except FileNotFoundError:
                    print("Error: File not found. Try again")
                except OSError as e:
                    print(f"System error occurred: {e}")

            case "q":
                print("You selected: Quit program. Have a nice day")
                break

            case _:
                print(f"Incorrect alternative > {menu_input} <: Try again")


if __name__ == "__main__":
    main()
