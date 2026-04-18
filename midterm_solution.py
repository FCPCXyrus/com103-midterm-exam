categories = [
    ["Food and Drinks", "Lunch", "Snacks", "Coffee"],
    ["Transportation", "Bus", "Jeepney", "Ride-Share"],
    ["Mobile/Internet", "Load", "Data", "Wifi top-up"],
    ["School Supplies", "Notebook", "Pen", "Bond Paper"],
    ["Entertainment", "Games", "Movie", "Hangout"]]

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

student_name = input("Student's Name: ")
weekly_budget = float(input("Weekly Budget: "))

print("==============================")
print(" WEEKLY EXPENSE -- CATEGORIES ")
print("==============================")

for lists in range(5):
    print(lists+1, "-", categories[lists][0], ",", categories[lists][1], ",", categories[lists][2], ",", categories[lists][3])
print("==============================")

print("--- EXPENSE 1 ---")
category1 = float(input("Category(0 to skip): "))

print("--- EXPENSE 2 ---")
category1 = float(input("Category(0 to skip): "))

print("--- EXPENSE 3 ---")
category1 = float(input("Category(0 to skip): "))