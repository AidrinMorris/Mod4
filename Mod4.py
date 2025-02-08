#Bank
balance = float(input("Please enter your bank balance: "))
print(balance < 100)

#Headlights
sensor_threshold = 7

if sensor_threshold < 8:
    print("Headlights On")
else:
    print("Headlights Off")

#Movies
age = int(input("Please enter your age: "))

if age < 13:
    print("You can see G rated movies.")
elif 13 <= age <= 17:
    print("You can see PG-13 rated movies.")
else:
    print("You can see R rated movies.")

#Store
order_total = float(input("Enter the order total: "))

if order_total < 50:
    shipping_cost = 5
else:
    shipping_cost = 0

total_cost = order_total + shipping_cost
print(f"The total cost, including shipping, is: ${total_cost:.2f}")

#TF
# Truth Table for the expression: (A AND B) OR (NOT B)
# A      B      (A AND B) OR (NOT B)
# True   True   True
# True   False  True
# False  True   False
# False  False  True

def truth_table():
    print("A\tB\t(A AND B) OR (NOT B)")
    for A in [True, False]:
        for B in [True, False]:
            result = (A and B) or (not B)
            print(f"{A}\t{B}\t{result}")

truth_table()
