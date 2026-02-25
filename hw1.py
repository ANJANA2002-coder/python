rice_price=45
sugar_price=40
oil_price=130
rice_weight=3
sugar_weight=2.5
oil_weight=1.8
totalrice_price=rice_price*rice_weight
totalsugar_price=sugar_price*sugar_weight
totaloil_price=oil_price*oil_weight
total_bill=totalrice_price+totalsugar_price+totaloil_price
print(total_bill)
total_bill_int=int(total_bill)
print(total_bill_int)
total_bill_str=str(total_bill_int)
import random
delivery_charge=random.randrange(5,10)
print("The delivery charge is: ", delivery_charge)
total_bill_with_delivery=total_bill_int+delivery_charge
print("The total bill with delivery charge is: ", total_bill_with_delivery)
                                
