import tkinter as tk
from tkinter import *
main_window = tk.Tk()

window_height = 500
window_width = 500
screen_width = main_window.winfo_screenwidth() 
screen_height = main_window.winfo_screenheight()
padding_top = screen_height // 2 - window_height // 2
padding_left = screen_width // 2 - window_width // 2

main_window.geometry('{}x{}+{}+{}'.format(window_width, window_height, padding_left, padding_top))

main_frame = tk.Frame(main_window)
main_frame.place(
   relx= 0.5,
   rely= 0.5,
   anchor= tk.S
)

def get_widget_name(widget):
    return str(widget).split('.')[2]



def Kcal_can(weight, height, age, gender):
    import math
    gender = en_gender.get()
    age = int(en_age.get())
    weight = int(en_weight.get())
    height = int(en_height.get())
    if gender == "nữ":
        Kcal_can = (weight*9.6) + (height*1.8) + (age*4.7) + 655
        result_F = math.ceil(Kcal_can/100.0)*100
        print("calo của bạn cần 1 ngày", ":", result_F)
    elif gender == "nam":
        Kcal_can = (weight*13.7) + (height*5)+ (age*6.8) +66
        result_M = math.ceil(Kcal_can/100.0)*100
        print("calo của bạn cần 1 ngày", result_M)
        


lbl_weight = tk.Label(main_frame, text= "cân nặng của bạn với kg: ")
lbl_age = tk.Label(main_frame, text= "Tuổi của bạn: ")
lbl_height = tk.Label(main_frame, text= "chiều cao của bạn với cm: ")
lbl_delta = tk.Label(main_frame, text= "số kg muốn giảm ")
lbl_day = tk.Label(main_frame, text= "số ngày thực hiện ")
lbl_gender = tk.Label(main_frame, text = "giới tính của bạn")
lbl_message = tk.Label(main_frame, text = "Kcal cần nạp mỗi ngày")

en_weight = tk.Entry(main_frame, name = 'en_weight')
en_age = tk.Entry(main_frame, name='en_age')
en_height = tk.Entry(main_frame, name='en_height')
en_delta = tk.Entry(main_frame, name='en_delta')
en_day = tk.Entry(main_frame, name='en_day')
en_gender = tk.Entry(main_frame, name='en_gender')
btn_BMR = tk.Button(main_frame, text="tính Kcal Cần Nạp", command= Kcal_can)
#btn_search = tk.Button(main_frame, text= 'Search', command= search)
#lstbox_phone = tk.Listbox(main_frame)

lbl_weight.grid( row=0, column=0) 
lbl_age.grid( row=1, column=0)
lbl_height.grid(row=2, column=0)
lbl_delta.grid(row=3, column=0)
lbl_day.grid(row=4, column=0)
lbl_gender.grid(row=5, column=0)
en_weight.grid(row=0, column=1)
en_age.grid(row=1, column=1)
en_height.grid(row=2, column=1)
en_delta.grid(row=3, column=1)
en_day.grid(row=4, column=1)
en_gender.grid(row=5, column=1)
btn_BMR.grid(row=6, column =0, columnspan= 4 )
lbl_message.grid(row=7, column= 0, columnspan= 4)


main_window.mainloop()