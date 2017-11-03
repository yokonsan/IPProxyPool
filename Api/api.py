from flask import Flask, g

from ProxyPool.db import MongodbClient


app = Flask(__name__)

def get_conn():
	"""
	链接Mongodb
	"""
	if not hasattr(g, 'mongodb_conn'):
		g.mongodb_conn = MongodbClient()
	return g.mongodb_conn

@app.route('/')
def index():
	"""
	index html
	"""
	return '<h1>IP Proxy Pool</h1>' + '\n' \
		+ '<h3>/get: Get a proxy from proxy pool;</h3>' + '\n' \
		+ '<h3>/count: Get number of proxies</h3>'

@app.route('/get')
def get_proxy():
	"""
	拿到一个代理
	"""
	conn = get_conn()
	return conn.pop()

@app.route('/count')
def count():
	"""
	代理总数
	"""
	conn = get_conn()
	return str(conn.get_nums)

