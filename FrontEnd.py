#US1: 
#-> màn hình tính KCal:
#+ Tên -> input
#+ ĐT   -> input
#+ Tuổi * -> input
#+ Kg  *  -> input
#+ Cm *   -> input
#=> kết quả : Kcal dùng cho 1 ngày ()
# Số KG muốn giảm: (delta)
# Số ngày thực hiện (t) -> số bữa ăn gợi ý là t * 3

#US2:
# -> màn hình hiển thị Kcal cần 1 ngày
# -> Kcal nạp = KCal cần * t / (7*2 * delta) => công thức siêu tính giảm 1/2 Kcal thì 7 ngày giảm 1KG
# -> Kcal bữa = Kcal nạp /3 
# -> Chế độ ăn 1 = Keto = tỉ lệ Tinh Bột, Fat, Protein = 10%, 45%, 45%
# -> Chế độ ăn 2 = Low Carb = tỉ lệ TB, F, Protein = 25%, 40%, 30%
# -> Chế độ tùy chọn = TB, F, Pr

#US3:
#Generate Meal: -> tx3 bữa  = bữa 1,2,3,....n 
#điều kiện Meal Keto = chọn ngẫu nhiên trong list có sẵn (thit), (rau), (hat)
#sao cho lượng tổng Kcal = Kcal bữa và tỉ lệ Carb, Fat, Pro theo chế độ
# thêm món của bạn: gán vào (thit), (rau), (hat) (luong Kcal)


thit_list =["gà","lợn","cá","bò"]
rau_list = ["cai", "muop", "xalach"]
hat_list = ["com", "hanh nhan"]
bua = 5
for i in range (0,bua):
    import random
    diet_m = random.choice(thit_list)
    diet_v = random.choice(rau_list)
    diet_n = random.choice(hat_list)
    print("bữa số", i+1, diet_m, "thịt", diet_v, "rau", diet_n, "ngũ cốc")





