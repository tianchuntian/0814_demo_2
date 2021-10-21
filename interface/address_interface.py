from common.send_method import SendMethod
from interface.login import Login
from common.get_keyword import GetKeyword
from common.op_database import OpDatabase
"""
接口测试
"""
class Addresss(object) :
    @staticmethod
    def view_address(url,data):
        """查看收货地址"""
        return SendMethod.send_method(url=url,data=data)

    @staticmethod
    def add_address(url,data):
        """添加收货地址"""
        return SendMethod.send_method(url=url, data=data)

    @staticmethod
    def modify_address(url,data):
        """修改收货地址"""
        return SendMethod.send_method(url=url, data=data)

    @staticmethod
    def delete_address(url,data):
        """删除收货地址"""
        return SendMethod.send_method(url=url, data=data)

    @staticmethod
    def get_address_id(res):
        """获取收货地址id"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/list"
        data = {"session":res}
        response = Addresss.view_address(url,data)
        return GetKeyword.get_keyword(response,"id")

    @staticmethod
    def get_mysql_adddress_number():
        """获取数据库中收货地址的个数"""
        # 先登录,在查看,获取登录码session
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        login = Login(url)
        data = {"name": "李哈哈_5", "password": "123456"}
        response = login.get_session(data)
        # 获取uid
        user_id = GetKeyword.get_keyword(response,"uid")
        stu = OpDatabase()
        sql = f"select * from ecs_user_address where user_id = {user_id}"
        return len(stu.get_all(sql))

    @staticmethod
    def get_address_number(res):
        """获取当前收货地址的数量"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/list"
        data = {"session":res}
        # 获取结果的返回值
        response = Addresss.view_address(url,data)
        # 提取里面的地址个数
        return len(GetKeyword.get_keyword(response,keyword="data"))


if __name__ == '__main__':
    # 先登录,在查看,获取登录码session
    url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
    login = Login(url)
    data = {"name":"grj123456","password":"grj123456"}
    res = login.get_session(data)
    # 查看收货地址
    url1 = "http://ecshop.itsoso.cn/ECMobile/?url=/address/list"
    data = {"session":res}
    print(Addresss.view_address(url1, data))
    # # 添加收货地址
    # url1 = "http://ecshop.itsoso.cn/ECMobile/?url=/address/add"
    # data1 = {"address":{"default_address":0,"consignee":"小蒙","tel":"18582361927","zipcode":"656560","country":"1","city":"271","id":0,"email":"123@163.com","address":"天府新谷","province":"24","district":"2716","mobile":""},"session":res}
    # print(res)
    # print(Addresss.add_address(url=url1, data=data1))
    # # 修改收货地址
    # url1 = "http://ecshop.itsoso.cn/ECMobile/?url=/address/update"
    # data = {"address":{"default_address":0,"consignee":"user","tel":"1898976579464","zipcode":"621000","country":"4044","city":"0","id":0,"email":"98784564@qq.com","address":"sdfsdfsd","province":"0","district":"0","mobile":""},"address_id":"2515","session":res}
    # print(Addresss.modify_address(url=url1, data=data))
    # # 删除收货地址
    # url1 = "http://ecshop.itsoso.cn/ECMobile/?url=/address/delete"
    # data1 = {"address_id":"2017","session":res}
    # print(Addresss.delete_address(url=url1, data=data1))
    # # 获取收藏商品的数量
    # url1 = "http://ecshop.itsoso.cn/ECMobile/?url=/address/list"
    # data = {"session": res}
    # print(Addresss.get_address_id(url=url1, data=data))
    # # 查看当前地址个数
    # print(Addresss.get_address_number(res))
    # # 获取数据库中的地址个数
    # print(Addresss.get_mysql_adddress_number())
    # 获取当前地址的id
    print(Addresss.get_address_id(res))