Customers = {'Chansa':200,
             'Chan': 700,
             'Nosiku': 7000,
             'Walter':11000}

#platinum = (5000,10000)
#Gold = (1000,4999)
#Silver = (0,999)
#
#
#
#for name, points in platinum:
#    c = 0
#    if points >= 0 and points <= 1000:
#        return
#        c+=1
#return c
#
#def count(list1, l, r): 
#    c = 0 
#    # traverse in the list1 
#    for x in list1: 
#        # condition check 
#        if x>= l and x<= r: 
#            c+= 1 
#    return c 
#      
## driver code 
#list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70] 
#l = 40
#r = 80 
#print count(list1) 

def platinum():
    platinum = []
    gold = []
    silver = []
    points = range(0,10000)
    for i in points:
      if i >= 5000 and i<= 10000: 
        i == platinum.append
      elif i >= 1000 and i<= 4999: 
        i == gold.append
      elif i >= 0 and i<= 999: 
        i == silver.append

platinum()
print()
    
        