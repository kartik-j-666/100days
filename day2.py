print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip /100
bill_amount= bill * tip_percentage
total_amount = bill + bill_amount
split_by_people=(total_amount / people)
final_total = round(split_by_people,2)

print(f"final amount to pay :${final_total}")