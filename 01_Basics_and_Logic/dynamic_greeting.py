import time

def get_greeting():
    """
    Determines the greeting based on the current system time.
    """
    # Get the current hour (0-23) as an integer
    current_hour = int(time.strftime('%H'))

    # Python supports chained comparison operators for cleaner logic
    if 5 <= current_hour < 12:
        return "Good Morning!!"
    elif 12 <= current_hour < 17:
        return "Good Afternoon!!"
    elif 17 <= current_hour < 20:
        return "Good Evening!!"
    else:
        return "Good Night!!"

# Driver Code
if __name__ == "__main__":
    print(get_greeting())
