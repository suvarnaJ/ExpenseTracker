from .validation import validate_amount, validate_date
from .logger import log_info, log_error

FILE_NAME = "expenses.txt"


def load_expenses():
    expenses = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    data = line.split(",")

                    expense = {
                        "id": int(data[0]),
                        "date": data[1],
                        "category": data[2],
                        "description": data[3],
                        "amount": float(data[4])
                    }

                    expenses.append(expense)

        log_info("Expenses loaded successfully.")

    except FileNotFoundError:
        log_info("Expense file not found. Starting with empty list.")

    except (ValueError, IndexError) as e:
        log_error(f"Invalid expense file data: {e}")
        print("Error: Invalid data found in expense file.")

    except IOError as e:
        log_error(f"File reading error: {e}")
        print("Unable to read expense file.")

    return expenses


def save_expenses(expenses):

    try:
        with open(FILE_NAME, "w") as file:

            for expense in expenses:
                file.write(
                    f"{expense['id']},"
                    f"{expense['date']},"
                    f"{expense['category']},"
                    f"{expense['description']},"
                    f"{expense['amount']}\n"
                )

        log_info("Expenses saved successfully.")

    except IOError as e:
        log_error(f"Error saving expenses: {e}")
        print("Unable to save expenses.")


def generate_id(expenses):

    if not expenses:
        return 1

    return max(expense["id"] for expense in expenses) + 1


def add_expense(expenses):

    try:
        date = input("Enter date (YYYY-MM-DD): ")
        validate_date(date)

        category = input("Enter category: ")

        if not category.strip():
            raise ValueError("Category cannot be empty.")

        description = input("Enter description: ")

        if not description.strip():
            raise ValueError("Description cannot be empty.")

        amount = float(input("Enter amount: "))
        validate_amount(amount)

        expense = {
            "id": generate_id(expenses),
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)

        save_expenses(expenses)

        log_info(f"Expense added: {expense['id']}")

        print("Expense added successfully.")

    except ValueError as e:

        log_error(f"Add expense validation error: {e}")

        print("Invalid input:", e)

    except Exception as e:

        log_error(f"Unexpected add expense error: {e}")

        print("Something went wrong.")


def delete_expense(expenses):

    try:

        expense_id = int(input("Enter Expense ID to delete: "))

        expense = find_expense(expenses, expense_id)

        if expense is None:

            print("Expense not found.")

            log_error(
                f"Delete failed. Expense not found: {expense_id}"
            )

            return

        expenses.remove(expense)

        save_expenses(expenses)

        log_info(f"Expense deleted: {expense_id}")

        print("Expense deleted successfully.")

    except ValueError:

        print("Please enter a valid Expense ID.")

    except Exception as e:

        log_error(f"Delete expense error: {e}")

        print("Something went wrong.")


def update_expense(expenses):

    try:

        expense_id = int(
            input("Enter Expense ID to update: ")
        )

        expense = find_expense(expenses, expense_id)

        if expense is None:

            print("Expense not found.")

            return

        print("Enter new details:")

        date = input("Enter date (YYYY-MM-DD): ")
        validate_date(date)

        category = input("Enter category: ")
        description = input("Enter description: ")

        amount = float(input("Enter amount: "))
        validate_amount(amount)

        expense["date"] = date
        expense["category"] = category
        expense["description"] = description
        expense["amount"] = amount

        save_expenses(expenses)

        log_info(f"Expense updated: {expense_id}")

        print("Expense updated successfully.")

    except ValueError as e:

        log_error(f"Update validation error: {e}")

        print("Invalid input:", e)

    except Exception as e:

        log_error(f"Update expense error: {e}")

        print("Something went wrong.")


def find_expense(expenses, expense_id):

    for expense in expenses:

        if expense["id"] == expense_id:
            return expense

    return None


def display_all_expenses(expenses):

    if not expenses:

        print("No expenses available.")

        return

    print("\n========== ALL EXPENSES ==========")

    for expense in expenses:

        print(
            f"ID: {expense['id']} | "
            f"Date: {expense['date']} | "
            f"Category: {expense['category']} | "
            f"Description: {expense['description']} | "
            f"Amount: ₹{expense['amount']:.2f}"
        )

    log_info("Displayed all expenses.")