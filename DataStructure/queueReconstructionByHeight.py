# Problem: https://leetcode.com/problems/queue-reconstruction-by-height/

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=itemgetter(1), reverse=False)
        
        res, temporary = list(), list()
        res.append(people[0])
        
        def rightshift(j, peo):
            temp = peo
            for i in range(j, len(res), 1):
                if i == len(res)-1:
                    t = res[i]
                    res[i] = temp
                    res.append(t)
                    break
                t = res[i]
                res[i] = temp
                temp = t
            
        def recons(array):
            for i in range(len(array)):
                front, h, count, dhukse = array[i][1], array[i][0], 0, False
                for j in range(len(res)):
                    if res[j][0] >= h:
                        count = count + 1
                        if count > front:
                            rightshift(j, array[i])
                            dhukse = True
                            break 
                            
                if count == front and not dhukse:
                    res.append(array[i])
                    dhukse = True
                    
                if not dhukse:temporary.append(array[i])
                        
        recons(people[1:])
        recons(temporary)
        return res