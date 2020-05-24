# gurvan buhel too damjuulna, gurvaljin mun esehig shalga -> bool
def triangle(a: int,b: int,c: int)->bool:
    if a<b+c and b<a+c and c<a+b:
        return True
    else:
        return False
a,b,c = [int(x) for x in input().split()]
if triangle(a,b,c):
    print("yes yes yes yes")
else:
    print("no no no no")