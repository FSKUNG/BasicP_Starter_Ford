# """"
# a = int(input("Enter num: "))
# b = int(input("Enter num: "))

# print(a+b)

# if a == 50:
#     print("123")
# else:
#     print("321")
# """

# x = int(input("Enter x :"))
# y = int(input("Enter y :"))

# if x > y:
#     print(f"{x}>{y}")
# elif x < y:
#     print(f"{x}<{y}")
# elif x == y:
#     print(f"{x}={y}")
# else :
#     print("idk")


D = int(input("Enter Distance: "))



print("Distance: ",D)
if D < 5:
    print("Free shipping")
elif D >= 5 and D<= 50:
    print("ค่าส่ง 10 บาท")
    vat = 10*7/100
    print("Vat = ",vat)
    print("Price + Vat = ",vat+10)
elif D >= 51 and D<= 100:
    print("ค่าส่ง 15 บาท")
    vat = 15*7/100
    print("Vat = ",vat)
    print("Price + Vat = ",vat+15)
elif D >= 101 and D<= 300:
    print("ค่าส่ง 25 บาท")
    vat = 25*7/100
    print("Vat = ",vat)
    print("Price + Vat = ",vat+25)
elif D >= 301 and D<= 500:
    print("ค่าส่ง 35 บาท")
    vat = 35*7/100
    print("Vat = ",vat)
    print("Price + Vat = ",vat+35)
else:
    print("ค่าส่ง 45 บาท")
    vat = 45*7/100
    print("Vat = ",vat)
    print("Price + Vat = ",vat+45)




