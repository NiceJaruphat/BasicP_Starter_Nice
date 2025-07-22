distance = int(input("ใส่ระยะทาง : "))
price = 0
if(distance > 500) :
    price = 45
elif(distance > 300) :
    price = 35
elif(distance > 100) :
    price = 25
elif(distance > 50) :
    price = 15
elif(distance > 5) :
    price = 10
elif(distance > 0) :
    price = 0
else :
    print("Error")

vat = price * 7/100
print("ระยะทาง : " , distance , "KM" , "ราคาขนส่ง :" , price , "บาท" , "ภาษี :" , vat , "บาท" , "ราคาสุทธิ:" , (price + vat) , "บาท" )