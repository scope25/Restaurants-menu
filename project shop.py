menu = {
    'Pizza':100,
    'Burger':110,
    'Pasta':90,
    'French Fries':106,
    'Chilli Cheese Toast':115,
    'Chilli Cheese Gralic Toast':115,
    'Garlic Bread':98,
    'Garlic Bread with Cheese':119,	 
    'Plain Sandwich':175,
    'Grilled Sandwich':175,
    'Club Sandwich':175,
    'Tandoori Paneer Tikka':220,
    'Malai Paneer Tikka':220,
    'Soya Tandoori Tikka':175,
    'Tandoori Aloo':179,
    'Punjabi Soya Chap':179,
    'Hare-Bhare Kabab':162,
    'Dahi ke Kabab':179,
    'Tawa Parantha':53,
    'Laccha Parantha':53,
    'Pudina Parantha':53,
    'Stuffed Kulcha (Aloo)':65,
    'Stuffed Kulcha (Paneer)':65,
    'Papad':15,
    'Dal Makhani':192,
    'Yellow Dal':141,
    'Rajma':141,
    'Chole':141,
    'Steam Rice':161,
    'Soya Dum Biryani':220,
    'Veg. Pulao':161,
    'Mix Veg. Pulao':161,
    'Jeera Pulao':161,
    'Matka Biryani With Raita':220,
    'Hyderabadi Biryani':220,
    'Tandoori Roti':30,
    'Roomali Roti':17,
    'Red Sea':150,
    'Virgin Colada':150,
    'Love Valley':150,
    'Pomi Twist':150,
    'Blue Lagoon':150,
    'Vanilla/Strawberry':51,
    'Tutti Fruti':60,
    'Chocolate':60,
    'Butter Scotch':60,
    'Kaju Kishmish':60,
    'Vanilla Chocochips':60,
    'Mango':60
}

print("Welcome to TASTKING Restaurant")
print("Pizza: Rs100\nFrench Fries: Rs106\nBurger: Rs110\nPasta: Rs90\nChilli Chees Toast: Rs115\nChilli Cheese Gralic Toast: Rs98\nGarlic Bread with Cheese: Rs119\nPlain Sandwich: Rs175\nGrilled Sandwitch: Rs175\nClub Sandwich: Rs175\nTandoori Paneer Tikka: Rs179\nMalai Paneer Tikka: Rs220\nSoya Tandoori Tikka: Rs175\nTandoori Aloo: Rs179\nPunjabi Soya Chap: Rs179\nHare Bhare Kabab: Rs162\nDahi ke kabab: Rs179\nTawa Parantha: Rs53\nLaccha Parantha: Rs53\nPudina Paranth: Rs53\nStuffed Kulcha (Aloo): Rs65\nStuffed Kulcha (Paneer): Rs65\nPapad: Rs15\nDal Makhani: Rs192\nYellow Dal: Rs141\nRajma: Rs141\nChole: Rs141\nSteam Rice: Rs161\nSoya Dum Biryani: Rs220\nVeg. Pulao: Rs161\nMix Veg. Pulao: Rs161\nJeera Pulao: Rs161\nMatka Biryani With Raita: Rs220\nHyderabandi Biryani: Rs220\nTandoori Roti: RS220\nRoomali Roti: Rs17\nTutti Fruti: Rs60\nButter Scotch: Rs60\nKaju Kishmish: Rs60\nVanilla Chocochips: Rs60\nMango: Rs60\n")

order_total = 0

item_1 = input("Enter the name of item you want to other =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print("Orderd item {item_2} is not avaialable yet")

    another_order = input("Do you want to add another item? (Yes/No)")
    if another_order =="Yes":
       item_2 = input("Enter the name of second item = ")
       if item_2 in menu:
           order_total += menu[item_2]
           print(f"Item {item_2} has been added to order")
    else:
           print(f"Ordered item {item_2} is not avaialable!")
    print(f"The total amount of items to pay is {order_total}")