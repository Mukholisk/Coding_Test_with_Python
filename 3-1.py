jandon = [500, 100, 50, 10]
cnt = 0

money = int(input("money: "))

for i in jandon:
    cnt += money//i
    money %= i

print(cnt)