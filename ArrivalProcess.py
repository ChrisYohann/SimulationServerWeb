__author__ = 'chris'

import Type1
import Type2
import random as rd
import numpy as np
import Queue as Q
import scipy as sp
import scipy.stats
from math import pow
from math import sqrt
from math import floor



class ArrivalProcess :
    #initialisation
    file_arrivee = Q.PriorityQueue()

    def __init__(self,lambd,rate_param,nb_users):
        self.lambd = lambd
        self.rate_param = rate_param
        self.nb_users = nb_users

    def remove_with_id(self,array,id):
        for i, (identifiant, date_arrivee) in enumerate(array):
            if identifiant == id:
                del array[i]
                break
        return

    def already_connected(self,array,current_time):
        date_file = 0
        connected_users = 0
        i = 0
        while date_file < current_time and i < len(array) :
            date_file = array[i][1]
            if date_file < current_time :
                connected_users += 1
            i+=1
        return connected_users

    def mean_confidence_interval(data, confidence=0.95):
        a = 1.0*np.array(data)
        n = len(a)
        m, se = np.mean(a), scipy.stats.sem(a)
        h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
        return m, m-h, m+h



    def test(self,law=None,mode=1,shape=1):
      #initialisation
        i = 0
        arrive_date = 0
        state = 0
        moyenne = 0
        moyenne2 = 0
        vrai_moyenne = 0
        mediane = 0
        ecart_type = 0
        intervalle_68  = 0
        intervalle_95  = 0
        intervalle_997  = 0
        current_time = 0
        liste_user = list()
        liste_mediane = list()


        while i<self.nb_users :
            t1 = Type1.TraitementType1(i,arrive_date)
            liste_user.append((i,arrive_date))
            self.file_arrivee.put((arrive_date,t1))
            #print("Arrivee de l'utilisateur "+ str(i) +" : "+ str(arrive_date) + " ms")
            arrive_date += rd.expovariate(1/self.lambd)
            i+=1

      #simulation

        liste = list()
        liste_response = list()

        while not self.file_arrivee.empty():
            event = self.file_arrivee.get()

            #print("Current Time : "+ '%6.3f' % current_time + "ms")
            state = self.already_connected(liste_user,current_time)
            #print(str(state)+ " utilisateurs connectes ")
            #print("Utilisateurs connectes " + str(state))

            if isinstance(event[1],Type1.TraitementType1):
                if current_time < event[1].getStartTime() :
                    waiting_time = 0
                    current_time = event[1].getStartTime()
                else :
                    waiting_time = current_time - event[1].getStartTime()

                #state+=1
                request1 = np.random.uniform(0,30)
                event[1].setElapsedTime(request1+6)
                #print("Requete 1 de l'utilisateur "+ str(event[1].getId()) +" a t = "+ '%6.3f' % current_time + " ms. L'utilisateur a attendu " +'%6.3f' % waiting_time +" ms")
                #print("Le temps de cette requete de Type 1 est de "+'%6.3f' % request1 +" ms")
                nextuser_request = request1+18+event[1].getStartTime()
                current_time += request1 + 12
                temps_ecoule = request1+18+waiting_time
                t2 = Type2.TraitementType2(event[1].getId(),nextuser_request,temps_ecoule)
                self.file_arrivee.put((request1+18+event[1].getStartTime(),t2))


            elif isinstance(event[1],Type2.TraitementType2) :
                if current_time < event[1].getStartTime() :
                    waiting_time = 0
                    current_time = event[1].getStartTime()
                else :
                    waiting_time = current_time - event[1].getStartTime()

                #print("Requete 2 de l'utilisateur "+ str(event[1].getId()) +" a t = " + str(event[1].getStartTime()) + " ms. L'utilisateur a attendu " +'%6.3f' % waiting_time +" ms")
                if law == "pareto" :
                    request2 = (np.random.pareto(shape) + 1) * mode
                else :
                    request2 = rd.expovariate(self.rate_param)


                event[1].setElapsedTime(event[1].getElapsedTime() + request2 + 6 + waiting_time)
                elapsedtime = event[1].getElapsedTime()
                #print("Le temps de cette requete de Type 2 est de "+'%6.3f' % request2 +" ms")
                #print("Temps de reponse pour l'utilisateur "+ str(event[1].getId()) + " : " + '%6.3f' %  + elapsedtime+ " ms")
                current_time += request2 + 12
                moyenne+= elapsedtime
                liste_mediane.append(elapsedtime)
                moyenne2 += pow(elapsedtime,2)
                self.remove_with_id(liste_user,event[1].getId())
                #state-=1
                liste_response.append(elapsedtime)
                vrai_moyenne = moyenne/self.nb_users
                ecart_type = sqrt( (moyenne2/self.nb_users) - pow(vrai_moyenne,2) )
                intervalle_68 = ecart_type/sqrt(self.nb_users)
                intervalle_95 = 2*ecart_type/sqrt(self.nb_users)
                intervalle_997 = 3* ecart_type/sqrt(self.nb_users)

            liste.append((event[0],state))

        print("Temps de reponse moyen avec lambda = "+str(self.lambd)+" : "+ str(vrai_moyenne) + " ms." )
       #print("Ecart-type avec lambda = "+str(self.lambd)+" : "+ str(ecart_type)  )
        print("Intervalle a 68  : " + str([vrai_moyenne-intervalle_68 , vrai_moyenne + intervalle_68]))
        print("Intervalle a 95  : " + str([vrai_moyenne -intervalle_95 , vrai_moyenne + intervalle_95]))
        print("Intervalle a  99.7  : " + str([vrai_moyenne - intervalle_997 , vrai_moyenne + intervalle_997]))
        liste_mediane.sort()
        if self.nb_users%2 == 1 :
            mediane = liste_mediane[floor(self.nb_users/2)]
        else :
            mediane = (liste_mediane[self.nb_users/2] + liste_mediane[(self.nb_users+1)/2])

        print ("La mediane vaut : " + str(mediane))
        print( "------------------------------------------------------------------------------------------")


        data_in_array = np.array(liste)
        response_in_array = np.array(liste_response)

        return(data_in_array,response_in_array)










