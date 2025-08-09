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

#### 实现服务端

```bash
thrift -r --gen cpp match.thrift
```

会自动生成`gen-cpp`代码其中，`xxx-skeleton.cpp`是**实现服务端接口的示例代码**

**编译服务端**

```bash
# 注意链接时应该加上-lthrift，链接系统库中的thrift动态链接库
g++ -o main main.cpp match_server/*.cpp -lthrift
```



