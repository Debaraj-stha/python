myDist={"A": 1, "B": 2, "C": 3}
print(myDist.keys())
print(myDist)
print(myDist.values())
print(myDist.pop('A'))
x=myDist.popitem()#remove last element from dict    
print(x)
print(myDist)
myDist.update({"A": 10})
print(myDist)
print(myDist.items())
x=myDist.copy()
print(x)
print(myDist.get('A'))
myDist['C']=100
print(myDist)
y=[2,7,9,5]
