# 使用多个键值对，存储描述一个无题的相关信息————描述更复杂的数据信息
# 将多个字典放在一个列表中，在进行遍历
card_list = [
    {"name": "张三",
     "qq": "1253",
     "phone": "101456"},
    {"name": "李四",
     "qq": "1253212",
     "phone": "10142156"}
]

for card_info in card_list:

    print(card_info)