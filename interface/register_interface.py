from common.send_method import SendMethod
from common.get_keyword import GetKeyword
from common import op_database

"""
接口测试
"""


class Register(object):
    """
    验证注册接口数据
    """

    def __init__(self, url):
        """
        初始化绑定类属性
        :param url:注册接口地址
        """
        self.url = url

    def register(self, data):
        """
        post请求注册并将返回值返回

        :return: 返回值
        """
        return SendMethod.send_method(self.url, data=data)

    def get_id(self, data):
        """
        注册并获取session中的uid值
        :return: uid值
        """
        res = SendMethod.send_method(self.url, data=data)
        # 取出uid的值并返回uid值
        return GetKeyword.get_keyword(res, "uid")


if __name__ == "__main__":
    url = 'http://ecshop.itsoso.cn/ECMobile/?url=/user/signup'
    data = {"field": [{"id": 5, "value": "17964112811"}], "email": "1515880269@qq.com", "name": "李哈哈_7",
            "password": "123456"}
    keyword = "uid"
    register_test = Register(url)
    res = register_test.register(data)
    print(res)
    # register_test = Register(url, data)
    # res=register_test.get_id(keyword)
    # print(res)
