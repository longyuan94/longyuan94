'''
格式化字符
%s 字符串
%d 有符号十进制整数，%06d表示输出的整数显示位数，不足的地方使用0补全
浮点数，%.2f表示小数点后只显示两位
%% 输出%

'''

# 定义字符串变量 name, 输出 我的名字叫 小明，请多多关照
name = "小明"
print("我的名字叫%s，请多关照！"%name)


# 定义整数变量 student_no, 输出我的学号是000001
student_no = 2
print("我的学号是%06d" % student_no)

# 定义小数 price、weight、money
# 输出苹果单价9.00元/斤，购买了5.00斤，需要支付4500元
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价%.2f元/斤，购买了%.3f斤，需要支付%.4f元" % (price,weight,money))

# 定义一个小数 scale，输出 数据比例是10.00%
scale = 0.25
print("数据比例是%f%%" % (scale * 100))