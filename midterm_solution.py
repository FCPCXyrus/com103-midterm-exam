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


expenses_data = []

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
    
    expenses_data.append([listsno, description, amount])


print("=" * 70)
print(f"  {student_name.upper()} -- WEEKLY EXPENSE LOG")
print("=" * 70)
print(f"  Weekly Budget  : P{weekly_budget:.2f}")

total = 0
for expense in expenses_data:
    cat_num = expense[0]
    desc = expense[1]
    amt = expense[2]
    total += amt
    print(f"  [{cat_num}] {categories[cat_num-1].split('[')[0].strip()}")
    print(f"      {desc:<30} P{amt:.2f}")

remaining = weekly_budget - total
print("-" * 70)
print(f"  Total Spent    : P{total:.2f}")
print(f"  Remaining      : P{remaining:.2f}")
print(f"  Status         : Budget OK! Keep it up.")
print("=" * 70)
