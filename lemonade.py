def lemonade(customers):
    myBills = []
    while len(customers) > 0:
        customer = customers.pop(0)

        if customer == 5:
            myBills.append(customer)
        elif customer == 10:
            change = False

            if myBills.count(5) > 0:
                myBills.remove(5)
                myBills.append(10)
                change = True
            
            if change == False:
                return False  
        elif customer == 20:
            change = False
            
            if myBills.count(10) > 0:
                if myBills.count(5) > 0:
                    myBills.remove(5)
                    myBills.remove(10)
                    myBills.append(20)
                    change = True
                    
            if change == False:
                if myBills.count(5) >= 3:
                    found5 = 0
                    while found5 <= 3:
                        myBills.remove(5)
                        found5 += 1
                    change = True
                    myBills.append(20)
            
            if change == False:
                return False
    
    return True

print("output =", lemonade([5, 5, 5, 10, 20]))        
print("output =", lemonade([5, 5, 10, 10, 20]))
print("output =", lemonade([10, 10]))
print("output =", lemonade([5, 5, 10]))
