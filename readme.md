### thrift

基本步骤

1. 定义接口
2. 实现server
3. 实现client

#### IDL文件

thrift官方给了类似C++的IDL文件示例（文件后缀为`.thrift`），地址为[tutorial.thirt](https://raw.githubusercontent.com/apache/thrift/HEAD/tutorial/tutorial.thrift)

- 划分相应的命名空间
- 定义相关的数据类型
- 定义需要的函数

#### 实现匹配服务端 C++

```bash
thrift -r --gen cpp match.thrift
```

会自动生成`gen-cpp`代码其中，`xxx-skeleton.cpp`是**实现服务端接口的示例代码**

**编译服务端**

```bash
# 注意链接时应该加上-lthrift，链接系统库中的thrift动态链接库
g++ -o main main.cpp match_server/*.cpp -lthrift
```

#### 实现匹配客户端 Python

```bash
thrift -r --gen cpp match.thrift
```

会自动生成`gen-py`代码其中，`Match-remote`是**实现服务端接口的示例代码**，但这里是实现客户端因此用不上，官网给了客户端实现的例子[thrift-python-tutorial](https://thrift.apache.org/tutorial/py.html)





----

### PS：

#### 为什么Python通常`__name__  == "__main__"`处理

**区分脚本执行和模块导入**

- 每个 Python 模块都有一个内置变量 `__name__`，它表示模块的名字。

- 当你直接运行一个 Python 文件时，`__name__` 会被置为 `"__main__"`。

- 当这个文件被作为模块导入时，`__name__` 就是模块的名字，而不是 `"__main__"`。
