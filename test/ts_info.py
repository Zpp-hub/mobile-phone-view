# coding:utf-8
import json, unittest
import requests

class Test_api(unittest.TestCase):

    def setUp(self):
        self.host_url = "http://127.0.0.1:5000"
        print('Case Before')
        pass

    def tearDown(self):
        print('Case After')
        pass

    # 接口功能
    def test_get_detail(self):
        r = requests.get(self.host_url + '/api/info/zhe')
        print(r.headers)
        print(r.json())
        pass

if __name__ == '__main__':
    unittest.main()

