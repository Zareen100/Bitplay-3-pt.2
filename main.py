# def swap(a,b):
#     print("before swapping", a ,b)
#      a=a^b
#     b=a^b
#      a=a^b
#      print("after swapping", a,b)
#  swap(5,9)
# def swap2(a,b):
#     a=(a&b) + (a|b)
#     b=a+(~b+1)
#     a=a+(~b)+1
#     print("after swapping", a,b)
# swap2(6,7)

def divide(ourdividend, ourDivisor):
  sign = (-1 if((ourdividend < 0) ^ (ourDivisor < 0)) else 1);
  ourdividend = abs(ourdividend);
  ourDivisor = abs(ourDivisor);

  quotientNumber = 0
  tempNumber = 0
  for i in range(31, -1, -1):
    if (tempNumber + (ourDivisor << i) <= ourdividend):
      tempNumber += ourDivisor << i
      quotientNumber |= 1 << i
  if sign == -1:
    quotientNumber = -quotientNumber
  return quotientNumber

a = int(input("Enter a for a/b: "))
b = int(input("Enter b for a/b: "))
print("Result of", a, "/", b, "is", divide(a, b))