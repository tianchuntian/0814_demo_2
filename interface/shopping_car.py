from common.send_method import SendMethod
from common.get_keyword import GetKeyword
from interface.login import Login

class ShoppingCar(object) :
    def __init__(self,url):
        self.url = url
    def add_shopping_car(self,data):
        """添加购物车"""
        return SendMethod.send_method(self.url,data)

    def view_shopping_car(self,data):
        """查看购物车"""
        return SendMethod.send_method(self.url,data)

    def modify_shopping_car(self,data):
        """修改购物车"""
        return SendMethod.send_method(self.url,data)

    def delete_shopping_car(self,data):
        """删除购物车"""
        return SendMethod.send_method(self.url,data)

if __name__ == '__main__':
    # 先登录,获取session
    url1 = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
    logins = Login(url1)
    data = {"name": "grj123456", "password":"grj123456"}
    session = logins.get_session(data)
    # # 添加购物车
    url = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/create"
    login = ShoppingCar(url)
    data = {"spec":[],"session":session,"goods_id":89,"number":1}
    print(login.add_shopping_car(data))
    # 查看购物车(此处添加后却查看不到,BUG)
    # url = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/list"
    # login1 = ShoppingCar(url)
    # data = {"session":session}
    # res = login1.view_shopping_car(data)
    # rec_id = GetKeyword.get_keyword(res,"rec_id")
    # # 修改购物车(会返回商品信息)
    # url = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/update"
    # login2 = ShoppingCar(url)
    # data = {"new_number":3,"session":session,"rec_id":16470}
    # print(login2.modify_shopping_car(data))
    # 清空购物车(也会返回商品信息,删除不了数据)
    # url = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/delete"
    # login3 = ShoppingCar(url)
    # data = {"session":session,"rec_id":rec_id}
    # print(login3.delete_shopping_car(data))
