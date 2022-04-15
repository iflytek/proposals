

class Arg(object):
	# 定义 openapi schema需要的一些基础信息， base类
    def __init__(self, name, type ,description="", max=None,min=None,required=False):
        self.name = name
        self.type = type
        self.description = description
        self.max = max
        self.min = min
        self.required = required


class BaseASEApi(object):

	def gen():
	    # todo 生成schema
	    pass

    def request(self):
        raise NotImplementError

    def response(self):
		raise NotImplementError

