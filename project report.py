import csv
import os

FILENAME = "vehicle_service_history.csv"

def load_from_file():
    records = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                records.append(row)
    return records


def save_to_file(records):
    with open(FILENAME, "w", newline="") as file:
        fieldnames = ["Vehicle Number", "Service Date", "Service Type", "Service Cost", "Remarks"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def add_record(records):
    print("--- Add New Service Record ---")
    vnum = input("Enter Vehicle Number: ")
    date = input("Enter Service Date (DD-MM-YYYY): ")
    stype = input("Enter Service Type: ")
    cost = input("Enter Service Cost: ")
    remarks = input("Enter Remarks: ")

    record = {
        "Vehicle Number": vnum,
        "Service Date": date,
        "Service Type": stype,
        "Service Cost": cost,
        "Remarks": remarks
    }
    records.append(record)
    save_to_file(records)
    print("Record added successfully!")


def view_all_records(records):
    print("--- All Vehicle Service Records ---")
    if not records:
        print("No records found.\n")
        return

    for r in records:
        print(r)
    print()


def search_record(records):
    print("--- Search Service History ---")
    vnum = input("Enter Vehicle Number to Search: ")

    found = False
    for r in records:
        if r["Vehicle Number"] == vnum:
            print(r)
            found = True

    if not found:
        print("No matching record found.")
    print()


def main():
    records = load_from_file()

    while True:
        print("=== Vehicle Service History Management ===")
        print("1. Add Service Record")
        print("2. View All Records")
        print("3. Search Record")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_record(records)
        elif choice == "2":
            view_all_records(records)
        elif choice == "3":
            search_record(records)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again")


main()
