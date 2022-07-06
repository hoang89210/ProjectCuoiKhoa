
#tính BMR Nữ:
def BMR_cal_F(kg,cm,age):
    import math
    bmr_F = (kg*9.6) + (cm*1.8) + (age*4.7) + 655
    result_F = math.ceil(bmr_F/100.0)*100
    print("calo của bạn cần 1 ngày", ":", result_F)

#Tính BMR Nam:
def BMR_cal_M(kg,cm,age):
    import math
    bmr_M = (kg*13.7) + (cm*5)+ (age*6.8) +66
    result_M = math.ceil(bmr_M/100.0)*100
    print("calo của bạn cần 1 ngày", ":", result_M)

#Số KG muốn giảm
#Time muốn giảm KG

#Tính KCAL cho 1 bữa:
def Kcal_meal():
    import math
    Kcal_meal = BMR_cal_F()
    pass

# Generate Meal: 
def food_suitable:
    pass

def generate_meal:
    import random
    for i range (0,)
    pass
