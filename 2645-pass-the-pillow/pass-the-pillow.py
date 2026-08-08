class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        

        def move(n , dirn ):
            if dirn == True :
                return n+1
            else :
                return n -1
        
        person = 1 
        timer = 0
        dirn = True
        while timer != time : 
            person = move (person,dirn)
            if person == n or person == 1 :
                dirn = not dirn 
            timer += 1
        return person  