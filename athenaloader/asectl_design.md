# ASE 命令行工具设计 


## 功能点

为方便用户快速在ASE服务框架下开发部署新能力，推出 ***asectl*** 工具

工具包含功能点:
* 服务框架状态检查、基础pu

* 配置中心配置管理，(增删改查)
  - 配置集群crud
  - 区域crud
  - 服务crud
  - 服务版本crud

* Mock Run wrapper.py






* helm 安装完成后终端提示ase service的配置中心接口地址，ui地址

* 首次运行生成命令行工具所需配置,如输入配置中心地址


* 支持APISchema定义

* AI引擎相关功能: 启动AI引擎，AI引擎镜像构建, AI引擎本地仿真


### 命令行工具详细设计

**asectl**

#### init

调用 docker-compose 或者 helm install 初始化推理服务框架

#### api web

工具启动一个web页面[ase的API设计页面],监听本地口

![img_1.png](api_design.png)

页面保存后，可以生成或者提交 schema json到 配置中心

#### api create

执行 `asectl api create -f ai_api.yml`

```yaml
apiVersion: iflytek.com/v1alpha1
kind: ApiSchema
metadata:
  group: gas # 配置中心group
  region: dx # 配置中心区域
  serviceName: image-detect # 服务名
  projectName: guiderAllService # 配置项目名称
  version: "1.0.0" # 配置版本号
  configFilname: xxxx.json # 缺省值，默认根据kind 对应配置中心特定配置文件: 如webgate的配置文件
  creationTimestamp: null
  name: my-api-schema # 生成配置文件名
spec:
  request:
    paramters:
      properties:
        # 以下为用户自定义的请求参数，可根据需求定义修改
        vcn: 
          description: "a word that xxx"
          type: string
        speed:
          description: "a speed that xxx"
          type: integer
          format: int32
          minimum: 50
          maximum: 200000
        isauto:
          description: "boolean value"
          type: boolean
        someother:
          description: "a objcet key"
          properties:
            value1:
              type: string
            value2: 
              type: string
          type: object
      required:
        - vcn
        - someother
    payload:
      properties:
        audio1:
          compress: raw
          type: audio
          encoding: speex-wb
          format: plain
        text1:
          compress: raw
          type: text
          encoding: utf-8
          format: json
        image1:
          compress: raw
          type: base64
          format: jpg
          raw: string
        vedio1:
          type: vedio
          compress: raw
          format: ""
          raw: string
      required:
        - image1
  response:
    palyload:
      properties:
        audio1:
          type: audio
          encoding: speex-wb

```

执行完次命令后在当前目录/schemas下 生成一条schema.json 并提示是否推送到配置中心


#### config upload
配置推送

#### config edit
配置编辑

#### config list
配置列表

#### config 查看
配置查看


#### loader build
辅助构建加载器镜像

#### loader test
辅助测试加载器镜像运行测试用例

#### loader run
辅助运行1个加载器服务 并注册到推理服务框架，并生成api地址，api调用文档地址

### cluster status


#### setup

配置asectl 工具， 如配置中心地址，账户密码， 区域配置


