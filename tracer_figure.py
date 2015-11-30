__author__ = 'chris'

import ArrivalProcess as exo1
import matplotlib.pyplot as plt


#Question 3
#Choisir un lambda pour lequel le syst`eme est stable et un lambda pour lequel le systeme est instable et
#tracer evolution du nombre de client connectes au serveur en fonction du temps.
print("--------------------Exponential Rate-----------------")

test_100 = exo1.ArrivalProcess(100.0,0.1,5000)
test_10 = exo1.ArrivalProcess(10.0,0.1,5000)
test_60 = exo1.ArrivalProcess(60.0,0.1,5000)
test_20 = exo1.ArrivalProcess(20.0,0.1,5000)
test_40 = exo1.ArrivalProcess(40.0,0.1,5000)

data_100,histo1 = test_100.test()
data_10,histo2 = test_10.test()
data_60,histo3 = test_60.test()
data_20 = test_20.test()[0]
data_40 = test_40.test()[0]


x100,y100= data_100.T
x10,y10= data_10.T
x60,y60 = data_60.T
x20,y20 = data_20.T
x40,y40 = data_40.T

fig, ax = plt.subplots(1,1)
ax.plot(x100,y100, 'b-')
ax.set_title("Stable Process : Lambda = 100")
fig2,ax2 = plt.subplots(1,1)
ax2.plot(x10,y10,'r-')
ax2.set_title("Unstable Process : Lambda = 10")
plt.ylabel("Clients connected")
plt.show()


fig, ax = plt.subplots(1,1)
ax.plot(x20,y20, 'b-',x40,y40,'r-',x60,y60,'g-')
ax.set_title("Lambda = 20,40 and 60")
plt.show()

#plt.hist(histo1, 25, alpha=0.5, label='stable')
#plt.hist(histo2, 25, alpha=0.5, label='unstable')
#plt.legend(loc='upper right')
#plt.show()
print("---------------------------Pareto--------------------------")


data_pareto_100,histo_pareto_1 = test_100.test("pareto",2,1.25)
data_pareto_10,histo_pareto_2 = test_10.test("pareto",2,1.25)
data_pareto_60 = test_60.test("pareto",2,1.25)[0]
data_pareto_20 = test_20.test("pareto",2,1.25)[0]
data_pareto_40 = test_40.test("pareto",2,1.25)[0]

xpareto100,ypareto100 = data_pareto_100.T
xpareto10,ypareto10 = data_pareto_10.T
xpareto60,ypareto60 = data_pareto_60.T
xpareto40,ypareto40 = data_pareto_40.T
xpareto20,ypareto20 = data_pareto_20.T

fig, ax = plt.subplots(1,1)
ax.plot(xpareto100,ypareto100, 'b-')
ax.set_title("Stable Pareto Process : Lambda = 100")
fig2,ax2 = plt.subplots(1,1)
ax2.plot(xpareto10,ypareto10,'r-')
ax2.set_title("Unstable Pareto Process : Lambda = 10")
plt.ylabel("Clients connected")
plt.show()


fig, ax = plt.subplots(1,1)
ax.plot(xpareto20,ypareto20, 'b-',xpareto40,ypareto40,'r-',xpareto60,ypareto60,'g-')
ax.set_title("Lambda = 20,40 and 60 for Pareto")
plt.show()

#plt.hist(histo_pareto_1, 25, alpha=0.5, label='stable')
#plt.hist(histo_pareto_2, 25, alpha=0.5, label='unstable')
#plt.legend(loc='upper right')
#plt.show()