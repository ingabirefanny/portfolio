def final_price(purchase_price,percentage_discount):
    if(purchase_price<=0):
     print(f'invalid purchase price')
    elif(purchase_price<=100):
     discount=purchase_price*(percentage_discount/100)
    elif(purchase_price<=500):
     discount=purchase_price*(percentage_discount/100) 
    elif(purchase_price<=1000): 
       discount=purchase_price*(percentage_discount/100) 
    else:
     discount=purchase_price*(percentage_discount/100)

     

     purchase_price = 100
     percentage_discount = 5
     final_price = purchase_price - discount
     print(final_price)
     
    
