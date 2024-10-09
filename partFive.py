def get_days_until_weekend(day):
    """Return the number of days until the weekend based on the input day."""
    countdown_to_weekend = {
        "monday": 5,
        "tuesday": 4,
        "wednesday": 3,
        "thursday": 2,
        "friday": 1,
        "saturday": 0,
        "sunday": 0
    }
    return countdown_to_weekend.get(day, None)  

def What_Is_the_Date():
    The_Day = input("Enter the day of the week: ").strip().lower()  
    
    
    capitalized_day = The_Day.capitalize()
    
    if The_Day == "saturday" or The_Day == "sunday":
        print("It's the weekend! ")
    elif The_Day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
        days_left = get_days_until_weekend(The_Day)
        print(f"It's a weekday. Keep pushing through, {capitalized_day} is a productive day!")
        print(f"There are {days_left} days left until the weekend!")
    else:
        print("Invalid day entered. Please try again.")

What_Is_the_Date()
