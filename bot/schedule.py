import csv

app = input("This schedule is for which app (meet/zoom)?: ")

if app == "meet":
    with open('meet.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        choice = 'y'

        while choice == 'y':
            day = input("Enter day of meeting: ")
            time = input("Enter time of meeting: ")
            link = input("Enter link of meeting: ")
            writer.writerow([day, time, link])

            choice = input("Want to add more meetings ? (y/n)")

elif app=="zoom":
    with open('zoom.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        choice = 'y'

        while choice == 'y':
            day = input("Enter day of meeting: ")
            time = input("Enter time of meeting: ")
            mid = input("Enter zoom meeting ID: ")
            mpass = input("Enter meeting password: ")
            writer.writerow([day, time, mid, mpass])

            choice = input("Want to add more meetings ? (y/n)")
