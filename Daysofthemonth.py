days_in_month = {
    "january": 31,
    "february": 28,  
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}

month_input = input("Which month would you like to know about? ").strip().lower()

if month_input in days_in_month:
    print(f"{month_input.capitalize()} has {days_in_month[month_input]} days.")
else:
    print("Hmm, that doesn’t seem like a real month. Try again using a full month name (e.g., 'March').")