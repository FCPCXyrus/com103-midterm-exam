Food_and_Drinks = ["Lunch", "Snacks", "Coffee"]
Transportation = ["Bus", "Jeepney", "Ride-Share"]
Mobile_Internet = ["Load", "Data", "Wifi top-up"]
School_Supplies = ["Notebook", "Pen", "Bond Paper"]
Entertainment = ["Games", "Movie", "Hangout"]

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

student_name = input("Student's Name: ")
weekly_budget = float(input("Weekly Budget: "))

print("==============================")
print(" WEEKLY EXPENSE -- CATEGORIES ")
print("==============================")
print("1. Food and Drinks [e.g. Lunch, Snacks, Coffee]")
print("2. Transportation [e.g. Bus, Jeepney, Ride-Share]")
print("3. Mobile / Internet [e.g. Load, Data plan, WiFi top-up]")
print("4. School Supplies [e.g. Notebook, Pen, Bond Paper]")
print("5. Entertainment [e.g. Games, Movie, Hangout]")
print("==============================")

print("--- EXPENSE 1 ---")
category1 = float(input("Category(0 to skip): "))