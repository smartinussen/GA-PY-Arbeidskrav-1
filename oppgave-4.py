# Oppgavce 4 - Filer, feilhåndtering og feilsøking
import csv

type Case = dict[str, str | int]


# Helper functions
def count_pr_category(datalist: list[Case]) -> dict[str, int]:
    cat_count = {}
    for row in datalist:
        if row["category"] not in cat_count:
            cat_count[row["category"]] = 1
        else:
            cat_count[row["category"]] += 1
    return cat_count


def get_call_status(cases: list[Case], state: str) -> list[Case]:
    status = []
    for row in cases:
        if row["is_resolved"] == state:
            status.append(row)
    return status


def calc_total_avg_time(valid_calls: list[Case]) -> tuple[int, float]:
    total_time_used = sum(call["minutes"] for call in valid_calls)
    avg_time_call = total_time_used / len(valid_calls)
    return total_time_used, avg_time_call


def sort_case_by_duration(case: list[Case]) -> list[Case]:
    return sorted(case, key=lambda s: s["minutes"], reverse=True)


def most_popular_category(categories: dict[str, int]) -> str:
    cat = ""
    calls = 0
    for key, value in categories.items():
        if value > calls:
            calls = value
            cat = key
    return cat
    # return max(categories, key=lambda x: categories[x])


def load_cases() -> list[Case] | None:
    filename = "supporthenvendelser.csv"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            validated_cases = []
            for row_num, row in enumerate(reader, start=2):
                row_is_valid = True
                for column, value in row.items():
                    if value is None or str(value).strip() == "":
                        print(
                            f"Missing value in row {row_num} - column: '{column}'. Row skipped"
                        )
                        row_is_valid = False
                        break
                if not row_is_valid:
                    continue
                try:
                    id_no = int(row["id"])
                    row["id"] = id_no
                    if id_no < 1:
                        print(
                            f"Invalid value in row {row_num} - 'id' = {row['id']} - Must be 1 or higher. Row skipped"
                        )
                        continue
                except ValueError:
                    print(
                        f"Invalid value in row {row_num} - 'id' = {row['id']} - Must be a positive integer. Row skipped"
                    )
                    continue
                try:
                    mins = int(row["minutes"])
                    row["minutes"] = mins
                    if mins < 0:
                        print(
                            f"Invalid value in row {row_num} - 'minutes' = {row['minutes']} - Must be 0 or more. Row skipped"
                        )
                        continue
                except ValueError:
                    print(
                        f"Invalid value in row {row_num} - 'minutes' = {row['minutes']} - Must be a positive integer. Row skipped"
                    )
                    continue
                if row["is_resolved"] not in ("yes", "no"):
                    print(
                        f"Invalid value in row {row_num} - 'is_resolved' = {row['is_resolved']} - Must be 'yes' or 'no'. Row skipped"
                    )
                    continue
                validated_cases.append(row)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
        return None
    except OSError as e:
        print(f"System error occurred: {e}")
        return None
    return validated_cases


def write_report(validated_cases: list[Case] | None) -> None:
    if not validated_cases:
        print("Nothing to write. List empty")
        return
    with open("support-rapport.txt", "w", encoding="utf-8") as report:
        # 1.1
        report.write("### Antall support henvedelser totalt ###\n")
        report.write(f"Vi har mottatt totalt {len(validated_cases)} henvendelser\n")

        # 1.2
        report.write("### Antall henvendelser pr. kategori ###\n")
        for key, value in count_pr_category(validated_cases).items():
            report.write(f"Kategori {key.capitalize()} har {value} henvendelser\n")

        # 2
        report.write("### Total tid brukt og gjennomsnitt pr henvendelse ###\n")
        total_mins, avg_mins_pr_call = calc_total_avg_time(validated_cases)
        hours_spent, minutes_spent = divmod(total_mins, 60)

        report.write(
            f"Total tid brukt: {hours_spent} timer, og {minutes_spent} minutter\n"
        )
        report.write(
            f"Gj.snitt tidsbruk pr henvendelse: {avg_mins_pr_call:.1f} minutter\n"
        )

        # 3
        report.write("### Antall henvendelser etter status ###\n")
        unresolved_calls = len(get_call_status(validated_cases, "no"))
        resolved_calls = len(get_call_status(validated_cases, "yes"))
        report.write(
            f"Det er totalt {unresolved_calls} uløste- og {resolved_calls} løste saker\n"
        )

        # 4
        report.write("### Kategori med flest henvendelser ###\n")
        report.write(
            f"Kategorien {most_popular_category(count_pr_category(validated_cases)).capitalize()} har flest henvendelser\n"
        )

        # 5
        report.write("### Uløste henvendelser sortert synkende ###\n")
        sorted_unresolved = get_call_status(
            sort_case_by_duration(validated_cases), "no"
        )
        for row in sorted_unresolved:
            report.write(
                f"Id {row['id']} er uløst med {row['minutes']} minutter brukt.\n"
            )


if __name__ == "__main__":
    write_report(load_cases())
