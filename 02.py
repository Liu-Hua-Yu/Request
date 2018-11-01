import urllib
from urllib import request, parse

if __name__ == '__main__':
    url = "http://www.baidu.com/s?"

    # 输入搜索的问题
    wd = input("input you question:")
    # 使用字典构造问题
    qs = {
          "wd": wd
	}

    # 使用parse编码问题
    qs = parse.urlencode(qs)
    # 构造新的URL
    fullurl = url + qs
    # 获取新的请求对应的页面
    rsp = request.urlopen(fullurl)
    rsp = rsp.read()
    print(rsp.decode("utf-8"))