import unittest
from interface.register_interface import Register
from common.op_database import OpDatabase
from common.get_keyword import GetKeyword


class Test_regester(unittest.TestCase):
    def setUp(self) -> None:
        # 清空数据库中注册信息
        OpDatabase().clear_mysql()

    def test_re(self):
        """
        验证可否注册成功
        :return:
        """
        """
        验证注册接口数据
        """
        # 初始化绑定属性url,data
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/user/signup'
        data = {"field": [{"id": 5, "value": "17964112811"}], "email": "1515880269@qq.com", "name": "李哈哈_7",
                "password": "123456"}
        # 获取注册的用户名,用作预期结果
        name1 = GetKeyword.get_keyword(data, "name")
        # 发送请求地址与请求参数
        register_test = Register(url)
        # #取出返回值中的uid值
        # res = register_test.get_id(self.data)
        # 注册
        response = register_test.register(data)
        # #数据库中查询是否存在注册的user_id值
        # sql= f"select user_id from ecs_users where user_id like '{res}'"
        # #将数据库user_id值取出
        # res_sql=OpDatabase().get_one(sql)['user_id']
        # #将int转换str
        # res_sql=str(res_sql)
        # 获取返回值中的name
        name2 = GetKeyword.get_keyword(response, "name")
        # 断言返回值中的id值是否等于数据库中id值
        self.assertEqual(name1, name2)


if __name__ == "__main__":
    unittest.main()
