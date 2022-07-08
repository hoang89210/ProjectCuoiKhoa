

from tkinter import END, RIGHT, ttk, StringVar, Tk, VERTICAL, HORIZONTAL, W, NS, N, S

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


# ds_food = FoodDictionary(food_lst)
# ds_food.add_food(thitga)
# ds_food.add_food(thitheo)
# ds_food.add_food(raumuong)
# ds_food.print_info()

# def BMR_cal_F():
#     kg = float(ent_your_kg.get())
#     cm = float(ent_your_cm.get())
#     age = float(ent_your_age.get())
#     delta = float(ent_delta_kg.get())
#     time = float(ent_time.get())
#     import math
#     if gender == "nữ":
#         bmr_F = math.ceil(((float(ent_your_kg.get())*9.6) + (float(ent_your_cm.get())*1.8) + (float(ent_your_age.get())*4.7) + 655)/100)*100
#         kcal_diet = math.ceil((((((bmr_F* float(ent_time.get()))/ (14* float(ent_delta_kg.get())))/100 *100)/ 3)/100)*100)
#         print("calo của bạn cần 1 ngày", ":", bmr_F)
#         while delta/ time > 1/7:
#             print("giảm kg nguy hiểm, hãy nhập lại số kg nhỏ hơn hoặc số ngày lớn hơn")
#             # delta = int(input(" nhập lại số kg"))
#             # time = int(input("nhập lại số ngày"))     
#         else:
#             kcal_diet = math.ceil(((bmr_F* time / (14 * delta))/100)*100)
#             print("calo nạp 1 ngày để giảm ", delta, "kg","trong thời gian bạn muốn", ":", kcal_diet)
#             kcal_meal = math.ceil(((kcal_diet/3)/100)*100)
#             lbl_message.config("calo nạp 1 bữa để giảm", delta, "kg", "trong thời gian bạn muốn", ":", kcal_meal)
#     elif gender == "nam":
#         bmr_M = (kg*13.7) + (cm*5)+ (age*6.8) +66
#         result_M = math.ceil(bmr_M/100.0)*100
#         print("calo của bạn cần 1 ngày", ":", result_M)
#         while delta/ time > 1/7:
#             print("giảm kg nguy hiểm, hãy nhập lại số kg nhỏ hơn hoặc số ngày lớn hơn")
#             # delta = int(input(" nhập lại số kg"))
#             # time = int(input("nhập lại số ngày"))     
#         else:
#             kcal_diet = math.ceil(((result_M * time / (14 * delta))/100)*100)
#             print("calo nạp 1 ngày để giảm ", delta, "kg","trong thời gian bạn muốn", ":", kcal_diet)
#             kcal_meal = math.ceil(((kcal_diet/3)/100)*100)
#             lbl_message.config("calo nạp 1 bữa để giảm", delta, "kg", "trong thời gian bạn muốn", ":", kcal_meal)

