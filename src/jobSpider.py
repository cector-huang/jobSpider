#!/usr/bin/python
#encoding: utf-8
import requests
from openpyxl import Workbook

class connection():
	def __init__(self, lang_name, city):
		self.baseUrl = "http://www.lagou.com/job/positionAjax.json"
		self.lang_name = ""
		self.city = ""
	def post(self,page):
		header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0',
'Accept':'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding':'gzip, deflate',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Connection':'keep-alive',
'Host':'www.lagou.com'}
		body = {'first': true, 'pn': page, 'kd': self.lang_name}
		url = baseUrl + '?city=' + self.city + 'needAddtionalResult=false'
		print(url)
		json = requests.post(url, body, header)
		return json.json()

def get_json(jobInstance, page):
	json = jobInstance.post(page)
	list_con = json['content']['positionResult']['result']
	info_list = []
	for i in list_con:
		info = []
		info.append(i['companyShortName'])
		info.append(i['companyName'])
		info.append(i['salary'])
		info.append(i['city'])
		info.append(i['education'])
		info_list.append(info)
	
	return info_list

def main():
	lang_name = raw_input('职位名：')
	while lang_name == "":
		lang_name = raw_input("请重新输入职位信息：")
	city = ""
	while city == "":
		city == raw_input("请输入求职的城市信息：（default：成都）")
		if city == "":
			city = "成都"
	page = 1
	jobInstance = connection(lang_name, city)
	info_result = []
	while page < 10:
		info = get_json(jonInstance, page)
		info_result = info_result + info
		page += 1
	wb = Workbook()
	ws1 = wb.active()
	ws1.title = lang_name
	for row in info_result:
		ws1.append(row)
	wb.save('职位信息.xlsx')

if __name__ == '__main__':
	main()
