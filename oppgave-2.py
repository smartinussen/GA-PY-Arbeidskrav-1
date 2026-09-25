# Oppgave 2 – Datastrukturer og behandling av data

# Generics
type Session = dict[str, str | int]

study_sessions: list[Session] = [
    {"topic": "python", "duration_minutes": 45, "status": "completed"},
    {"topic": "mysql", "duration_minutes": 90, "status": "completed"},
    {"topic": "design", "duration_minutes": 60, "status": "planned"},
    {"topic": "bootdev", "duration_minutes": 45, "status": "completed"},
    {"topic": "python", "duration_minutes": 45, "status": "planned"},
]


def separator() -> None:
    print(30 * "-")


def show_sessions(sessions: list[Session]) -> None:
    if sessions:
        for i, session in enumerate(sessions, start=1):
            print(f"{'Result:':<10} {i}")
            print(f"{'Subject:':<10} {session['topic']}")
            print(f"{'Duration:':<10} {session['duration_minutes']} minutes")
            print(f"{'Status:':<10} {session['status']}")
            separator()
    else:
        print("No records")


def ask_for_text(prompt: str) -> str:
    """Ask until the user gives a valid input: str."""
    while True:
        text_input: str = input(prompt)
        if text_input.strip() != "":
            return text_input.strip()
        print("Wrong or missing input. Try again")


def ask_for_int(prompt: str) -> int:
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


def ask_for_status(prompt: str) -> str:
    """Ask until the user gives a valid input: str."""
    while True:
        text_input: str = input(prompt)
        if (
            text_input.lower().strip() == "planned"
            or text_input.lower().strip() == "completed"
        ):
            return text_input.strip()
        print("Wrong/missing input. Only 'planned' or 'completed' is accepted")


# Menu 3 - Filter for completed sessions
def get_completed_sessions(sessions: list[Session]) -> list[Session]:
    completed = []
    for session in sessions:
        if session["status"] == "completed":
            completed.append(session)
    return completed


# Menu 4 - Search in sessions by criteria
def search_in_sessions(criteria: str, sessions: list[Session]) -> list[Session]:
    search_results = []
    for session in sessions:
        if criteria.lower() in session["topic"].lower():
            search_results.append(session)
    return search_results


# Menu 5 - Show a sorted list of sessions by longest to shortest
def sort_sessions_by_duration(sessions: list[Session]) -> list[Session]:
    return sorted(sessions, key=lambda s: s["duration_minutes"], reverse=True)


# Menu 6 - Calculate total and avg time
def calc_total_avg_time(sessions: list[Session]) -> tuple[int, float]:
    total_time_used = sum(session["duration_minutes"] for session in sessions)
    avg_time_session = total_time_used / len(sessions)
    return total_time_used, avg_time_session


def show_time_summary(total: int, avg: float) -> None:
    print(f"Total time spent studying: {total}")
    print(f"Avg time pr session: {avg:.1f}")


def main() -> None:
    while True:
        print("1. Register a study session")
        print("2. Show all study sessions")
        print("3. Show completed study sessions")
        print("4. Search for subject in study sessions")
        print("5. Show study sessions by duration")
        print("6. Show accumulated and avg time spent studying")
        print("7. Quit program")

        user_input = ask_for_int("Chose an option, confirm with ENTER: ")
        if user_input == 1:
            print("Register a new study session")
            separator()
            topic = ask_for_text("Please enter subject: ")
            duration = ask_for_int("Please enter duration in mins: ")
            status = ask_for_status("Register status (planned or completed): ")
            study_sessions.append(
                {"topic": topic, "duration_minutes": duration, "status": status}
            )
        elif user_input == 2:
            show_sessions(study_sessions)
        elif user_input == 3:
            show_sessions(get_completed_sessions(study_sessions))
        elif user_input == 4:
            criteria = ask_for_text("Search criteria: ")
            show_sessions(search_in_sessions(criteria, study_sessions))
        elif user_input == 5:
            show_sessions(sort_sessions_by_duration(study_sessions))
        elif user_input == 6:
            completed = get_completed_sessions(study_sessions)
            if completed:
                total, avg = calc_total_avg_time(completed)
                show_time_summary(total, avg)
            else:
                print("No completed sessions")
        elif user_input == 7:
            break
        else:
            print("Wrong alternative, try again")


# Runtests
if __name__ == "__main__":
    main()
