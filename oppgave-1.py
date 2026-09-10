# Oppgave 1.1 - Beregn tidsbruk
def ask_for_int(prompt: str) -> int:
    """Ask until the user gives a valid input: int."""
    while True:
        user_input: str = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        print("Feil input: Kun heltall kan benyttes. Prøv igjen")


def calc_study_time(sessions: int, minutes_used: int) -> None:
    total_minutes_used = sessions * minutes_used
    # Tips om funksjon divmod fra Claude
    hours_spent, minutes_spent = divmod(total_minutes_used, 60)
    print(f"Antall studieøkter: {sessions}")
    print(f"Minutter pr. økt: {minutes_used}")
    print(f"Samlet tidsbruk: {hours_spent} time(r) og {minutes_spent} minutt(er)")


# Oppgave 1.2 - Analyser tekst
def ask_for_text(prompt: str) -> str:
    """Ask until the user gives a valid input: str."""
    while True:
        text_input = input(prompt)
        if text_input.strip() != "":
            return text_input
        print("Feil input: Skriv inn tekst for analyse")


def analyze_text(txt_for_analysis: str) -> None:
    chars_with_spaces = len(txt_for_analysis)
    chars_without_spaces = len(txt_for_analysis.replace(" ", ""))
    reversed_text = txt_for_analysis[::-1]
    contains_python = "python" in txt_for_analysis.lower()

    print(f"{'Antall tegn medregnet mellomrom:':<35} {chars_with_spaces}")
    print(f"{'Antall tegn uten mellomrom:':<35} {chars_without_spaces}")
    print(f"{'Reversert utgave av tekst:':<35} {reversed_text}")
    print(f"{'Inneholder "Python":':<35} {'Ja' if contains_python else 'Nei'}")


# Oppgave 1.3
def get_interval() -> tuple[int, int]:
    while True:
        start = ask_for_int("Tast inn startpunkt (heltall): ")
        stop = ask_for_int("Tast inn sluttpunkt (heltall): ")
        if stop > start:
            return start, stop
        print("Sluttpunkt kan ikke være mindre enn startpunkt")


def show_divisible(start: int, stop: int, divisor: int) -> None:
    for num in range(start, stop + 1):
        if num % divisor == 0:
            print(f"{num}", end=" ")
    print()


def analyze_interval(start: int, stop: int) -> None:
    print(f"{'Partall i intervall:':<30}", end=" ")
    show_divisible(start, stop, 2)
    print(f"{'Intervalltall delelig med 3:':<30}", end=" ")
    show_divisible(start, stop, 3)

    interval_sum = sum(range(start, stop + 1))
    print(f"{'Intervalltall summert:':<30} {interval_sum}")


def main() -> None:
    while True:
        print("1. Beregn tidsbruk")
        print("2. Analyser tekst")
        print("3. Analyser tallintervall")
        print("4. Avslutt")
        user_input = ask_for_int("Tast inn ditt menyvalg og bekreft med ENTER: ")
        if user_input == 1:
            sessions = ask_for_int("Legg inn antall studieøkter: ")
            minutes_used = ask_for_int("Antall minutter pr. økt: ")
            calc_study_time(sessions, minutes_used)
        elif user_input == 2:
            text_input = ask_for_text("Skriv inn tekst for analyse: ")
            analyze_text(text_input)
        elif user_input == 3:
            start_int, stop_int = get_interval()
            analyze_interval(start_int, stop_int)
        elif user_input == 4:
            break
        else:
            print("Du har tastet et ugyldig valg, prøv igjen")


if __name__ == "__main__":
    main()
