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


# D = int(input("Enter Distance: "))



# print("Distance: ",D)
# if D < 5:
#     print("Free shipping")
# elif D >= 5 and D<= 50:
#     print("ค่าส่ง 10 บาท")
#     vat = 10*7/100
#     print("Vat = ",vat)
#     print("Price + Vat = ",vat+10)
# elif D >= 51 and D<= 100:
#     print("ค่าส่ง 15 บาท")
#     vat = 15*7/100
#     print("Vat = ",vat)
#     print("Price + Vat = ",vat+15)
# elif D >= 101 and D<= 300:
#     print("ค่าส่ง 25 บาท")
#     vat = 25*7/100
#     print("Vat = ",vat)
#     print("Price + Vat = ",vat+25)
# elif D >= 301 and D<= 500:
#     print("ค่าส่ง 35 บาท")
#     vat = 35*7/100
#     print("Vat = ",vat)
#     print("Price + Vat = ",vat+35)
# else:
#     print("ค่าส่ง 45 บาท")
#     vat = 45*7/100
#     print("Vat = ",vat)
#     print("Price + Vat = ",vat+45)


# d = int(input("Enter: "))

# if d > 50:
#     print("ผ่าน")
# if d >= 80:
#     print("A")
# elif d >= 70:
#     print("B")
# elif d >= 60:
#     print("C")
# elif d >= 50:
#     print("D")
# else:
#     print("ไม่ผ่าน")
#     print("F")

# member = input("Enter member: ")
# price = int(input("Enter price: "))
# date = int(input("Enter date: "))

# discout = 0

# if member == "gold":
#     if price >= 1000:
#         print("ได้ส่วนลด 15%")
        
#     else:
#         print("ได้ส่วนลด 10%")
# elif member == "silver":
#     if price >= 1000:
#         print("ได้ส่วนลด 10%")
#     else:
#         print("ได้ส่วนลด 5%")
# else:
#     print("ไม่มีส่วนลด")
# if price > 500:
#     if price % 2 == 1:
#         print("โปรพิเศษลดอีก 5%")
#     else:
#         print(" ")
# else:
#     print(" ")


# num = int(input("Enter your num: "))
# sum = 0
# for i in range(1,num +1):
#     sum = sum + 5
#     print("ครั้งที่{i}, ได้ {sum}"")

# i = 1
# num = int(input("Enter your num: "))
# a = int(input("Enter your a: "))
# while i <= a:
#     print(f"ครั้งที่ {i} ได้ {num} ")
#     num += 5
#     i += 1 
monster = ()
hp = 100

axe = 30
sword = 100
dagger = 25

chooseweapon = [axe, sword, dagger]

start = int(input("Select start(1) or exit(2) : "))
if start == 1:
    times = int(input("Type times to hit: "))
    i = 0
    while i <= times:
    
        selectweapon = int(input("Select weapon| axe(0) , sword(1) , dagger(2): "))
        baseDAMAGE = chooseweapon[selectweapon]
        hp = hp - baseDAMAGE
        print(f"Boss Hp is: {hp}")
        if hp == 0:
            print("Boss defeted")
            break
        elif hp < 0:
            hp +20
        else:
            print("Player lose")  
            break
        i += 1

elif start == 2:
    exit
else:
  print("aaa")
