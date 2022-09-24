x,y,z = map(float,input().split())
s = x+y+z
a = s/2
A = a*(a-x)*(a-y)*(a-z)
B = A**0.5
print("{:.2f}".format(B))