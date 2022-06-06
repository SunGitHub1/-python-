num = int(input("请输入一个数字："))
i = 2
while i < num:
    if num % i == 0:
        print("%d不是素数"%num)
        break
    i += 1
else:
    print("%d是素数"%num)
