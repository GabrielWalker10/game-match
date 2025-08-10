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

### 步骤

#### 1. 实现匹配服务端 C++

```bash
thrift -r --gen cpp match.thrift
```

会自动生成`gen-cpp`代码其中，`xxx-skeleton.cpp`是**实现服务端接口的示例代码**

**编译服务端**

```bash
# 注意链接时应该加上-lthrift，链接系统库中的thrift动态链接库
g++ -o main main.cpp match_server/*.cpp -lthrift
```

#### 2. 实现匹配客户端 Python

```bash
thrift -r --gen cpp match.thrift
```

会自动生成`gen-py`代码其中，`Match-remote`是**实现服务端接口的示例代码**，但这里是实现客户端因此用不上，官网给了客户端实现的例子[thrift-python-tutorial](https://thrift.apache.org/tutorial/py.html)

#### 3. 改进匹配服务端 V2.0

实现利用互斥锁和一般队列包装成消息队列通信，实现简单的生成者-消费者模型，其中`unique_lock`和条件变量`condition_variable`实现PV操作。

现在并没有涉及到数据库，只是将数据存储在内存中管理，并且匹配模式简单，用户池中相邻两个用户匹配，匹配后从池子中删除。

#### 4. 实现数据保存客户端

官方C++客户端和服务端的样例，见[thrift-cpp-tutorial](https://thrift.apache.org/tutorial/cpp.html)

#### 5. 改进匹配服务端 V3.0

改进匹配方式，现在为分差匹配，当池子中某两个用户分差50以内，匹配成功

#### 6. 改进匹配服务端 V4.0 

引入**多线程**实现的服务端，现在生产者-消费者模型的服务端是多线程，并且条件变量保证线程安全

官方给的服务器例子就是多线程的，对照修改代码即可，见[thrift-cpp-tutorial](https://thrift.apache.org/tutorial/cpp.html)的Server一条

#### 7. 改进匹配服务端 V5.0 

修改业务逻辑，按照等待时间扩大匹配范围，符合现实生活中的匹配逻辑







----

### PS：

#### 为什么Python通常`__name__  == "__main__"`处理

**区分脚本执行和模块导入**

- 每个 Python 模块都有一个内置变量 `__name__`，它表示模块的名字。

- 当你直接运行一个 Python 文件时，`__name__` 会被置为 `"__main__"`。

- 当这个文件被作为模块导入时，`__name__` 就是模块的名字，而不是 `"__main__"`。

#### Linux上可以使用工具得到md5值

```bash
md5sum 123456
# 回车，再ctrl + d结束回车
```

md5值有单向的特点，用明文能得到唯一的密文，而从密文几乎不可能还原为明文

#### 关于git

**`git diff`命令**

```bash
# 查看工作区与暂存区对比
git diff

# 暂存区与上次提交（HEAD）对比
git diff --cached [文件名]
```

**git报错**

```bash
topeet@DESKTOP-J2H56AA ~/c/a/t/game-match (main)> git add readme.md
error: insufficient permission for adding an object to repository database .git/objects
error: readme.md: failed to insert into database
error: unable to index file 'readme.md'
fatal: updating files failed

# 可能是当前用户没有当前项目的所有权，可以修改
# 命令格式sudo chown [新所有者]:[新组] [文件/目录]
sudo chown -R topeet:topeet ./game-match/
```

