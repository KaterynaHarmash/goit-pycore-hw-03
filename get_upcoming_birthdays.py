from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    """
    Find users whose birthdays fall within the next 7 days,
    including today. If a birthday falls on a weekend,
    move the congratulation date to the following Monday.

    Args:
        users (list): A list of dictionaries containing 'name' and 'birthday'.

    Returns:
        list: A list of dictionaries containing 'name' and 'congratulation_date'.
    """
    today = datetime.today().date()
    end_of_week = today + timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        birthday_date = datetime.strptime(
            user["birthday"], "%Y.%m.%d"
        ).date()

        birthday_this_year = birthday_date.replace(year=today.year)

        # If the birthday has already passed, consider next year
        if birthday_this_year < today:
            birthday_this_year = birthday_date.replace(year=today.year + 1)

        # Check whether the birthday falls within the next 7 days
        if today <= birthday_this_year <= end_of_week:
            congratulation_date = birthday_this_year

            # Move weekend birthdays to the following Monday
            if birthday_this_year.weekday() == 5:  # Saturday
                congratulation_date += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  # Sunday
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.09.29"},
    {"name": "Jane Smith", "birthday": "1990.10.25"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)