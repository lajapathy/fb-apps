

def outer_func(a,b,c="sss",d=5,x="ddd"):
    b=7
    def inner_func():
        print(c)
        print(a)
        a=3
        print(a)
        print(b)
        print(c)
        print(d)
        print(x)
    inner_func()

outer_func(10,20)
