


Samsung_TV = {
    "name": "Samsung 55\" 4K UHD TV",
    "price": 429.99,
    "department": "Televisions",
    "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
}
LGTV = {
    'name': "LG 65\" OLED TV",
    "price": 996.99,
    "department": 'Televisions',
    'description': 'Its a tv bro'
}
Sony_Headphones = {
    "name": "Sony Noise-Canceling headphones",
    "price": 119.99,
    "department": "Headphones",
    "description": "its headphones I dont know what u want."
}

products = {
    'samsung tv' : Samsung_TV,
    'sony headphones': Sony_Headphones,
    'lg tv': LGTV
}
cart = []
total = 0
listy = {'name','price', 'department', 'description'}

I = 5
while I == 5:
    item = input('what item would you like to browse? [samsung tv, sony headphones, lg tv, cart] ')
    if item in products:
        info = input('what would you like to know? [price, department, description] ')
        print (products[item]['name'],'-', products[item][info])
        imfo = input('Is there anything else you would like to know? ')
        if imfo in listy:
            print (products[item]['name'],'-', products[item][imfo])
        purchase = input('would you like to purchase this item? ')
        if purchase == 'yes':
            cart.append(item)
            Total = total + (products[item]['price'])
            print ('item added to cart')
        
    elif item == 'cart':
        print (cart)
        pay = input ('Continue to checkout? ')

        if pay == 'yes':
            print ('your total is', Total)
            final = input ('Complete transaction? ')
            if final == 'yes':
                print('purchase complete.')
                cart.clear()
        
    else: print('product not found, please retry')

