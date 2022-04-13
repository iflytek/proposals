# AI推理服务框架开源版本v2设计(ASE OpenSource)


## 整体组件架构

如图: ![架构](athena.png)


注:

* Kong Nginx为推介组件,使用者可以根据自身需求更换合适的接入层网关

* 配置中心、LB为可选组件

* 根据部署方式不同[见下节],docker-compose 和 kuberentes方式 实际部署架构可能存在不同的组合方式: kubernetes方式可配置使用polaris配置中心，或者使用k8s/configmap


## 命令行工具[asectl]设计


为方便用户快速搭建部署整个AI推理服务框架，推出 ***asectl*** 工具

工具包含功能点:

* AI服务框架部署初始化: 支持 *docker-compose* , kubernetes 部署

* AI服务框架组件配置、状态管理: 支持实时编辑各个组件需要配置，支持重启停各个组件, 支持各组件部署信息管理(如扩缩容某组件)

* AI能力管理: 支持新增AI能力，能力API设计， AI能力关联API(见详细设计), 能力的上下线

* AI引擎相关功能: 启动AI引擎，AI引擎镜像构建, AI引擎本地仿真



### 命令行工具详细设计
TDO



