def func(*args):
    c = a+b
    return c,args

a=1
b=2
d={'pipo':3,'caca':'2'}
x,y=func(a,b,d)

print(x)
print(y)
