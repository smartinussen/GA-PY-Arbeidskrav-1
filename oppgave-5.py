# Miniprosjekt: Aktivitetsplanlegger













def main() -> None:
    while True:
        print(10 * "-", "    MENU     ", 10 * "-")
        print("1. Register and show activities")
        print("2. Search for activity or category")
        print("3. Filter by status")
        print("4. Sort by date or duration")
        print("5. Mark activity as completed")
        print("6. Show no. of activities, total est. time and no. of completed")
        print("7. Save activities to file")
        print("8. Read activites from file")
        print("9. Quit program")
        print(10 * "-", " END OF MENU ", 10 * "-")
        #menu_input = ask_for_int("Chose an option, confirm with ENTER: ")
        menu_input = input("Please select an action (1-9): ")

        match menu_input:
            case "1":
                print("You selected: Register and show activities")
            case "2":
                print("You selected: Search for activity or category")
            case "3":
                print("You selected: Filter by status")
            case "4":
                print("You selected: Sort by date or duration")
            case "5":
                print("You selected: Mark activity as completed")
            case "6":
                print("You selected: Show no.of activities, total estimated time and no. of completed")
            case "7":
                print("You selected: Save activities to file")
            case "8":
                print("You selected: Read activites from file")
            case "9":
                print("You selected: Quit program")
                break
            case _:
                print(f"Incorrect alternative > {menu_input} <: Try again")

main()