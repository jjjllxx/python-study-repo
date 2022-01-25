"""
File: huoqucookies.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-05-27 14:31:00
Function:


"""
import requests

r1 = requests.get('http://www.baidu.com')
print(r1.cookies)
for key, value in r1.cookies.items():
    print(key, '=', value)
headers1 = {'Host': 'www.jianshu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Cookies': 'GA1.2.2088694907.1582266582; __gads=ID=4d1bf6e65e472ea8:'
                       'T=1582266578:S=ALNI_Mb2gtZ7C1He0-PxW3gYcvqQT5cbSQ; __'
                       'yadk_uid=jv39gORk3tp0xQuhYNJuRMLemYf9aPIS; '
                       'web_login_version=MTU5MDQ5ODM2MQ%3D%3D--dd4df13443b6d3eb0ab1100abdce47199bf95935; '
                       'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2223557928%22%2C%22first_'
                       'id%22%3A%22170666fffab5e9-0e44064807fb11-36664c08-2073600-170666fffad488%22%2C%22'
                       'props%22%3A%7B%22%24latest_traffic_source_type'
                       '%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24'
                       'latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24'
                       'latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24'
                       'latest_utm_source%22%3A%22oschina-app%22%2C%22%24latest_referrer_host'
                       '%22%3A%22www.baidu.com%22%7D%2C%22%24device_'
                       'id%22%3A%22170666fffab5e9-0e44064807fb11-36664c08-2073600-170666fffad488%22%7D; '
                       'remember_user_token=W1syMzU1NzkyOF0sIiQyYSQxMSR1cXdBZVA5S0VkbmJFSS9aZFlOYm8u'
                       'IiwiMTU5MDU2MTI2OC4zNjgyNTMyIl0%3D--3ea6575a4dfd176896bf79f6f0ecc48ca2e8f9d4;'
                       ' read_mode=day; default_font=font2; locale=zh-CN;'
                       ' _m7e_session_core=81512717f187b3bde87d34696023aef2;'
                       ' Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1590498385,1590498394,1590498399,1590561271;'
                       ' Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1590561288'}
r2 = requests.get('https://www.jianshu.com', headers=headers1)
print(r2.text)
