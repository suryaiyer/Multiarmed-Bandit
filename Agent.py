import numpy as np


class agent:

    def __init__(self, N, q = [] ,num = []):
    
        self.n = N
        
        if q == []:
            self.q = [0 for i in range(N)]
        
        elif len(q) != n:            
            raise ValueError("The length must be same as that of number of bandits")
        
        else:        
            self.q = q
            
        if num == []:            
            self.num = [1 for i in range(N)]
            
        elif len(num) != N:            
            raise ValueError("The length must be same as that of number of bandits")
        
        else:        
            self.num = num


    def get_action(self, eps = 0):
        
        p = np.random.choice( [1,0] , p = [1 - eps, eps])
        
        if p:
            
            a = np.argmax(self.q)
            
            
        else:
            
            a = np.random.choice(list(range(self.n)))
         
        self.num[a] += 1 
        
        return a

    def update_reward(self, r, action, alpha):
        
        self.q[action] += alpha * (r - self.q[action])
        
        return self
    
    def agent_state(self):
    
        return [self.q, self.num]
