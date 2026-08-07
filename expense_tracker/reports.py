from .logger import log_info, log_error


def monthly_summary(expenses, year, month):

    total = 0
    count = 0

    for expense in expenses:

        date = expense["date"]

        expense_year = int(date[:4])
        expense_month = int(date[5:7])

        if expense_year == year and expense_month == month:

            total += expense["amount"]
            count += 1

    print("\n========== MONTHLY SUMMARY ==========")

    print(f"Year  : {year}")
    print(f"Month : {month}")
    print(f"Number of Expenses : {count}")
    print(f"Total Expense     : ₹{total:.2f}")

    log_info(
        f"Monthly summary generated for {year}-{month}"
    )


def category_summary(expenses):

    categories = {}

    for expense in expenses:

        category = expense["category"]

        if category not in categories:
            categories[category] = 0

        categories[category] += expense["amount"]

    print("\n========== CATEGORY SUMMARY ==========")

    if not categories:

        print("No expenses available.")

        return

    for category, amount in categories.items():

        print(
            f"{category:<20} ₹{amount:.2f}"
        )

    log_info("Category-wise summary generated.")


def highest_expense(expenses):

    if not expenses:

        print("No expenses available.")

        return

    highest = max(
        expenses,
        key=lambda expense: expense["amount"]
    )

    print("\n========== HIGHEST EXPENSE ==========")

    print(
        f"ID          : {highest['id']}\n"
        f"Date        : {highest['date']}\n"
        f"Category    : {highest['category']}\n"
        f"Description : {highest['description']}\n"
        f"Amount      : ₹{highest['amount']:.2f}"
    )

    log_info("Highest expense calculated.")


def export_report(expenses, year, month):

    file_name = f"expense_report_{year}_{month:02d}.txt"

    try:

        monthly_expenses = []

        for expense in expenses:

            expense_year = int(expense["date"][:4])
            expense_month = int(expense["date"][5:7])

            if (
                expense_year == year
                and expense_month == month
            ):

                monthly_expenses.append(expense)

        total = sum(
            expense["amount"]
            for expense in monthly_expenses
        )

        with open(file_name, "w") as file:

            file.write(
                "====================================\n"
            )

            file.write(
                "       MONTHLY EXPENSE REPORT\n"
            )

            file.write(
                "====================================\n\n"
            )

            file.write(
                f"Year  : {year}\n"
            )

            file.write(
                f"Month : {month}\n\n"
            )

            file.write(
                "------------------------------------\n"
            )

            for expense in monthly_expenses:

                file.write(
                    f"ID: {expense['id']} | "
                    f"Date: {expense['date']} | "
                    f"Category: {expense['category']} | "
                    f"{expense['description']} | "
                    f"₹{expense['amount']:.2f}\n"
                )

            file.write(
                "\n------------------------------------\n"
            )

            file.write(
                f"TOTAL EXPENSE: ₹{total:.2f}\n"
            )

            file.write(
                "------------------------------------\n"
            )

        print(
            f"Report exported successfully: {file_name}"
        )

        log_info(
            f"Monthly report exported: {file_name}"
        )

    except IOError as e:

        log_error(f"Report export error: {e}")

        print("Unable to export report.")