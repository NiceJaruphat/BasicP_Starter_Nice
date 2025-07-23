distance = int(input("ใส่ระยะทาง : "))
price = next((p for d, p in [(500, 45), (300, 35), (100, 25), (50, 15), (5, 10), (0, 0)] if distance > d), None)
if price is None:
    print("Error")
else:
    vat = price * 0.07
    print(f"ระยะทาง : {distance} KM ราคาขนส่ง : {price} บาท ภาษี : {vat:.2f} บาท ราคาสุทธิ: {price + vat:.2f} บาท")