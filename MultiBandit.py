from numpy import random

class n_multi_bandit:
    """Multibandid Class which takes in n and the intial means and standard deviations"""

    def __init__(self, n, mean = [], std = []):
        
        self.n = n
        
        if mean == []:            
            self.mean = [0 for i in range(n)]
            
        elif len(mean) != n:            
            raise ValueError("The length of the means of distribution must be same as that of number of bandits")
        
        else:        
            self.mean = mean
            
        if std == []:            
            self.std = [1 for i in range(n)]
            
        elif len(std) != n:            
            raise ValueError("The length of the stdss of distribution must be same as that of number of bandits")
        
        else:        
            self.std = std
    
    
    def possible_actions(self): 
        
        """Returns list of possible actions"""
        
        return list(range(self.n))
    
    def reward(self, action):        
        
        """Returns reward for the action taken"""        
        
        return random.normal(loc = self.mean[action], scale = self.std[action])
        
    def update_mean(self, mu_upd = 0, std_upd = 0.01):
        """ Updates the means by using a normal distribution with specified means and std"""
        self.mean = [mu + random.normal(loc = mu_upd, scale = std_upd) for mu in self.mean]
        
        return self
                   
    def q_star(self):
        """ Returns the true environment"""
        
        return [self.mean, self.std]

