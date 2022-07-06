class Food:
    def __init__(self,id, name, kcal, f_type):
        self.id = id
        self.name = name
        self.kcal = kcal
        self.type = f_type
    
    def print_info(self):
        print(self.name, self.kcal, self.type)
  
class FoodDictionary:
    def __init__(self, food_lst):
        self.food_lst = food_lst

    def add_food(self,food):
        self.food_lst.append(food)
    
    def print_info(self):
        for food in self.food_lst:
            food.print_info()




thitga = Food(1,"thịt gà", 200, "thịt")
thitheo = Food(2,"thịt heo", 176, "thịt")
thitbo = Food(4,"thịt bò", 453, "thịt")
cathu = Food(8,"cathu",265,"thịt")
thitcho = Food(9,"thịt chó",620,"thịt")
raucai = Food (5,"rau cải", 24, "rau")
raumuong = Food(3,"rau muống", 50, "rau")
caingot = Food(10,"cải ngọt", 36, "rau")
com = Food(6, "cơm", 200, "hạt")
hanhnhan = Food(7,"hạnh nhân", 35, "hạt")
ngo = Food(56,"ngô", 72,"hạt")
occho = Food (75, "óc chó", 23, "hạt")
food_lst = []
thit_list = []


ds_food = FoodDictionary(food_lst)
ds_food.add_food(thitga)
ds_food.add_food(thitheo)
ds_food.add_food(raumuong)
ds_food.print_info()

thitga.print_info()
print(thitga.type)


# phân nhóm thịt, rau, hạt
#set tỉ lệ thịt : rau : hạt =  a: b: c -> cố định hoặc tùy chọn 
# kcal_meal * a% / thịt (làm tròn)  =  +"g" = thịt cần 
import math
import random
Kcal_meal = 420
bua = 22
thit_list =[thitbo, thitga, thitheo, thitcho, cathu]
rau_lst = [raucai, raumuong,caingot]
hat_lst = [hanhnhan,com,occho,ngo]
diet_meat = {}
diet_veg = {}
diet_nut = {}
for thit in thit_list:
    mass_thit = round((((Kcal_meal * 0.45)/ thit.kcal))*100)
    diet_meat.setdefault(thit.name, mass_thit) 
for rau in rau_lst:
    mass_rau = round((((Kcal_meal* 0.45)/ rau.kcal))*100)
    diet_veg.setdefault(rau.name, mass_rau)
for hat in hat_lst:
    mass_hat = round((((Kcal_meal* 0.1)/hat.kcal))*100)
    diet_nut.setdefault(hat.name, mass_hat)
for i in range (0,bua):
    res = key, diet_m = random.choice(list(diet_meat.items()))
    res_2 = key, diet_v = random.choice(list(diet_veg.items()))
    res_3 = key, diet_n = random.choice(list(diet_nut.items()))
    print("bữa số", i+1, str(res), "g", str(res_2), "g", str(res_3), "g")
        

