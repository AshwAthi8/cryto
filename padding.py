s=input()
x=len(s)
c=x%16
r=16-c
for i in range (0,r,1):
	s=s+"\\"+hex(r)
print(s)



