import tkinter as tk


# * Name, phone number
# todo: create( add info), read( get info), update( update info), delete ( delete info)
# todo: working with files
# * widgets:
# *  lblname, lblphone , lbmessage
# *  entryname, entryphone
# *  add, update, delete, search button 
# *  view list
main_window = tk.Tk()

window_height = 600
window_width = 600
screen_width = main_window.winfo_screenwidth() 
screen_height = main_window.winfo_screenheight()
padding_top = screen_height // 2 - window_height // 2
padding_left = screen_width // 2 - window_width // 2

main_window.geometry('{}x{}+{}+{}'.format(window_width, window_height, padding_left, padding_top))

main_frame = tk.Frame(main_window)
main_frame.place(
    relx= 0.5,
    rely= 0.5,
    anchor= tk.CENTER
)


phone_dict = {
    'vinhbc': '123',
    'vinhad': '456',
}

def get_widget_name( widget):
    return str(widget).split('.')[2]

def simple_validation( widget):
    is_valid = True
    widget_name = get_widget_name(widget)
    if widget_name == 'en_phonenumber' or widget_name == 'en_name':
        if widget.get() == '' or widget.get() == None:
            is_valid = False
    return is_valid
    
def is_exist_phonenumber(phonenumber):
    for per in phone_dict:
        if phonenumber == phone_dict[per]:
            return True
    return False
        
def is_exist_name(name):
    if name in phone_dict:
        return True
    return False

def is_valid_info(name, phonenumber):
    if is_exist_name(name):
        lbl_message.config(text= "Message: Tên đã tồn tại")
        return False
    if is_exist_phonenumber(phonenumber):
        lbl_message.config(text= "Message: Số điện thoại đã tồn tại")
        return False
    return True

def add_phone():
    if not simple_validation(en_name) or not simple_validation(en_phonenumber):
        lbl_message.config(text= "Message: Thông tin chưa hợp lệ")
        return
    lbl_message.config(text= "Message: Thông tin hợp lệ")
    if is_valid_info(en_name.get(), en_phonenumber.get()):
        phone_dict[en_name.get()] = en_phonenumber.get()
        en_name.delete(0,tk.END)
        en_phonenumber.delete(0,tk.END)
        lbl_message.config(text= "Message: Thêm thông tin thành công")

def lstbox_phone_onselect(event):
    if lstbox_phone.size() > 0:
        index = lstbox_phone.curselection()
        print(index)
        lstbox_phone.get(index)
        en_name.delete(0, tk.END)
        en_name.insert(0, lstbox_phone.get(index))
        en_phonenumber.delete(0, tk.END)
        en_phonenumber.insert(0, phone_dict[lstbox_phone.get(index)])

def generate_phone_lst(filter=None):
    rs_lst = []
    lstbox_phone.delete(0, tk.END)
    if filter is None:
        rs_lst = [x for x in phone_dict]
    else:
        rs_lst = [x for x in phone_dict if filter in x]
    for el in rs_lst:
        lstbox_phone.insert(tk.END, el)
    if len(rs_lst) > 0:
        lstbox_phone.select_set(0)
        lstbox_phone.event_generate("<<ListboxSelect>>")

def search():
    name = en_name.get()
    generate_phone_lst(filter = name)

lbl_name = tk.Label(main_frame, text= "Name: ")
lbl_phonenumber = tk.Label(main_frame, text= "Phone: ")
lbl_message = tk.Label(main_frame, text= "Message: ")
en_name = tk.Entry(main_frame, name = 'en_name')
en_phonenumber = tk.Entry(main_frame, name="en_phonenumber")
btn_ad = tk.Button(main_frame, text="Add", command= add_phone)
btn_search = tk.Button(main_frame, text= 'Search', command= search)
lstbox_phone = tk.Listbox(main_frame)

lbl_name.grid( row=0, column=0)
lbl_phonenumber.grid( row=1, column=0)
lbl_message.grid(row= 4, column=0, columnspan= 2)
en_name.grid( row=0, column=1)
en_phonenumber.grid( row=1, column=1)
btn_ad.grid( row=2, column=0, columnspan=2)
btn_search.grid( row=3, column=0, columnspan=2)
lstbox_phone.grid( row=5, column= 1, columnspan=2)
lstbox_phone.bind('<<ListboxSelect>>',lstbox_phone_onselect)
generate_phone_lst()


main_window.mainloop()