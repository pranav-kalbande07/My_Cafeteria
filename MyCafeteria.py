print("\nWelcome to MyCafeteria, we will serve you the best we have!! \n")
print("Our Menue:-")

menu ={
  "Coffee":80,
  "Maggie":60,
  "Tea":  10,
  "Pizza":100,
  "Burger":50,
   "Pasta":60   
}

print("Coffee: Rs 80 \n Maggie: Rs 60 \n Tea: Rs 10 \n Pizza: Rs 100 \n Burger: Rs 50 \n Pasta: Rs 60")

order_total =0
item_1=input("Enter the name of item you want = ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item{item_1} is added to ordered list \n")
else:
    print(f"Your item{item_1} is not unavailable please order somethig else from our menu\n")
   
another_item = input("Do you want ot add any other item ? (Yes/No)")

if another_item == "Yes":
    item_2=input("Enter the name of second item =")
    
    if item_2 in menu:
     order_total+= menu[item_2]
     print(f"Your item{item_2} is added to ordered list \n")
    else:
        print(f"Your item{item_1} is not unavailable please order somethig else from our menu\n")
        
print(f"The total amount is {order_total} \n")
print("Thank You!!")