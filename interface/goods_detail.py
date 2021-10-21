from common.send_method import SendMethod
from common.get_keyword import GetKeyword
from interface.login import Login
"""
接口测试
"""
class GoodsDetail(object) :
    def __init__(self,url):
        self.url = url
    def goods_detail(self,data):
        """商品详情"""
        return SendMethod.send_method(self.url,data)
    def get_succeed(self,data):
        """获取succeed,用做判断"""
        response = self.goods_detail(data)
        return GetKeyword.get_keyword(response,"succeed")


if __name__ == '__main__':
    # 先登录,获取session
    url1 = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
    logins = Login(url1)
    data = {"name":"grj123456","password":"grj123456"}
    res = logins.get_session(data)
    # # 商品详情
    # url = "http://ecshop.itsoso.cn/ECMobile/?url=/goods"
    # login = GoodsDetail(url)
    # data = {"goods_id":89,"session":res}
    # print(login.goods_detail(data))
    # 获取succeed
    url = "http://ecshop.itsoso.cn/ECMobile/?url=/goods"
    login = GoodsDetail(url)
    data = {"goods_id": 89, "session": res}
    print(login.get_succeed(data))