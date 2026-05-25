def main():
    time_str = input("What time is it? ")

    # Convert time to hours and minutes
    try:
        hours, minutes = map(int, time_str.strip().split(":"))
        total_minutes = hours * 60 + minutes
    except ValueError:
        return  # Invalid format, do nothing

    # Define meal times in minutes since midnight
    breakfast_start = 7 * 60
    breakfast_end = 8 * 60
    lunch_start = 12 * 60
    lunch_end = 13 * 60
    dinner_start = 18 * 60
    dinner_end = 19 * 60

    # Determine meal time
    if breakfast_start <= total_minutes <= breakfast_end:
        print("breakfast time")
    elif lunch_start <= total_minutes <= lunch_end:
        print("lunch time")
    elif dinner_start <= total_minutes <= dinner_end:
        print("dinner time")

if __name__ == "__main__":
    main()