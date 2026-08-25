# Script 2 : vérifier un stock de matériel

stock_tubes = 15
seuil_minimum = 10

print("Stock actuel de tubes :", stock_tubes)

if stock_tubes < seuil_minimum:
    print("ALERTE : il faut recommander des tubes !")
else:
    print("Stock suffisant, tout va bien.")