def generate_diet_meal(kg,cm,age,delta,time,gender):
    kg = float(ent_your_kg.get())
    cm = float(ent_your_cm.get())
    age = float(ent_your_age.get())
    delta = float(ent_delta_kg.get())
    time = float(ent_time.get())
    gender = ent_your_gender
    import math
    if gender == "nữ":
        bmr_F = math.ceil(((float(ent_your_kg.get())*9.6) + (float(ent_your_cm.get())*1.8) + (float(ent_your_age.get())*4.7) + 655)/100)*100
        kcal_diet = math.ceil((((((bmr_F* float(ent_time.get()))/ (14* float(ent_delta_kg.get())))/100 *100)/ 3)/100)*100)
        print("calo của bạn cần 1 ngày", ":", bmr_F)
        while delta/ time > 1/7:
            print("giảm kg nguy hiểm, hãy nhập lại số kg nhỏ hơn hoặc số ngày lớn hơn")
            # delta = int(input(" nhập lại số kg"))
            # time = int(input("nhập lại số ngày"))     
        else:
            kcal_diet = math.ceil(((bmr_F* time / (14 * delta))/100)*100)
            print("calo nạp 1 ngày để giảm ", delta, "kg","trong thời gian bạn muốn", ":", kcal_diet)
            kcal_meal = math.ceil(((kcal_diet/3)/100)*100)
            lbl_message.config("calo nạp 1 bữa để giảm", delta, "kg", "trong thời gian bạn muốn", ":", kcal_meal)
    elif gender == "nam":
        bmr_M = (kg*13.7) + (cm*5)+ (age*6.8) +66
        result_M = math.ceil(bmr_M/100.0)*100
        print("calo của bạn cần 1 ngày", ":", result_M)
        while delta/ time > 1/7:
            print("giảm kg nguy hiểm, hãy nhập lại số kg nhỏ hơn hoặc số ngày lớn hơn")
            # delta = int(input(" nhập lại số kg"))
            # time = int(input("nhập lại số ngày"))     
        else:
            kcal_diet = math.ceil(((result_M * time / (14 * delta))/100)*100)
            print("calo nạp 1 ngày để giảm ", delta, "kg","trong thời gian bạn muốn", ":", kcal_diet)
            kcal_meal = math.ceil(((kcal_diet/3)/100)*100)
            lbl_message.config("calo nạp 1 bữa để giảm", delta, "kg", "trong thời gian bạn muốn", ":", kcal_meal)
    import math
    import random
    Kcal_meal = math.ceil((((((math.ceil(((float(ent_your_kg.get())*9.6) + (float(ent_your_cm.get())*1.8) + (float(ent_your_age.get())*4.7) + 655)/100)*100* float(ent_time.get()))/ (14* float(ent_delta_kg.get())))/100 *100)/ 3)/100)*100)
    bua = int(ent_time.get()) * 3
    thit_list =[thitbo, thitga, thitheo, thitcho, cathu]
    rau_lst = [raucai, raumuong,caingot]
    hat_lst = [hanhnhan,com,occho,ngo]
    diet_meat = {}
    diet_veg = {}
    diet_nut = {}
    meal_list =[]
    if diet_style.get() == "Keto":
        thit_rate = 0.45
        rau_rate = 0.45
        hat_rate = 0.1
    elif diet_style.get() == "Low_Carb":
        thit_rate = 0.5
        rau_rate = 0.3
        hat_rate = 0.2
        for thit in thit_list:
            mass_thit = round((((Kcal_meal * thit_rate)/ thit.kcal))*100)
            diet_meat.setdefault(thit.name, mass_thit) 

        for rau in rau_lst:
            mass_rau = round((((Kcal_meal* rau_rate)/ rau.kcal))*100)
            diet_veg.setdefault(rau.name, mass_rau)

        for hat in hat_lst:
            mass_hat = round((((Kcal_meal* hat_rate)/hat.kcal))*100)
            diet_nut.setdefault(hat.name, mass_hat)

        for i in range (0,bua):
            res = key, diet_m = random.choice(list(diet_meat.items()))
            res_2 = key, diet_v = random.choice(list(diet_veg.items()))
            res_3 = key, diet_n = random.choice(list(diet_nut.items()))
            dict = {"bữa số"+ str(i+1) + str(res) + "g" + str(res_2) + "g" + str(res_3) + "g"}
            treeview.insert('', END, value = (str(i+1), str(res), str(res_2), str(res_3)))
            meal_list.append(dict)
            print(meal_list)



def validation_delta_time():
    delta = float(ent_delta_kg.get())
    time = float(ent_time.get())
    if delta/time < 1/7:
        print("Giảm kg nguy hiểm chỉ nên giảm 1kg 7 ngày")
        lbl_message.config(text= "Giảm kg nguy hiểm chỉ nên giảm 1kg 7 ngày")
    else:
        lbl_message.config(text= "Cố lên bạn giảm cân được")
    
def diet_style_decide():
    if diet_style.get() == "Keto":
        pass
    elif diet_style == "Low_Carb":
        pass
    pass

def readfile():
    diet_style = ["Keto", "Low_Carb"]
    return diet_style

def clear_entry_button():
    if treeview.size != 0:
        ent_time.delete(0)
        ent_delta_kg.delete(0)

def clear_table():
    if treeview.size != 0:
        ent_time.delete(0)
        ent_delta_kg.delete(0)
    for i in treeview.get_children():
        treeview.delete(i)

root = Tk()
root.title("Chế Độ Ăn Kiêng")

root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))


ttk.Style().configure("Main.TFrame", background="#F6F4EC")
mainframe = ttk.Frame(root, style="Main.TFrame", height=root.winfo_screenheight(), width=root.winfo_screenwidth())
mainframe.grid(column=0, row=0, padx=10)

# Bên Trái:
left = ttk.Frame(mainframe)
left.grid(column=1, row=1, padx=5, pady=30, sticky=N)
left.rowconfigure(0, weight=1)


# phương thức ăn kiêng
lbl_diet_style = ttk.Label(left, text="diet_style", font=("System", 15, "bold"),
        padding=10)
lbl_diet_style.grid(column=1, row=1)

#số kg của bạn:
lbl_your_kg = ttk.Label(left, text= " số kg của bạn", font= ("System", 15,"bold"), padding= 10)
lbl_your_kg.grid (column=1, row = 3)

ent_your_kg = ttk.Entry(left, text = "điền số kg")
ent_your_kg.grid(column= 1, row = 4 )

#chiều cao của bạn:
lbl_your_cm = ttk.Label(left, text= " chiều cao của bạn theo cm", font= ("System", 15,"bold"), padding= 10)
lbl_your_cm.grid (column=1, row = 5)

ent_your_cm = ttk.Entry(left, text = "điền số cm")
ent_your_cm.grid(column= 1, row = 6 )

