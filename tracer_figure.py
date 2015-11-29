__author__ = 'chris'

import ArrivalProcess as exo1
import matplotlib.pyplot as plt

#Question 3
#Choisir un lambda pour lequel le syst`eme est stable et un lambda pour lequel le systeme est instable et
#tracer evolution du nombre de client connectes au serveur en fonction du temps.

test_stable = exo1.ArrivalProcess(70.0,0.1,5000)
test_instable = exo1.ArrivalProcess(10.0,0.1,5000)

data_stable = test_stable.test()
data_instable = test_instable.test()

x1,y1 = data_stable.T
x2,y2 = data_instable.T
fig, ax = plt.subplots(1,1)
ax.set_ylim(0,20)
ax.plot(x1, y1, 'b-',x2,y2,'r-')
plt.show()
