
with open('results.csv','r') as f:
    lines = [x.split(',') for x in f.readlines()]

data = []
for line in lines:
    tmp = [x.strip() for x in line]
    data.append(tmp)


raw = []

for line in data:
    if line[-1] != 0 and line[-1] != '0':
        raw.append(float(line[-1]))


print "[*] Estimating probability of packetloss.."

lost = 0
for k in data:
    if k[1]=='0': lost+=1

print "{} packets sent, {} packets lost => P(packet lost) = {}".format(len(raw), lost, float(lost)/len(raw))





import numpy as np
import matplotlib.pyplot as plt

arr = np.array(raw)

h, X1 = np.histogram(arr, bins=100, normed=True)
dx = X1[1] - X1[0]
F1 = np.cumsum(h) * dx

plt.plot(X1[1:], F1)
plt.xlabel("Time / s")
plt.ylabel("P(x < X)")

plt.show()

