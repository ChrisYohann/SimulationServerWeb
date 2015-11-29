__author__ = 'chris'

import ArrivalProcess as exo1
import matplotlib.pyplot as plt


#Question 3
#Choisir un lambda pour lequel le syst`eme est stable et un lambda pour lequel le systeme est instable et
#tracer evolution du nombre de client connectes au serveur en fonction du temps.

test_stable = exo1.ArrivalProcess(20.0,0.1,5000)
test_instable = exo1.ArrivalProcess(30.0,0.1,5000)

data_stable = test_stable.test()[0]
data_instable = test_instable.test()[0]

histo1 = test_stable.test()[1]
histo2 = test_instable.test()[1]

x1,y1= data_stable.T
x2,y2= data_instable.T
fig, ax = plt.subplots(1,1)
ax.plot(x1,y1, 'b-')
ax.set_title("Stable Process")
fig2,ax2 = plt.subplots(1,1)
ax2.plot(x2,y2,'r-')
ax2.set_title("Unstable Process")
plt.show()


plt.hist(histo1, 25, alpha=0.5, label='stable')
plt.hist(histo2, 25, alpha=0.5, label='unstable')
plt.legend(loc='upper right')
plt.show()