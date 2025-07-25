drinks = [
    {'menu': '1 Matcha', 'price': 55},
    {'menu': '2 Iced Thai Milk Tea', 'price': 45},
    {'menu': '3 Coconut Milk Tea', 'price': 50},
    {'menu': '4 Hot Matcha Latte', 'price': 60},
    {'menu': '5 Matcha Coconut Smoothie', 'price': 65},
    {'menu': '6 Coconut Matcha Frappe', 'price': 70},
    {'menu': '7 Thai Milk Tea with Coconut Cream', 'price': 55},
    {'menu': '8 Matcha Milk Tea with Coconut Jelly', 'price': 65},
    {'menu': '9 Iced Matcha Thai Milk Tea', 'price': 60},
    {'menu': '10 Hot Thai Milk Tea', 'price': 45}
]

print("-------------Menu---------------")
for i in drinks:
    print(f"{i['menu']} - {i['price']} บาท")

print("\nคุณมีบัตรส่วนลดมั้ย")
print("มีกด 1 ")
print("ไม่มีกด 2 ")
credit_sale = int(input(" : "))

for drink in drinks:
    menu_number = int(drink['menu'].split()[0])  # ดึงเลขเมนูจากชื่อ เช่น "1 Matcha" → 1
    if menu_number == select_menu:
        if credit_sale == 1:
            discounted_price = drink['price'] - 5
            print(f"{drink['menu']} - ลดเหลือ {discounted_price} บาท (จาก {drink['price']} บาท)")
    elif credit_sale == 2:
        print("\nไม่มีส่วนลด แสดงราคาปกติ:")
    for i in drinks:
        print(f"{i['menu']} - {i['price']} บาท")
    else:
        print("กรุณาเลือกแค่ 1 หรือ 2 เท่านั้น")
