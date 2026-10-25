import datetime

def get_days_from_today(target_date: datetime.date) -> int:
    """Return the number of days from today to the target date.

    A positive result means the target date is in the future.
    A negative result means the target date is in the past.
    Zero means the target date is today.

    Args:
        target_date: The date to compare with today's date.

    Returns:
        The signed difference between the target date and today, in days.
    """
    today = datetime.date.today()
    return (target_date - today).days

date_input = input("Enter a date in YYYY-MM-DD format: ")
try:
    date_object = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
except ValueError:
    print("Invalid date. Please enter a valid date in YYYY-MM-DD format.")
else:
    days_difference = get_days_from_today(date_object)
    print(f"The number of days from today to {date_object} is: {days_difference} days.")