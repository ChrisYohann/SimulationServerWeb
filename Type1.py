__author__ = 'chris'




class TraitementType1 :

    def __init__(self,id,temps=0):
        self.user_id = id
        self.start_time = temps
        self.elapsed_time = 0

    def getStartTime(self):
        return self.start_time

    def getElapsedTime(self):
        return self.elapsed_time

    def setStartTime(self,value):
        self.start_time = value

    def setElapsedTime(self,value):
        self.elapsed_time = value

    def getId(self):
        return self.user_id





