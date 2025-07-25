
try:
    with open("queue.txt", "r") as f:
        queue_number = int(f.read())
except:
    queue_number = 1


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

print("╔════════════════════════════════════════════════╗")
print("║              🍵 Drink Menu 🍹                  ║")
print("╠════════════════════════════════════════════════╣")
for drink in drinks:
    print(f"║ {drink['menu']:<40} ฿{drink['price']:>4} ║")
print("╚════════════════════════════════════════════════╝")


select_menu = int(input("Select Menu (1-10): "))

if 1 <= select_menu <= 10:
    selected_drink = drinks[select_menu - 1]
    price = selected_drink['price']
    print(f"\nMenu : {selected_drink['menu']} ราคา {price} บาท")


    print("Do u have a discount?")
    print("Yes: 1")
    print("No: 2")

    credit_sale = int(input(": "))
    if credit_sale == 1:
        price -= 5
        print("✅ ลด 5 บาท จากบัตรส่วนลด")


    promotion_day = int(input("กรุณากรอกวันที่ (1-31): "))
    if promotion_day % 2 != 0:
        price -= 7
        print("🎉 ได้รับโปรโมชั่นวันเลขคี่ ลดเพิ่มอีก 7 บาท")
    else:
        print("❌ วันที่ไม่ใช่เลขคี่ ไม่ได้รับโปรโมชั่น")

   
    print(f"\n💰 ราคาสุทธิของเมนู {selected_drink['menu']} คือ: {price} บาท")

    
    print("\n🎫 Que : ")
    print("══════════════════════")
    print(f"     คิวหมายเลข : {queue_number}")
    print("     กรุณารอเรียกคิว")
    print("══════════════════════")


    queue_number += 1
    with open("queue.txt", "w") as f:
        f.write(str(queue_number))

else:
    print("❌ กรุณาเลือกหมายเลขเมนูระหว่าง 1 ถึง 10 เท่านั้น")
