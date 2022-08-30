#append

c = [ 10, 20, 30 ]
c.append(40)
c.append(50)
print(c)

#insert

a = [1,2,3,4,5]
print(a)
a.insert(1,10)
print(a)

#extend

x = [1,2,3]
y = [4,5,6]
x.extend(y)
print("x: ", x)
print("y: ", y)

z = x + y
print("z: ", z)

x += [7,8,9]
print("x: ", x)