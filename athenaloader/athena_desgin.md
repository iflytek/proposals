# AI推理服务框架开源版本v2设计(ASE OpenSource)


## 整体组件架构

如图: ![架构](athena.png)


注:

* Kong Nginx为推介组件,使用者可以根据自身需求更换合适的接入层网关

* 配置中心、LB为可选组件

* 根据部署方式不同[见下节],docker-compose 和 kuberentes方式 实际部署架构可能存在不同的组合方式: kubernetes方式可配置使用polaris配置中心，或者使用k8s/configmap


## 用户使用流程

![用户流程](usage.png)

## Schema设计讨论

目前有两大生成schema方案,讨论下首版本支持范围

1. 用户生成式

这里细分两种方案 单页面web配置、命令行基于yaml创建式 [见命令行详细设计](#命令行工具详细设计)

2. 代码生成式

融合用户API定义和插件编写2个步骤，根据代码自动生成schema

举例: 

* 先介绍下当前python wrapper代码基础格式:

[wrapper](wrapper/wrapper.py)

增加api定义后:
```python
'''
API定义,定义用户期望的api输入输出
asectl工具将扫描python此处BaseASEApi继承类生成openapi
'''
class Api(base.BaseASEApi):
	def request(self):
	    param1 = base.Arg("param1", int, "user param1", max=10, min=11, required=True )
	    param2 = base.Arg("param2", str, "user param2", required=True )
	    param3 = base.Arg("param3", str, "user param3", required=False )

    def response(self):
        param1 = base.Arg("param1", int, "user param1", max=10, min=11, required=True )
        param2 = base.Arg("param2", str, "user param2", required=True )
        param3 = base.Arg("param3", str, "user param3", required=False )

```

完整例子: [wrapper_new](wrapper/wrapper_new.py)

