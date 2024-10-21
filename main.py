# def swap(a,b):
#     print("before swapping", a ,b)
#     a=a^b
#     b=a^b
#     a=a^b
#     print("after swapping", a,b)
# swap(5,9)
def swap2(a,b):
    a=(a&b) + (a|b)
    b=a+(~b+1)
    a=a+(~b)+1
    print("after swapping", a,b)
swap2(6,7)