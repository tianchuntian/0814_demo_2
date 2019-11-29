from  common.send_method import SendMethod
from common.get_keyword import GetKeyword

class Goods_detail(object):
    @staticmethod
    def goods_view(url,data):
        return SendMethod.send_method(url,data)

if __name__=="__main__":
        from interface.login import Login

        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/user/signin'
        data = {"name": "李哈哈_5", "password": "123456"}
        res=str(Login(url).get_session(data))
