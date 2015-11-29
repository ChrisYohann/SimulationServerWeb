__author__ = 'chris'

import Type1
import Type2
import random as rd
import numpy as np
import matplotlib.pyplot as plt
import Queue as Q

#initialisation
file_arrivee = Q.PriorityQueue()


class ArrivalProcess :

    def __init__(self,lambd,rate_param,nb_users):
        self.lambd = lambd
        self.rate_param = rate_param
        self.nb_users = nb_users

    def test(self):
      #initialisation
        i = 0
        arrive_date = 0
        state = 0
        moyenne = 0


        while i<self.nb_users :
            t1 = Type1.TraitementType1(i,arrive_date)
            file_arrivee.put((arrive_date,t1))
            arrive_date += rd.expovariate(self.lambd/1000)
            print("Arrivee de l'utilisateur "+ str(i) +" : "+ str(arrive_date) + " ms")
            i+=1


      #simulation

        liste = list()

        while not file_arrivee.empty():
            event = file_arrivee.get()

          #print("Current Time : "+ '%6.3f' % current_time + "ms")
          #print("Utilisateurs connectes " + str(state))

            if isinstance(event[1],Type1.TraitementType1):
                state+=1
                request1 = np.random.uniform(0,30)
                event[1].setElapsedTime(request1+6)
                #print("Le temps de cette requete de Type 1 est de "+'%6.3f' % request1+" ms")
                print("Requete 1 de l'utilisateur "+ str(event[1].getId()) +" a t = " + str(event[1].getStartTime()))
                nextuser_request = request1+18+event[1].getStartTime()
                temps_ecoule = request1+18
                t2 = Type2.TraitementType2(event[1].getId(),nextuser_request,temps_ecoule)
                file_arrivee.put((request1+18+event[1].getStartTime(),t2))
            elif isinstance(event[1],Type2.TraitementType2) :
                print("Requete 2 de l'utilisateur "+ str(event[1].getId()) +" a t = " + str(event[1].getStartTime()))
                request2 = rd.expovariate(self.rate_param)
                event[1].setElapsedTime(event[1].getElapsedTime() + request2 + 6)
                elapsedtime = event[1].getElapsedTime()
                #print("Le temps de cette requete de Type 2 est de "+'%6.3f' % request2 +" ms")
                print("Temps de reponse pour l'utilisateur "+ str(event[1].getId()) + " : " + '%6.3f' %  + elapsedtime+ " ms")
                moyenne+= elapsedtime
                state-=1

            liste.append((event[0],state))

        print("Temps de reponse moyen :"+ str(moyenne/self.nb_users))

        data_in_array = np.array(liste)

        x,y = data_in_array.T
        #fig, ax = plt.subplots(1,1)
        #ax.set_ylim(0,20)
        #ax.plot(x, y, 'b-')
        #plt.show()

        return(data_in_array)






