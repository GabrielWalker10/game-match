
# 将当前当前路劲加入Python的环境变量里，一般可以删除
# import sys
# import glob
# sys.path.append('gen-py')
# sys.path.insert(0, glob.glob('../../lib/py/build/lib*')[0])

from match_client.match import Match
from match_client.match.ttypes import User

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Match.Client(protocol) # 注意改名

    # Connect!
    transport.open()

    # 教程示例，简单测试了连接和函数调用
    # client.ping()
    # print('ping()')

    # sum_ = client.add(1, 1)
    # print('1+1=%d' % sum_)

    # work = Work()

    # work.op = Operation.DIVIDE
    # work.num1 = 1
    # work.num2 = 0

    # try:
    #     quotient = client.calculate(1, work)
    #     print('Whoa? You know how to divide by zero?')
    #     print('FYI the answer is %d' % quotient)
    # except InvalidOperation as e:
    #     print('InvalidOperation: %r' % e)

    # work.op = Operation.SUBTRACT
    # work.num1 = 15
    # work.num2 = 10

    # diff = client.calculate(1, work)
    # print('15-10=%d' % diff)

    # log = client.getStruct(1)
    # print('Check log: %s' % log.value)

    # 业务逻辑
    user = User(1, "zsy", 100)
    client.add_user(user, "add user")

    # Close!
    transport.close()

# 常见处理
if __name__ == "__main__":
    main()