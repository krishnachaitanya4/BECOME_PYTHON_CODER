def first_reverse(n):
    dn=n
    dc=0
    while dn:
        dn=dn//10
        dc+=1
    dc-=1
    r=n%10
    num=n//10
    n2=r*(10**dc)+num
    print(n2)

def middle_reverse(n):
    rev=0
    dn=n
    dc=0
    while dn:
        dn=dn//10
        dc+=1
    dc2=dc
    first_num=n//(10**(dc-1))
    last_num=n%10
    while(n):
        if dc == dc2 or dc == 1:
            dc-=1
            n=n//10
            continue
        r=n%10
        n=n//10
        if r==0 :
            r=1
        rev=rev*10+r
        dc-=1
    n2=first_num*(10**(dc2-2))+rev
    n2=n2*10+last_num
    print(n2)

n1=int(input())   
middle_reverse(n1)
n2=int(input())
first_reverse(n2)
