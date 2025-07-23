score = int(input("ใส่คะแนน : "))
grade = ""
status = ""
if(score >= 50):
    status = "ผ่าน"
    if(score >= 80 and score <= 100) :
        grade = "A"
    elif(score >= 70 and score < 80) :
        grade = "B"
    elif(score >= 60 and score < 70) :
        grade = "C"
    elif(score >= 50 and score < 60) :          
        grade = "D"
else :
    status = "ไม่ผ่าน"
    if(score >= 0 and score < 50) :  
        grade = "F"


print("คะแนน : ", score, "เกรด : ", grade) 
print("สถานะ : ", status)