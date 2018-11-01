from urllib import request
import chardet
# 测试request库
# r = requests.get("http://www.baidu.com")
# print(r.status_code)
# print(r.text)

if __name__ == '__main__':

	url = "https://study.163.com/my"
	# 获取网页
	rsp = request.urlopen(url)

	print("URL: {}".format(rsp.geturl()))	# 响应的URL
	print("Info: {}".format(rsp.info()))	# 响应的Info
	print("Code: {}".format(rsp.getcode()))# 响应的状态

	# 显示返回结果
	html = rsp.read()
	# 获取返回类型为 bytes
	print(type(html))

	# 利用chardet自动获取网页编码格式
	cs = chardet.detect(html)
	# 网页解码
	# 使用get方法传递编码格式，保证不出错，（默认解码格式为utf-7）
	html = html.decode(cs.get("encoding", "utf-8"))
	# print(html)


