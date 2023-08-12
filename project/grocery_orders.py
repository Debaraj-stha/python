menu=[
{
    "title": "banana",
    "price": 100,
    "unit":"dozzen"
},
{
    "title": "apple",
    "price": 104,
    "unit":"kg"
},
{
    "title": "mutton",
    "price": 1000,
    "unit":"kg"
},
{
    "title": "bread",
    "price": 40,
    "unit":"packet"
},
{
    "title": "egg",
    "price": 10,
    "unit":"unit"
},
{
    "title": "daal",
    "price": 140,
    "unit":"kg"
},
{
    "title": "sugar",
    "price": 90,
    "unit":"kg"
},
{
    "title": "chicken",
    "price": 400,
    "unit":"kg"
},

]
orders=[]
def show_menu():
    print("Menu")
    print("================================")
    for items in menu:
        print(items['title'],":Rs",items["price"],"per",items["unit"])


def takeOrder():
    while True:
        found_item="none"
        user_input=input("Enter item name or  'no' for finishing your order ").lower()
        if(user_input=='no'):
            break
        for item in menu:
            if item['title'] in user_input:
                found_item=item['title']
                rate=item['price']
                unit=item['unit']
                break
        if(found_item=="none"):
            print("not found")
        else:
        
            quantity=int(input("enter item quantity::"))
            orders.append({"title":user_input,"quantity":quantity,"rate":rate,"unit":unit})
            print(f"{user_input} of quantity {quantity} is added to your order")

def show_bill():
    print("")
    print("")
    print("Item Bill")
    print("================================================")
    print("")
    total_cost=0
    for order in orders:
        cost=0
        cost=order['quantity']*order['rate']
        print(order['title'].capitalize(),"*",order['quantity'], order['unit'],"=",order['quantity']*order['rate'])
        total_cost+=cost
    print("================================================")
    print("")
    print("Total bill ammount = Rs",total_cost.__float__())
    discount=(total_cost*4)/100
    print(f"Discount={discount.__float__()}")
    print(f"Grand total={(total_cost-discount).__float__()}")
show_menu()
takeOrder()
show_bill()