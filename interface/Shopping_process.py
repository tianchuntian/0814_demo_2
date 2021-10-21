from common.send_method import SendMethod
from common.get_keyword import GetKeyword
from interface.login import Login


class Shopping_Process:
    def setup(self):
        # 前置条件

        self.url = 'http://ecshop.itsoso.cn/ECMobile/'
        url_1 = self.url + '?url=/user/signin'
        data = {"name": "李哈哈_5", "password": "123456"}
        login_test = Login(url_1)
        res = login_test.login(data)

        self.uid = GetKeyword.get_keyword(res, 'uid')  # 获取 uid

        sid = GetKeyword.get_keyword(res, 'sid')  # 获取 sid

        self.part = {'uid': f'{self.uid}', 'sid': f'{sid}'}  # 简化

    # 搜索商品
    def Search_for_goods(self):
        url = self.url + '?url=/search'
        data = {"pagination": {"count": 6, "page": 1},
                "filter": {"keywords": "", "sort_by": "price_asc", "brand_id": "", "category_id": "3",
                           "price_range": {"price_min": 0, "price_max": 0}}}
        goods = SendMethod.send_method(url, data)
        succee = GetKeyword.get_keyword(goods, 'succeed')
        return succee
        # sql=(f'select * from ')

    # 选择商品
    def select_goods(self):
        url = self.url + '?url=/goods'
        data = {"goods_id": 84, "session": self.part}
        goods_lis = SendMethod.send_method(url, data)
        select = GetKeyword.get_keyword(goods_lis, 'id')

        return select

    # 添加到购物车
    def add_goods(self):
        url = self.url + '?url=/cart/create'
        data = {"spec": [], "session": self.part, "goods_id": 89, "number": 1}
        goods = SendMethod.send_method(url, data)

    # 添加购物的购物车清单(选)
    def cart_list(self):
        url = self.url + '?url=/cart/list'
        data = {"session": self.part}
        cart = SendMethod.send_method(url, data)
        cart_l = GetKeyword.get_keyword(cart, 'goods_list')
        return len(cart_l)

    #     print(cart_l)
    #     v=len(cart_l)
    #     v=v-1
    #     x=cart_l[1:v:]
    #     return x

    # 结算
    def settle_accounts(self):
        url = self.url + '?url=/flow/checkOrder '
        data = {"session": self.part}
        settle = SendMethod.send_method(url, data)  # '购物车中没有商品'
        # data_id=GetKeyword.get_keyword()

        # 确认订单

    def order_form(self):
        url = self.url + '?url=/flow/done'
        data = {"shipping_id": "6", "session": self.part, "pay_id": "4"}
        order = SendMethod.send_method(url, data)
        # order_l=GetKeyword.get_keyword(order)
        # print(order)
        return order

    # 添加地址
    def address(self):
        url = self.url + '?url=/address/add'
        data = {"address": {"default_address": 0, "consignee": "你好", "tel": "17721213232",
                            "zipcode": "610000", "country": "1", "city": "271", "id": 0,
                            "email": "12426@qq.com", "address": "天府新谷",
                            "province": "24", "district": "2716", "mobile": ""}, "session": self.part}
        addr = SendMethod.send_method(url, data)
        addr_l = GetKeyword.get_keyword(addr, 'succeed')
        return addr_l

        # 结算

    def Settle_accounts(self):
        try:
            url = self.url + '?url=/flow/checkOrder '
            data = {"session": self.part}
            settle = SendMethod.send_method(url, data)  # '购物车中没有商品'
            self.settle_l = GetKeyword.get_keyword(settle, 'order_di')


        except:
            return False

    # 确认订单
    def checkOrder(self):

        url = self.url + '?url=/flow/checkOrder'
        data = {"session": self.part}
        settle = SendMethod.send_method(url, data)
        settle_l = GetKeyword.get_keyword(settle, 'succeed')
        if settle_l == '1':
            return True
        else:
            return False

    # 提交订单
    def confirm_an_order(self):
        url = self.url + '?url=/flow/done'
        data = {"shipping_id": "6", "session": self.part, "pay_id": "5"}
        order = SendMethod.send_method(url, data)


if __name__ == '__main__':
    process = Shopping_Process()
    process.setup()
    process.Search_for_goods()
    process.select_goods()
    process.add_goods()
    process.settle_accounts()
    process.cart_list()
    process.order_form()
    process.checkOrder()
    process.address()
    process.Settle_accounts()
    process.confirm_an_order()
