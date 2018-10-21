
# 需要体现
# 1 报单，方向，价格
# 2 撤单
# 3 成交，数量。方向（index大小判断？）
# 4 最新价（和成交重合？）
# 5 对应的时间戳，一秒有多个成交和挂单，怎么处理？

import matplotlib.pyplot as plt
import sys


class LogProcessor:
    """Parse the log"""

    # x = 0
    # log_file = ""

    def __init__(self, filename):
        self.x = 0
        self.td = []
        self.od = []
        self.orders = {}
        self.log_file = filename

    def parse_td(self, line):
        fields = line.split(',')
        instrument = fields[0].split(':')[-1]
        time = fields[2]
        price = float(fields[3])
        volume = int(fields[4])
        buy_index = int(fields[7])
        sell_index = int(fields[8])
        function_code = fields[10]  # '70' trade, '52' cancel
        if function_code == '70':
            self.td.append((self.x, price, volume))
            self.x += 1
        elif function_code == '52':
            if buy_index == 0:
                index = sell_index
            else:
                index = buy_index
            self.orders[-1] = volume

    def parse_od(self, line):
        fields = line.split(',')
        instrument = fields[0].split(':')[-1]
        time = fields[2]
        price = float(fields[3])
        volume = int(fields[4])
        order_index = int(fields[6])
        order_kind = fields[7]   # ’1‘（49）表示市价单，’2‘（50）表示限价单，’U‘（85）表示本方最优
        function_code = fields[8]  # ’1‘（49）表示BUY，’2‘（50）表示SELL
        order = [self.x, price, volume, order_kind, function_code, 0]
        self.x += 1
        self.od.append(order)
        self.orders[order_index] = order

    # 解析log文件
    def parse_log(self):
        f = open(self.log_file)
        for line in f:
            if line.find('OD:') > 0:
                self.parse_od(line)
            elif line.find('TD:') > 0:
                self.parse_td(line)
        print('Orders:', len(self.od), 'Trades:', len(self.td))

    def plot(self):
        # plot orders
        for order in self.od:
            x = order[0]
            if order[4] == '49':
                y = order[2]
                c = 'r'
            else:
                y = -order[2]
                c = 'g'
            plt.vlines(x, 0, y, colors=c)

        # plot trades

        print('start to show')
        # show
        plt.show()


log_file = '000420.txt'
if len(sys.argv) >= 2:
    #print('Usage:', sys.argv[0], '<logfile>')
    #sys.exit(-1)
    log_file = sys.argv[1]

print('Parsing file', log_file)
processor = LogProcessor(log_file)
processor.parse_log()
processor.plot()
