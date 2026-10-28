import datetime

def get_days_from_today(target_date: str) -> int:
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
    try:
        format_target_date = datetime.datetime.strptime(target_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Please enter a valid date in YYYY-MM-DD format.")
    return (today - format_target_date).days

date_input = input("Enter a date in YYYY-MM-DD format: ")
days_difference = get_days_from_today(date_input)
print(f"The number of days from today to {date_input} is: {days_difference} days.")