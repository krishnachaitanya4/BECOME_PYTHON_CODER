def position(n):
    a,b=0,1
    if(is_fib(n)):
       
        if n==0:
            print(0)
            return
        if n==1:
            print(1,2)
            return
        p_c =2
        c=0
        while c<=n:
                d=c
                c=a+b
                a=b
                b=c
                if c==n:
                    print(p_c)
                p_c+=1
    else:
        print( False)
        
def is_fib(n):
    a,b=0,1
    if n==0:
        return True
    c=0
    while c<=n:
            d=c
            c=a+b
            a=b
            b=c
            if c==n:
                return True
    return False
  n=int(input())
  position(n)
