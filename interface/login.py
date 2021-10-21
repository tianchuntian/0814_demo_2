from common.send_method import SendMethod
from common.get_keyword import GetKeyword
"""
接口测试
"""
class Login(object):
    """
    登录接口
    """
    def __init__(self,url):
        """
        初始化绑定类属性
        :param url:登录接口地址
        """
        #请求地址
        self.url=url

    def login(self,data):
        """
        登录并将返回值返回
        :return:返回值
        """
        return SendMethod.send_method(url=self.url,data=data)

    def get_session(self,data):
        """
        获取登录中的session
         {
            "session": {
                            "sid": "09f46c876df50def205e2b34783852cadc7c67ed",
                             "uid": "9654"
        }

        :return: 返回session值
        """
        pass
        #res=SendMethod.send_method(url=self.url,data=data)
        res=self.login(data)
        #获取返回值中的session值
        return GetKeyword.get_keyword(res,'session')
    def get_name(self,data):
        """
        获取用户名字段
        :param data:
        :return:
        """
        res=self.login(data)
        #获取返回值中的name值
        return GetKeyword.get_keyword(res,'name')





if __name__=="__main__":
    url='http://ecshop.itsoso.cn/ECMobile/?url=/user/signin'
    data ={"name":"李哈哈_5","password":"123456"}
    login_test=Login(url)
    res=login_test.login(data)
    print(res)
    print("hahaha")
    res1=login_test.get_session(data)
    print(type(res1))
    print(res1)

