# Miniprosjekt: Aktivitetsplanlegger
from datetime import date as dateclass, datetime, time, timedelta

activities: list[object] = []

class Activity:
    def __init__(self, title: str, category: str, date: dateclass, estimated_minutes: int, status: str):
        self.title = title
        self.category = category
        self.date = date
        self.estimated_minutes = estimated_minutes
        self.status = status


def main() -> None:
    while True:
        print(10 * "-", "    MENU     ", 10 * "-")
        print("1. Register and show activities")
        print("2. Show activities")
        print("3. Search for activity or category")
        print("4. Filter by status")
        print("5. Sort by date or duration")
        print("6. Mark activity as completed")
        print("7. Show no. of activities, total est. time and no. of completed")
        print("8. Save activities to file")
        print("9. Read activites from file")
        print("Q. Quit program")
        print(10 * "-", " END OF MENU ", 10 * "-")
        menu_input = input("Please select an action (1-9 or `Q`): ").lower()

        match menu_input:
            case "1":
                print("You selected: Register activities")
            case "2":
                print("You selected: Show activities")
            case "3":
                print("You selected: Search for activity or category")
            case "4":
                print("You selected: Filter by status")
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
    main()
