import numpy as np
import matplotlib.pyplot as plt
from program.exceptions import *

class trialInput(object):
    def __init__(self, positionList, num_trials):  
        if not isinstance(positionList, list):
            raise InvalidListError()
        else:
            denominations = [1000,100,10,1]
            for i in range(len(positionList)):
                if 1000/positionList[i] != denominations[i]:
                    raise PositionError()
        if not isinstance(num_trials, int):
            raise IntegerError() 
        
        self.positionList = positionList
        self.num_trials = num_trials
        
    def simulate(self):
        f = open('results.txt', 'w')
        for position in self.positionList:
            cumu_ret=np.zeros(self.num_trials)
            daily_ret=np.zeros(self.num_trials)
            for trial in range(self.num_trials):
                num_win=np.random.binomial(position,0.49)
                num_lost=position-num_win
                position_value=1000/position
                cumu_ret[trial]=(num_win*(1+1)+num_lost*(1-1))*position_value
                daily_ret[trial]=(cumu_ret[trial]/1000)-1
            plt.clf()
            plt.hist(daily_ret,100,range=[-1,1])
            plt.xlabel('Daily Returns')
            plt.title('Histogram of Daily Returns for position = ' + str(position))
            plt.savefig('histogram_'+'{:04d}'.format(position)+'_pos.pdf')
            mean_ret = np.mean(daily_ret)
            std_ret = np.std(daily_ret)
            f.write('mean of return for position ' + str(position) + ' : ' + str(mean_ret) + '\n')
            f.write('std of return for position ' + str(position) + ' : ' + str(std_ret) + '\n')
        f.close()