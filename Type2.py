__author__ = 'chris'


class TraitementType2 :

    def __init__(self,id,temps=0,lapse=0):
        self.start_time = temps
        self.elapsed_time = lapse
        self.user_id = id

    def getStartTime(self):
        return self.start_time

    def getElapsedTime(self):
        return self.elapsed_time

    def setElapsedTime(self,value):
        self.elapsed_time = value

    def getId(self):
        return self.user_id
