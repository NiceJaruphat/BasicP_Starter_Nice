vava_monster_hp = 100
Sword_Damage = 20
Bow_Damage = 10
Magic_Damage = 30

player_choice_ = int(input("ต่อสู้มอน กด 1  หรือ ออก กด 2 : "))

if player_choice_ == 1:
    print("คุณเลือกต่อสู้กับมอนสเตอร์")
    round = int(input("กรุณากรอกจำนวนรอบที่ต้องการต่อสู้: "))
    for i in range(1, round+1):
        player_choice_Damage = input("เลือกอาวุธ (bow = 10hp sword = 20hp magic = 30hp): ")
        if player_choice_Damage.lower() == "sword":
            vava_monster_hp -= Sword_Damage
            print(f"รอบที่ {i} คุณใช้ดาบโจมตีมอนสเตอร์ 20HP เหลือ {vava_monster_hp}")
        elif player_choice_Damage.lower() == "bow":
            vava_monster_hp -= Bow_Damage
            print(f"รอบที่ {i} คุณใช้ธนูโจมตีมอนสเตอร์ 10HP เหลือ {vava_monster_hp}")
        elif player_choice_Damage.lower() == "magic":
            vava_monster_hp -= Magic_Damage
            print(f"รอบที่ {i} คุณใช้เวทมนตร์โจมตีมอนสเตอร์ 30HP เหลือ {vava_monster_hp}")
        else:
            print("อาวุธที่เลือกไม่ถูกต้อง")

        if vava_monster_hp == 0:
            print("คุณชนะมอนสเตอร์แล้ว!")
            break
        elif vava_monster_hp < 0:
            vava_monster_hp = 20
            print(f"มอนสเตอร์ฮีล HP {vava_monster_hp} ")
            
        else:
            print(f"มอนสเตอร์ยังไม่ตาย คุณยังเหลืออีก { round - i} รอบในการต่อสู้")

    if vava_monster_hp > 0:
        print("มอนสเตอร์ยังมี HP เหลืออยู่ คุณแพ้การต่อสู้")
        exit()



elif player_choice_ == 2:
    print("ออกจากเกม")
    exit()
else:
    print("เลือกผิดพลาด")
    exit()


