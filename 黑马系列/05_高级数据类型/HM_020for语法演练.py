temp = ["战斗暴龙兽","天使兽","凤凰兽","亚古兽"]

for tep in temp:
    print(tep)

    if tep == "天使兽":
        break

else:
    # 如果循环体内部使用break退出了循环
    # else下方的代码就不会执行
    print("会执行吗")

print("循环结束")