#số tuổi của bạn:
lbl_your_age = ttk.Label(left, text= " số tuổi", font= ("System", 15,"bold"), padding= 10)
lbl_your_age.grid (column=1, row = 7)

ent_your_age = ttk.Entry(left, text = "điền số tuổi")
ent_your_age.grid(column= 1, row = 8 )

#giới tính của bạn:
lbl_your_gender = ttk.Label(left, text= " giới tính", font= ("System", 15,"bold"), padding= 10)
lbl_your_gender.grid (column=1, row = 9)

ent_your_gender = ttk.Entry(left, text = "điền nam hoặc nữ")
ent_your_gender.grid(column= 1, row = 10 )

# số kg muốn giảm
lbl_delta_kg = ttk.Label(left, text="KG muốn giảm", font=("System", 15, "bold"),
        padding=10)
lbl_delta_kg.grid(column=1, row=11)

ent_delta_kg = ttk.Entry(left, text='kg chênh')
ent_delta_kg.grid(column=1, row= 12)

# ngày giảm cân
lbl_day = ttk.Label(left, text="Thời Gian Giảm KG", font=("System", 15, "bold"),
        padding=10)
lbl_day.grid(column=1, row=13)


ent_time = ttk.Entry(left, text='ngày giảm kg')
ent_time.grid(column=1, row =14)

# cảnh báo dữ liệu: 
lbl_message = ttk.Label(left, text="Message", font=("System", 15, "bold"),
        padding=10)
lbl_message.grid(column=1, row=15)

check_button = ttk.Button(left, text="Check Dangerous", style="Bn.TButton",
        padding=2, command= validation_delta_time)

check_button.grid(column=1, row=16, sticky=N, pady=20)
# Nút tạo bữa ăn
ttk.Style().configure("Bn.TButton", font=('System', '13'), background="blue")
Generate_button = ttk.Button(left, text="Generate_Meal", style="Bn.TButton",
        padding=2, command= generate_diet_meal(ent_your_kg, ent_your_cm, ent_your_age , ent_delta_kg, ent_time, ent_your_gender))
Generate_button.grid(column=1, row=17, sticky=N, pady=20)

view_food_list = ttk.Button(left, text = "xóa danh sách bữa ăn", style="Bn.TButton", command= clear_table)
view_food_list.grid(column=1, row= 18)

# Nút xóa bữa ăn:
clear_table_button = ttk.Button(left, text = "view_food_list", style="Bn.TButton", command= clear_table)
clear_table_button.grid(column=1, row= 19)


#Bên Phải:

ttk.Style().configure("Right.TFrame", background="#F6F4EC")

right = ttk.Frame(mainframe, style="Right.TFrame")
right.grid(column=2, row=1, padx=10)
right.rowconfigure(1, weight=1)


treeview = ttk.Treeview(right, columns=["Bữa Số", "Thịt", "Rau", "Hạt"],  height=40)

treeview.grid(column=1, row=2)
vbar = ttk.Scrollbar(right, orient=VERTICAL, command=treeview.yview)
hbar = ttk.Scrollbar(right, orient=HORIZONTAL, command=treeview.xview)
ttk.Style().configure("Table.Treeview", background="#F6F4EC", font=("System", 18), rowheight=40)
treeview.configure(yscrollcommand=vbar.set, xscrollcommand=hbar.set, style="Table.Treeview")
vbar.grid(row=4, column=2, sticky=NS)
hbar.grid(row=5, column=1, sticky=NS)

ttk.Style().configure("Treeview.Heading", font=( 20))

treeview.column("Bữa Số", anchor='center') 
treeview.column("Thịt", anchor='center')
treeview.column("Rau", anchor='center')
treeview.column("Hạt", anchor='center')
    
treeview.heading("Bữa Số", text="Bữa Số") 
treeview.heading("Thịt", text="Thịt")
treeview.heading("Rau", text="Rau")
treeview.heading("Hạt", text="Hạt")
treeview['show'] = 'headings'

#Style ăn kiêng:
ttk.Style().configure("List.TCombobox", font=('System', '50'))
diet_style = StringVar()
diet_style = ttk.Combobox(left,
                        textvariable=diet_style,
                        height=20,
                        font=("'@System", 12)) 
diet_style["values"] = readfile() 
#diet_style.current(0)  
#diet_style.bind("<<ComboboxSelected>>", plate_refresh)
diet_style.grid(column=1, row=2)

#Bảng Dữ Liệu: 

def table_refresh():
    ## the name of table
    name_table = ttk.Label(right,
              text=" Kế Hoạch Ăn Kiêng",
              font=("System", 30),
              foreground="black",
              padding=20,
              background="#F6F4EC")

    name_table.grid(column=1, row=1, sticky=W)

## create the table
# def data_refresh():
#     global data

#     data[0] = plate_list.get()
#     read_file()


ttk.Style().configure("Right.TFrame", background="#F6F4EC")



root.mainloop()
