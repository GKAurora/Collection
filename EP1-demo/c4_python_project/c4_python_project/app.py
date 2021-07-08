from flask import Flask
import requests
import json
import math
import time, datetime
from urllib import parse
from flask_cors import *
app = Flask(__name__)
CORS(app, supports_credentials=True)

# 获取token
@app.route('/get_token')
def get_token():
    # 获取token
    url = "https://117.78.31.209:26335/rest/plat/smapp/v1/oauth/token"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "grantType": "password",
        "userName": "",
        "value": ""
    }
    response = requests.put(url, headers=headers, data=json.dumps(data), verify=False)
    token = response.json()['accessSession']
    return token


# 热力图开发
@app.route('/heat_map')
def heat_map():
    #获取token
    token = get_token()
    # 拿到热力图
    url = "https://117.78.31.209:26335/rest/campusrtlswebsite/v1/clientlocation/heatmap"

    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": token,
        "Accept": "application/json",

    }
    url = url+"?startTime=1624323600000&endTime=1624327200000"
    res = requests.post(url, headers=headers, verify=False)
    data = res.json()['data']
    print(data)

    # 处理data
    min_data = 10000
    max_data = 0
    for d in data:
        if min_data > d['count']:
            min_data = d['count']

        if max_data < d['count']:
            max_data = d['count']

    print(min_data, max_data)
    error = max_data - min_data
    for d in data:
        d['value'] = math.floor(d['count'] / error * 50)
        d.pop('count')

    print(data)
    return json.dumps(data)


# 终端位置
@app.route("/location")
def terminal_location():
    url = "https://117.78.31.209:26335/rest/campusrtlswebsite/v1/clientlocation/lastlocation"
    token = get_token()
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": token,
        "Accept": "application/json"
    }
    data = {
        "id": "540d8574-a743-4cda-a47e-3718b6a4f722",
        "level": 3,
        "type": "floor"
    }
    url = url + "?param="+parse.quote(json.dumps(data))
    res = requests.post(url, headers=headers, verify=False)
    print(res.json())
    return res.json()


# AP位置
@app.route("/topo_info")
def topo_info():
    url = "https://117.78.31.209:26335/rest/campuswlantopowebsite/v1/wlantopo/topoinfo"
    token = get_token()
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": token,
        "Accept": "application/json"
    }
    data = {
        "id": "540d8574-a743-4cda-a47e-3718b6a4f722",
        "level": 3,
        "type": "floor"
    }
    url = url + "?param="+parse.quote(json.dumps(data))
    res = requests.get(url, headers=headers, verify=False)
    print(res.json())
    return res.json()


# 质量评估体系多维度数据汇总
@app.route("/multi_dimension")
def multi_dimension():
    url = "https://117.78.31.209:26335/rest/campuswlanqualityservice/v1/expmonitor/overview/rate"
    token = get_token()
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": token,
        "Accept": "application/json"
    }
    begintime = int(time.time() * 1000) - 1000 * 60 * 60
    endtime = int(time.time() * 1000)
    data = {
        "id": "857b706e-67d9-49c0-b3cd-4bd1e6963c07", # 深圳站点举例
        "level": 1,
        "regionType": "site",
        "startTime": str(begintime),
        "endTime": str(endtime),
    }
    url = url + "?param="+parse.quote(json.dumps(data))
    res = requests.get(url, headers=headers, verify=False)
    print(res.json())
    return res.json()


# 健康度趋势数据汇总
@app.route("/health_trend")
def health_trend():
    url = "https://117.78.31.209:26335/rest/campuswlanqualityservice/v1/expmonitor/rate/basictable"
    token = get_token()
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": token,
        "Accept": "application/json"
    }
    begintime = int(time.time() * 1000) - 1000 * 60 * 60
    endtime = int(time.time() * 1000)
    data = {
        "id": "857b706e-67d9-49c0-b3cd-4bd1e6963c07", # 深圳站点举例
        "level": 1,
        "regionType": "site",
        "startTime": str(begintime),
        "endTime": str(endtime),
    }
    url = url + "?param="+parse.quote(json.dumps(data))
    res = requests.get(url, headers=headers, verify=False)
    print(res.json())
    return res.json()


# 单个维度数据
@app.route("/single_dimension")
def single_dimension():
    url = "https://117.78.31.209:26335/rest/campuswlanqualityservice/v1/expmonitor/common/basic"
    token = get_token()
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": token,
        "Accept": "application/json"
    }
    begintime = int(time.time() * 1000) - 1000 * 60 * 60
    endtime = int(time.time() * 1000)
    data = {
        "id": "857b706e-67d9-49c0-b3cd-4bd1e6963c07", # 深圳站点举例
        "level": 1,
        "regionType": "site",
        "startTime": str(begintime),
        "endTime": str(endtime),
        "metricType": "coverage", #此参数支持六种参数：accessSuccessRate，accessConsume，roam， coverage，capacity，throughput
    }
    url = url + "?param="+parse.quote(json.dumps(data))
    res = requests.get(url, headers=headers, verify=False)
    print(res.json())
    return res.json()


