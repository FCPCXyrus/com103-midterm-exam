categories = [
    "Food and Drinks [e.g. Lunch, snacks, coffee]",
    "Transportation [e.g. Bus, jeepney, ride-share]",
    "Mobile/Internet [e.g. Load, data plan, WiFi top-up]",
    "School Supplies [e.g. Notebook, pen, bond paper]",
    "Entertainment [e.g. Games, movies, hangout]"
]

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

student_name = input("Student's Name: ")
weekly_budget = float(input("Weekly Budget: "))

print("==============================")
print(" WEEKLY EXPENSE -- CATEGORIES ")
print("==============================")

for lists in range(5):
    print(lists+1, "-", categories[lists])
print("==============================")

for lists in range(4):
    print(f"\nOrder {lists+1}")
    listsno = int(input("What Category? (1-5 or 0 to skip): "))
    
    if listsno == 0:
        continue
    
    if listsno < 1 or listsno > 5:
        print("Invalid category! Please choose 1-5")
        continue
    
    description = input("Description: ")
    amount = int(input("Amount: "))