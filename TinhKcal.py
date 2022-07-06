
#Tính KCal đốt nội tại: -> hàm tính KCAL -> input : kg, tuổi, chiều cao,gender 

def BMR_cal_F(kg,cm,age,delta,time,gender):
    import math
    if gender == "nữ":
        bmr_F = (kg*9.6) + (cm*1.8) + (age*4.7) + 655
        result_F = math.ceil(bmr_F/100.0)*100
        print("calo của bạn cần 1 ngày", ":", result_F)
        while delta/ time > 1/7:
            print("giảm kg nguy hiểm, hãy nhập lại số kg nhỏ hơn hoặc số ngày lớn hơn")
            delta = int(input(" nhập lại số kg"))
            time = int(input("nhập lại số ngày"))     
        else:
            kcal_diet = math.ceil(((result_F * time / (14 * delta))/100)*100)
            print("calo nạp 1 ngày để giảm ", delta, "kg","trong thời gian bạn muốn", ":", kcal_diet)
            kcal_meal = math.ceil(((kcal_diet/3)/100)*100)
            print("calo nạp 1 bữa để giảm", delta, "kg", "trong thời gian bạn muốn", ":", kcal_meal)
    if gender == "nam":
        bmr_M = (kg*13.7) + (cm*5)+ (age*6.8) +66
        result_M = math.ceil(bmr_M/100.0)*100
        print("calo của bạn cần 1 ngày", ":", result_M)
        while delta/ time > 1/7:
            print("giảm kg nguy hiểm, hãy nhập lại số kg nhỏ hơn hoặc số ngày lớn hơn")
            delta = int(input(" nhập lại số kg"))
            time = int(input("nhập lại số ngày"))     
        else:
            kcal_diet = math.ceil(((result_M * time / (14 * delta))/100)*100)
            print("calo nạp 1 ngày để giảm ", delta, "kg","trong thời gian bạn muốn", ":", kcal_diet)
            kcal_meal = math.ceil(((kcal_diet/3)/100)*100)
            print("calo nạp 1 bữa để giảm", delta, "kg", "trong thời gian bạn muốn", ":", kcal_meal)

BMR_cal_F(90,160,32,3,22, "nam")
#Lựa chọn phương pháp giảm kg: input : 2 tùy chọn có sẵn "Keto", "Low Carb", "Khác"
def diet_style_decide(style):
    if style == "keto":
        meat_r = 0.45
        veg_r = 0.45
        carb_r = 0.1
    elif style == "low carb":
        meat_r = 0.55
        veg_r = 0.25
        carb_r = 0.2
    elif style == "khác":
        meat_r = input("nhập tỉ lệ protein và lipid của bạn")
        veg_r = input("nhập tỉ lệ vitamin của bạn")
        carb_r = input("nhập tỉ lệ tinh bột của bạn")

#Bài Viết
# CRUD thực phẩm + nhóm thực phẩm
# CRUD gợi ý thực phẩm
# Gợi ý thực phẩm -> random seq

