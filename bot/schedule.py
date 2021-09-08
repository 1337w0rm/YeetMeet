import csv

app = input("This schedule is for which app (meet/zoom)?: ")

if app == "meet":
    with open('meet.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        choice = 'y'

        while choice == 'y':
            name = input("Enter name of meeting/class: ")
            day = input("Enter day of meeting (Monday/Tuesday,etc): ")
            time = input("Enter time of meeting (24 hour format): ")
            link = input("Enter link of meeting: ")
            writer.writerow([name, day, time, link])

            choice = input("Want to add more meetings ? (y/n)")

elif app=="zoom":
    with open('zoom.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        choice = 'y'

        while choice == 'y':
            name = input("Enter name of meeting/class: ")
            day = input("Enter day of meeting (Monday/Tuesday,etc): ")
            time = input("Enter time of meeting(24 hour format): ")
            mid = input("Enter zoom meeting ID: ")
            mpass = input("Enter meeting password: ")
            writer.writerow([name, day, time, mid.replace(" ", ""), mpass])

            choice = input("Want to add more meetings ? (y/n)")
