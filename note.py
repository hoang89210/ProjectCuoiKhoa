
# todo: App quản lí mật khẩu các website (mark)
# * đối tượng là user, mark

from pprint import pprint

user_lst = [
    {
        "username": "vinhbc1",
        "password": "123",
        "mark_lst": []
    },
    {
        "username": "vinhbc2",
        "password": "123",
        "mark_lst": []
    }
]


def is_user_exists(user_name):
    for el in user_lst:
        if el["username"] == user_name:
            return True
    return False

def dang_ky_user(username, password):
    # * kiểm tra có user có tồn tài chưa
    if is_user_exists(username):
        # * đưa ra hướng xử lí nếu user tồn tại
        # * ví dụ là nhập lại, thông báo, báo lỗi, ...
        print("đã tồn tại")
        return
    user = {
        "username" : username,
        "password" : password
    }
    print("tạo thành công")
    user_lst.append(user)

def xoa_user(username):
    if not is_user_exists(username):
        print("Không tìm thấy user")
        return
    index = 0
    for el in user_lst:
        if el["username"] == username:
            break
        index += 1
    user_lst.pop(index)
    pprint(user_lst)
    print("xoá thành công")

def update_user(username, password):
    if not is_user_exists(username):
        print("Không tìm thấy user")
        return
    for el in user_lst:
        if el["username"] == username:
            el['password'] = password
    print("Update thành công")
    pprint(user_lst)
    
def create_mark(website, website_password):
    return {
        "website" : website,  
        "website_password" : website_password
    }

def user_add_mark(username, mark):
    for user in user_lst:
        if user['username'] == username:
            user["mark_lst"].append(mark)
            pprint("add thành công")
            pprint(user_lst)
            return
    print("Không tìm thấy user")

def user_edit_mark(username, update_mark):
    for user in user_lst:
        if user.ussername == username:
            for mark in  user["mark_lst"]:
                if mark.website == update_mark.website:
                    mark.password = update_mark.password

def user_delete_mark(username, del_mark):
    for user in user_lst:
        if user.ussername == username:
            index = 0
            for mark in user["mark_lst"]:
                if mark.website == del_mark.website:
                    user["mark_lst"].pop(index)
                index += 1

# ! đăng ký user
# dang_ky_user("vinhbc","password")
# dang_ky_user("vinhbc1","password")

# ! xoá user
# xoa_user("vinhbc")
# xoa_user("vinhbc1")

# ! update user password
# update_user("vinhbc","new_password")
# update_user("vinhbc1","new_password")

# ! user add mark
# mark = create_mark("facebook.com","123")
# user_add_mark("vinhbc",mark)
# user_add_mark("vinhbc1",mark)

