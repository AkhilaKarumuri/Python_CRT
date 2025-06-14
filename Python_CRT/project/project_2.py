'''WAPP
1) To display a Menu of Food Items(List)
2) To create a tuple of Prices w.r.t Food Items List
3) Read the input from the user for ordering the food including quantity
    if exists in the menu----Confirm order
    if not print a message----
4) While billing , read phone.no, feedback, read tip amount
5) Add 18% gst to the bill & print the bill if bill>0'''

size=int(input("Enter the no.of.Food Items available: "))
food_items =[]
for i in range(size):
    temp=input("Enter the food item at" f" {i}th index :")
    food_items.append(temp)
print("Menu of the Food Items in our restaurant:",food_items)
order= input("Order Please:")
if order in food_items:
    print(f"{order} is available in the menu.")
    quantity = int(input(f"The quantity of {order} is: "))
    print(f"You have ordered {quantity}-{order}(s).")
else:
    print(f"Sorry your {order} is not available now order the other item")

List=['Chickenbiryani','WaterBottle','Sweetpan','Curdrice','cooldrink','Sparklingwater']
Tuple=('500','30','50','100','40','45')
for i in range():
    word=input("Enter the word:")
    index=List.index(word)
    print(f"{word}-{Tuple[index]}")
    

tip= int(input("Enter the tip amount: "))
bill= print("Your Total Bill is: "f"{quantity*int(Tuple[index]) + tip