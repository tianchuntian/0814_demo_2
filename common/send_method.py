import requests
import json


class SendMethod:
    @staticmethod
    def send_method(url,data):
        """选择进入方式,将"""
        method_data = {"json":json.dumps(data)}
        res = requests.post(url=url,data=method_data)
        return res.json()
    @staticmethod
    def dict_2_json(res):
        """将结果进行json格式化输出"""
        return json.dumps(res,indent=2,ensure_ascii=False)

if __name__ == '__main__':
    url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin "
    data = {"name":"grj123456","password":"grj123456"}
    res = SendMetod.send_method(url, data)
    print(SendMetod.dict_2_json(res))