# 单个维度数据趋势
@app.route("/single_dimension_rate")
def single_dimension_rate():
    url = "https://117.78.31.209:26335/rest/campuswlanqualityservice/v1/expmonitor/common/trend"
    token = get_token()
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": token,
        "Accept": "application/json"
    }
    begintime = int(time.time() * 1000) - 1000 * 60 * 60
    endtime = int(time.time() * 1000)
    data = {
        "id": "857b706e-67d9-49c0-b3cd-4bd1e6963c07", # 深圳站点举例
        "level": 1,
        "regionType": "site",
        "startTime": str(begintime),
        "endTime": str(endtime),
        "metricType": "coverage", #此参数支持六种参数：accessSuccessRate，accessConsume，roam， coverage，capacity，throughput
    }
    url = url + "?param="+parse.quote(json.dumps(data))
    res = requests.get(url, headers=headers, verify=False)
    print(res.json())
    return res.json()


# 用户列表
@app.route("/userlist")
def userlist():
    url = "https://117.78.31.209:26335/rest/campusclientservice/v1/event/userlist"
    token = get_token()
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": token,
        "Accept": "application/json"
    }
    begintime = int(time.time() * 1000) - 1000 * 60 * 60
    endtime = int(time.time() * 1000)
    data = {
        "filter":{
            "operate": "=",
            "value": 0,
            "key": "accType"

        },
        "level": "1",
        "tenantId": "default-organization-id",
        "startTime": str(begintime),
        "endTime": str(endtime),
        "id": "857b706e-67d9-49c0-b3cd-4bd1e6963c07",
        "sortColumn": "totalcount",
        "currPage": "1",
        "pageSize": "100",
        "sortType": "desc"
    }
    res = requests.post(url, headers=headers,data=json.dumps(data),verify=False)
    print(res.json())
    return res.json()


# 用户数趋势
@app.route("/user_trend")
def user_trend():
    url = "https://117.78.31.209:26335/rest/campusclientservice/v1/clientoverview/userstatistics/trend"
    token = get_token()
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": token,
        "Accept": "application/json"
    }
    begintime = int(time.time() * 1000) - 1000 * 60 * 60
    endtime = int(time.time() * 1000)
    data = {
        "regionType": "site",
        "level": "1",
        "tenantId": "default-organization-id",
        "showType": "radio",
        "startTime": str(begintime),
        "id": "857b706e-67d9-49c0-b3cd-4bd1e6963c07",
        "endTime": str(endtime),
        "isAutoRefresh": "false"
    }

    url = url + "?param=" + parse.quote(json.dumps(data))
    res = requests.get(url, headers=headers, verify=False)
    print(res.json())
    return res.json()


# 用户接入失败数据
@app.route("/connect_trend")
def connect_trend():
    url = "https://117.78.31.209:26335/rest/campuswlanqualityservice/v1/connectivity/connect-trend"
    token = get_token()
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": token,
        "Accept": "application/json"
    }
    begintime = int(time.time() * 1000) - 1000 * 60 * 60
    endtime = int(time.time() * 1000)
    data = {"accType": 1,
            "id": "857b706e-67d9-49c0-b3cd-4bd1e6963c07",
            "regionType": "site",
            "level": 1,
            "tenantId": "default-organization-id",
            "startTime": begintime,
            "endTime": endtime,
            "dateFrom": begintime,
            "dateTo": endtime
            }

    url = url + "?param=" + parse.quote(json.dumps(data))
    res = requests.get(url, headers=headers, verify=False)
    print(res.json())
    return res.json()


# 质量评估体系区域排名
@app.route("/rank_rate")
def rank_rate():
    url = "https://117.78.31.209:26335/rest/campuswlanqualityservice/v1/expmonitor/rank/basictable"
    token = get_token()
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": token,
        "Accept": "application/json"
    }
    begintime = int(time.time() * 1000) - 1000 * 60 * 60
    endtime = int(time.time() * 1000)
    data = {
        "regionType": "site",
        "level": "0",
        "tenantId": "default-organization-id",
        "startTime": str(begintime),
        "id": "/",
        "endTime": str(endtime)
    }
    url = url + "?param=" + parse.quote(json.dumps(data))
    res = requests.get(url, headers=headers, verify=False)
    print(res.json())
    return res.json()


# 站点树
@app.route("/site_tree")
def site_tree():
    url = "https://117.78.31.209:26335/rest/uninetwork-res/v1/position/subtree"
    token = get_token()
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": token,
        "Accept": "application/json",
        "id": "6949a343-fbaa-4ff6-b98b-35c09a1dea66"
    }
    res = requests.get(url, headers=headers, verify=False)
    print(res.json())
    return res.json()


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8899", debug=True)