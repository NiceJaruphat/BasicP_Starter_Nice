# number = int(input("Enter your Number: "))
# num = 0
# for i in range(1 , number + 1):
#     num += 5
#     print (f"ครั้งที่ {i} ได้ผลเป็น " , num)

number = int(input("Enter your Number: "))
num = 0
i = 0
while i < number:
    num += 5
    i += 1
    print(f"ครั้งที่ {i} ได้ผลเป็น ", num)