
menu = {"shirts":700,"pants":600,"jeans":500,"tshirts":400,"shorts":300}

cart = {}
for x,y in menu.items():
    print(x," : Rs.",y)
while True :
    items = input("enter an item :")
    if items.lower()=="done":
        break
    if items not in menu:
        print("enter items from menu ... ")
    else :
        try :
            qty = int(input("enter the quantity : "))
            if qty <=0 :
                print("enter a valid quantity ...")
            if items in cart and qty > 0 :
                cart[items]+=qty
            elif items not in cart and qty > 0:
                cart[items]=qty
            print(qty ,". ",items," added to the cart")
        except ValueError :
            print("enter some valid quantity ...")
print("\n Final Bill ")
print(" ------------------------------------------------------------------- ")
print("{:<25}{:<20}{:<15}{:<10}".format("items","quantity","price","total"))
print(" ------------------------------------------------------------------- ")
g_total = 0
for items,qty in cart.items():
    price = menu[items]
    total = price*qty
    g_total += total
    print("{:<25}{:<20}{:<15}{:<10}".format(items,qty,price,total))
dis=0
if g_total>5000:
    dis = 0.1*g_total
g_total-=dis
print(" ------------------------------------------------------------------- ")
print("{:<60}".format("Discount : "),dis)
print("{:<60}".format("Grand Total : "),g_total)
    
            
                
        
