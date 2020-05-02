v1=[1,23,4,56]
v2=[0,0,0,0]
print(v2[0])
s=[1,1,1,1,23,23,23,56]
for item in s:
    for i in range(0,len(v1)):
        if (item==v1[i]):
            v2[i]=v2[i]+1
print(v2)

