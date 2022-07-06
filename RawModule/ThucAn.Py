class Thit:
    __data = []
    def addmeat(self):
        print("thêm meat")
        infor = {
            'id' : '',
            'name' : '',
            'kcal': ''
        }
        print("Nhập ID meat:")
        id = input()
 
        while True:
            meat = self.findmeat(id)
            if meat != False:
                print("ID này đã tồn tại, vui lòng nhập lại:")
                id = input()
            else:
                break
 
        infor['id'] = id
        print("Nhập loại thịt:")
        infor['name'] = input()
        self.listmeat.append(infor)
 
 
    def findmeat(self, id):
        for i in range(0, len(self.listmeats)):
            if self.listmeats[i]['id'] == id:
                return [i, self.listmeats[i]]
        return False
 
    def deletemeat(self):
        print("xóa thịt")
        print("Nhập ID cần xóa:")
        id = input()
 
        meat = self.findmeat(id)
        if meat != False:
            self.listmeat.remove(meat[1])
            print("Xóa thành công")
        else :
            print("Không tìm thấy")

    def showmeat(self):
        print("list thịt")
        for i in range(0, len(self.list_)):
            print("[",self.listmeat[i]['id'],"]", "[",self.listmeat[i]['name'],"]","[",self.listmeat[i]['kcal'],"]")



 