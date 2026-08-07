from expense_tracker.expenses import (
    load_expenses,
    add_expense,
    delete_expense,
    update_expense,
    display_all_expenses
)

from expense_tracker.reports import (
    monthly_summary,
    category_summary,
    highest_expense,
    export_report
)

from expense_tracker.validation import (
    validate_month,
    validate_year
)

from expense_tracker.logger import (
    log_info,
    log_error
)


def display_menu():

    print("\n")
    print("======================================")
    print("       PERSONAL EXPENSE TRACKER")
    print("======================================")

    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. Update Expense")
    print("4. Display All Expenses")
    print("5. Monthly Summary")
    print("6. Category-wise Summary")
    print("7. Highest Expense")
    print("8. Export Monthly Report")
    print("9. Exit")


def get_choice():

    try:

        return int(
            input("Enter your choice: ")
        )

    except ValueError:

        print("Please enter a valid number.")

        return 0


def get_month_year():

    year = int(input("Enter year: "))
    validate_year(year)

    month = int(input("Enter month (1-12): "))
    validate_month(month)

    return year, month


def main():

    expenses = load_expenses()

    log_info("Expense Tracker application started.")

    while True:

        display_menu()

        choice = get_choice()

        try:

            if choice == 1:

                add_expense(expenses)

            elif choice == 2:

                delete_expense(expenses)

            elif choice == 3:

                update_expense(expenses)

            elif choice == 4:

                display_all_expenses(expenses)

            elif choice == 5:

                year, month = get_month_year()

                monthly_summary(
                    expenses,
                    year,
                    month
                )

            elif choice == 6:

                category_summary(expenses)

            elif choice == 7:

                highest_expense(expenses)

            elif choice == 8:

                year, month = get_month_year()

                export_report(
                    expenses,
                    year,
                    month
                )

            elif choice == 9:

                log_info(
                    "Expense Tracker application closed."
                )

                print(
                    "Thank you for using Expense Tracker!"
                )

                break

            else:

                print(
                    "Invalid choice. "
                    "Please select 1-9."
                )

        except ValueError as e:

            log_error(
                f"Validation error: {e}"
            )

            print("Invalid input:", e)

        except Exception as e:

            log_error(
                f"Unexpected application error: {e}"
            )

            print(
                "Something went wrong."
            )


if __name__ == "__main__":
    main()