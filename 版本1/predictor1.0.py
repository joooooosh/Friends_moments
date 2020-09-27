import numpy as np
import matplotlib.pyplot as plt


friend_tot = float(input("请输入好友总人数："))
like_rate = float(input("请输入动态内容吸引力（好友看见后点赞概率）（0~1间小数）"))
see_rate = float(input("好友打开朋友圈频率（一天打开朋友圈多少次）"))


friend_tot = int(like_rate * friend_tot + 0.5)
peoseerate = np.random.normal(loc=see_rate, scale=3, size=friend_tot)
ftp = 24 / peoseerate + 0.5
ftp = ftp.astype(int)
ftp.sort()


x = range(0, 25, 1)
y = [0 for i in range(25)]


for i in range(0, friend_tot):
    if ftp[i] < 0:
        continue
    elif ftp[i] > 24:
        break
    y[ftp[i]] += 1


plt.plot(x, y)
plt.show()
