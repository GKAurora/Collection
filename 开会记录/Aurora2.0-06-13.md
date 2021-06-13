# 6月8号会议讨论

## 目前想法

### 设备信息展示
api: /controller/campus/v1/oamservice/device/alarm

#### 前端
##### 首页
api `/controller/campus/v1/performanceservice/basicperformance/device/{deviceId}`
1. 设备数量
2. 各种设备信息
   - cpu利用率
   - 上下行流量
   - 网络速率、上下行流量分析、设备连接终端数、单设备基本信息、总流量以及最近一次设备上报的终端连接数、CPU利用率、上行速率、下行速率、站点健康度、TOP N SSID流量和最近在线用户数
3. 各种状态信息

##### 页面一
1. 图纸
2. 设备信息
    - id
    - 设备状态
    - 高级等级
3. 鼠标悬浮显示详情
4. 多楼层


#### 页面三-流量概览
接口: 查询终端TopN应用流量
1. 图标展示流量信息

### 下发AP配置
api -> 站点内AP设备Nat日志上报开关
1. AP DHCP配置
2. AP SSID配置管理
3. PPSK帐号管理

前端表单
1. SSID
2. 网络类型
3. SSID状态
4. 限速
5. 128
6. SSID


## 计划安排

- 前端任务
  - 三个页面的开发

- 后端任务
  - 华为API接口请求
  - 完成前端相应接口

- 必要任务 - API接口文档浏览（***）、了解如何使用postman进行请求
- 每周任务汇报
- 下周六（19号）晚上开会 -- 会议内容： 任务汇报、api接口讨论、功能细分



