resources={
    "water": 500,
    "milk": 200,
    "coffee": 100,
}
menu={
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24
        },
        "cost":150
    },
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":100
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24
        },
        "cost":100
    },
}
def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item]>resources[item]:
            print(f"Not enough {item}")
            return False
        else:
            return True
def process_coins():
    total=0
    print("Please enter 5,10 and 20 rupees coins")
    five=int(input("Enter 5 rupees coins"))
    ten = int(input("Enter 10 rupees coins"))
    twenty =int(input("Enter 20 rupees coins"))
    total= five*5+ten*10+twenty*20
    return total
def payment(total,cost):
    if total>=cost:
        global profit
        profit = profit + cost
        change=total-cost
        print(f"The rest of your money{change}")
        return True
    else:
        print(f"actaul cost is{cost}")
        print((f"Here is your money{total}"))
        return False
def make_coffee(coffee,ingredients):
    for item in ingredients:
        resources[item]-=ingredients[item]
    print(f"Here is your {coffee}")

profit=0
machine=True
while machine:
    ch=input("What would you like? (espresso/latte/cappuccino):")
    ch=ch.lower()
    if ch=="off":
        machine=False
        break
    elif ch=="report":
        print((f"Water={resources['water']}"))
        print((f"Milk={resources['milk']}"))
        print((f"Coffee={resources['coffee']}"))
        print(f"Money={profit}")
    else:
        coffee_ty=menu[ch]
        print(coffee_ty)
        if check_resources(coffee_ty['ingredients']):
            total=process_coins()
            if payment(int(total),int(coffee_ty['cost'])):
                make_coffee(ch,coffee_ty['ingredients'])


