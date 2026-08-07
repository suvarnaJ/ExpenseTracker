from datetime import datetime


def validate_amount(amount):

    if amount <= 0:
        raise ValueError(
            "Expense amount must be greater than zero."
        )

    return True


def validate_date(date):

    try:

        datetime.strptime(date, "%Y-%m-%d")

        return True

    except ValueError:

        raise ValueError(
            "Date must be in YYYY-MM-DD format."
        )


def validate_month(month):

    try:

        month_number = int(month)

        if month_number < 1 or month_number > 12:

            raise ValueError(
                "Month must be between 1 and 12."
            )

        return True

    except ValueError:

        raise ValueError(
            "Please enter a valid month."
        )


def validate_year(year):

    try:

        year_number = int(year)

        if year_number < 2000:

            raise ValueError(
                "Please enter a valid year."
            )

        return True

    except ValueError:

        raise ValueError(
            "Please enter a valid year."
        )
    