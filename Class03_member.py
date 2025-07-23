member = input("กรุณากรอกระดับสมาชิก : ")
price = int(input("กรุณากรอกราคาสินค้า : "))
date= int(input("กรุณากรอกวันที่ (DD) : "))

if(member == "Gold"):
    if(price >= 1000):
        discount = 0.15
    else:
        discount = 0.10
elif(member == "Silver"):
    if(price >= 1000):
        discount = 0.10
    else:
        discount = 0.05
else:
    discount = 0.00

pricediscount = price * discount
sumprice = price - pricediscount
datediscount = 0
if(date % 2 != 0 ):
    if(sumprice >= 500):
        datediscount = sumprice * 0.05
    else:
        datediscount = 0

allprice = sumprice - datediscount
expression = 0
if(allprice < 800):
    expression = 50
else:
    expression = 0

netprice = allprice + expression

print("------------------------------")
print("ระดับสมาชิก :", member)
print("ราคาสินค้า :", price, "บาท")   
print("ส่วนลด :", pricediscount, "บาท")
print("ราคาหักส่วนลดสมาชิก :", sumprice, "บาท")
print("ส่วนลดตามวันที่ :", datediscount, "บาท")
print("ราคาก่อนจัดส่ง :", allprice, "บาท")   
print("ค่าจัดส่ง :", expression, "บาท")     
print("------------------------------")
print("ราคาสุทธิ :", netprice, "บาท")
print("------------------------------")
print("ขอบคุณที่ใช้บริการ")