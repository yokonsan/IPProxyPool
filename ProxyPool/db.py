from pymongo import MongoClient, ASCENDING
from config import *


class MongodbClient(object):

	def __init__(self):
		self.name = NAME
		self.client = MongoClient(HOST, PORT)
		self.db = self.client.proxy

	def change_table(self, name):
		self.name = name

	def proxy_num(self):
		"""
		得到数据库中代理num最高的数
		"""
		if self.get_nums != 0:
			self.sort()
			datas = [i for i in self.db[self.name].find()]
			nums = []
			for data in datas:
				nums.append(data['num'])
			return max(nums)
		else:
			return 0

	def get(self, count):
		"""
		从数据库左侧拿到相应数量的代理
		"""
		if self.get_nums != 0:
			self.sort()
			datas = [i for i in self.db[self.name].find()][0:count]
			proxies = []
			for data in datas:
				proxies.append(data['proxy'])
			return [proxy for proxy in proxies]
		return None

	def put(self, proxy):
		"""
		放置代理到数据库
		"""
		num = self.proxy_num() + 1
		if self.db[self.name].find_one({'proxy': proxy}):
			self.delete(proxy)
			self.db[self.name].insert({'proxy': proxy, 'num': num})
		else:
			self.db[self.name].insert({'proxy': proxy, 'num': num})

	def pop(self):
		"""
		从数据库右侧拿到一个代理
		"""
		if self.get_nums != 0:
			self.sort()
			data = [i for i in self.db[self.name].find()][-1]
			proxy =  data['proxy'] if data != None else None
			# 取出来使用后就从池中移除
			self.delete(proxy)
			return proxy
		return None

	def delete(self, value):
		"""
		如果代理没有通过检查，就删除
		"""
		self.db[self.name].remove({'proxy': value})

	def sort(self):
		"""
		按num键的大小升序
		"""
		self.db[self.name].find().sort('num', ASCENDING)

	def clean(self):
		"""
		清空数据库
		"""
		self.client.drop_database('proxy')

	@property
	def get_nums(self):
		"""
		得到数据库代理总数
		"""
		return self.db[self.name].count()
