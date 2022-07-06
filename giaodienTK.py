
import tkinter as tk

window = tk.Tk()
def login_btn_f():
    input_username = entry_user_name.get()
    input_password = entry_password.get()
    if input_username == username and input_password == password:
        lbl_message.config(text= "login successful")
    else:
        lbl_message.config(text= "login failed")


login_frame = tk.Frame(window)
login_frame.place(
    relx=0.5,
    rely=0.5,
    anchor= tk.CENTER
)

lbl_user_name = tk.Label(login_frame, text='User name: ')
lbl_password = tk.Label(login_frame, text='Password: ')
entry_user_name = tk.Entry(login_frame)
entry_password = tk.Entry(login_frame)
# ! xử lí khi nhấn nút
login_btn = tk.Button(
    login_frame, 
    text='Login',
    command= login_btn_f
    )

lbl_message = tk.Label(login_frame, text='')

lbl_user_name.grid(row=0, column= 0)
lbl_password.grid(row=1, column= 0)
entry_user_name.grid(row=0, column= 1)
entry_password.grid(row=1, column= 1)
login_btn.grid(row=2, column=0, columnspan=2)
lbl_message.grid(row=3, column=0, columnspan=2)

window.mainloop()