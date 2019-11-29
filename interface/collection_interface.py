from common.send_method import SendMethod
from interface.login import Login
from common.get_keyword import GetKeyword
from common.op_database import OpDatabase

class Collection(object):
    @staticmethod
    def view_collection(url,data):
        """查看收藏"""
        return SendMethod.send_method(url=url,data=data)

    @staticmethod
    def add_collection(url,data):
        """添加收藏"""
        return SendMethod.send_method(url=url,data=data)

    @staticmethod
    def delete_collectioin(url,data):
        """移除收藏"""
        return SendMethod.send_method(url=url, data=data)

    @staticmethod
    def get_rec_id(res):
        """获取收藏里面的商品rec_id"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/list"
        data = {"session": res, "pagination": {"count": 10, "page": 1}, "rec_id": 0}
        res = Collection.view_collection(url=url,data=data)
        return GetKeyword.get_keyword(res,keyword="rec_id")

    @staticmethod
    def get_goods_number(res):
        """获取收藏夹中的商品个数"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/list"
        data = {"session": res, "pagination": {"count": 10, "page": 1}, "rec_id": 0}
        res = Collection.view_collection(url=url,data=data)
        return len(GetKeyword.get_keywords(res,keyword="data"))

    @staticmethod
    def mysql_goods_number():
        """获取数据库的商品种类"""
        # 先登录,在查看,获取登录码session
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        login = Login(url)
        data = {"name": "李哈哈_5", "password": "123456"}
        response = login.get_session(data)
        # 获取uid
        user_id = GetKeyword.get_keyword(response,"uid")
        stu = OpDatabase()
        sql = f"select * from ecs_collect_goods where user_id = {user_id}"
        return len(stu.get_all(sql))

if __name__ == '__main__':
    # 先登录,在查看,获取登录码session
    url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
    login = Login(url)
    data = {"name": "李哈哈_5","password": "123456"}
    res = login.get_session(data)
    # # 创建对象,准备获取收藏列表
    # url1 = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/list"
    # data = {"session":res,"pagination":{"count":10,"page":1},"rec_id":0}
    # print(Collection.view_collection(url1,data))
    # # 添加收藏
    # url2 = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/create"
    # # print(res)
    # data1 = {"session":res,"goods_id":81}
    # print(Collection.add_collection(url=url2,data=data1))
    # 移除收藏
    # url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/delete"
    # data = {'session':res,'rec_id':'2608'}
    # print(Collection.delete_collectioin(url, data))
    # 获取商品id
    # url1 = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/list"
    # data = {"session":res,"pagination":{"count":10,"page":1},"rec_id":0}
    # keyword = 'goods_id'
    # print(Collection.get_goods_id(url=url1, data=data, keyword=keyword))
    # # 获取收藏中所有商品个数
    # url1 = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/list"
    # data1 = {"session":res,"pagination":{"count":10,"page":1},"rec_id":0}
    # print(Collection.get_goods_number(url1,data1))
    # # 获取rec_id
    # print(Collection.get_rec_id(res))
    # # 获取商品种类
    # print(Collection.get_goods_number(res))