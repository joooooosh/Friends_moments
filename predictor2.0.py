import numpy as np
import matplotlib.pyplot as plt


friends_tot = float(input("请输入好友总人数："))
like_rate = float(input("请输入动态内容吸引力（好友看见后点赞概率）（0~1间小数）"))
see_rate = float(input("好友打开朋友圈频率（一天打开朋友圈多少次）"))
tpoint = float(input("上传动态的时间点（输入小时数且为整数）（24小时制）"))
nightowl_rate = float(input("夜猫子在朋友中的占比（0点-6点看朋友圈的称为夜猫子)"))


friends_tot = int(like_rate * friends_tot + 0.5)
dayowl = int(friends_tot * (1-nightowl_rate))
nightowl = int(friends_tot - dayowl)


peoseerate1 = np.random.normal(loc=see_rate, scale=3, size=dayowl)
peoseerate2 = np.random.normal(loc=see_rate, scale=3, size=nightowl)


ftpday = 18 / peoseerate1
ftpday = ftpday+tpoint+0.5
ftpday = ftpday.astype(int)

ftpnight = 24 / peoseerate2
ftpnight = ftpnight+tpoint+0.5
ftpnight = ftpnight.astype(int)


for i in range(0, int(dayowl)):
    if ftpday[i] < tpoint:
        ftpday[i] = 100
        continue
    if 24 < ftpday[i] < 18+tpoint:
        ftpday[i] -= 18

for i in range(0, int(nightowl)):
    if ftpnight[i] < tpoint:
        ftpnight[i] = 100
        continue
    if 24 < ftpnight[i] < 24+tpoint:
        ftpnight[i] -= 24


ftp = np.hstack((ftpday, ftpnight))
ftp.sort()
x = np.arange(0, 25, 1)
y = [0 for i in range(25)]


for i in range(0, friends_tot):
    if ftp[i] < 0:
        continue
    if ftp[i] > 24:
        break
    y[ftp[i]] += 1

plt.plot(x, y)
plt.grid()
plt.show()
