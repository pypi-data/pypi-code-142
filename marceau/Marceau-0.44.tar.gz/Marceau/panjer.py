import numpy as np
import scipy.stats

class Cossette:
    def __init__(self,k=1,parameters=[],method='',h=1,fb=[],generator_param=[],generator_method=''):
        self.k=k
        self.parameters=parameters
        self.method=method
        self.h=h
        self.fb=fb
        self.generator_param=generator_param
        if generator_method=="Binomial":
            self.generator_method=scipy.stats.binom
        if generator_method=="NegBinomial":
            self.generator_method=scipy.stats.nbinom
        if generator_method=="Geometric":
            self.generator_method=scipy.stats.geom
        if generator_method=="Poisson":
            self.generator_method=scipy.stats.poisson
    def panjer(self):
        plist=[]
        if len(self.fb)==0:
            if len(self.generator_param)==2:
                self.fb=[self.generator_method.pmf(int(i*self.h),self.generator_param[0],self.generator_param[1]) for i in range(self.k+1)]
            else:
                self.fb=[self.generator_method.pmf(int(i*self.h),self.generator_param[0]) for i in range(self.k+1)]
        if self.method=='Binomial':
            n=self.parameters[0]
            p=self.parameters[1]
            a=p/(1-p)
            b=((n+1)*p)/(1-p)
            p0=((a-1)/((a*self.fb[0])-1))**((a+b)/a)
        if self.method=='Geometric':
            p=self.parameters[0]
            a=(1-p)
            b=0
            p0=(p/(1-self.fb[0]+(p*self.fb[0])))
        if self.method=='NegBinomial':
            r=self.parameters[0]
            q=self.parameters[1]
            a=(1-q)
            b=(r-1)*(1-q)
            p0=(q/(1-self.fb[0]+(q*self.fb[0])))**r
        if self.method=='Poisson':
            l=self.parameters[0]
            a=0
            b=l
            p0=np.exp((l*self.fb[0])-l)
        plist.append(p0)
        alpha=(1/(1-a*self.fb[0]))
        for i in range(1,self.k+1):
            temp=0
            for j in range(1,i+1):
                temp+=(a+b*j/i)*self.fb[j*self.h]*plist[(i-j)]
            pi=alpha*(temp)
            plist.append(pi)
        return(print(f'f({self.k}*{self.h})={plist[-1]} \nF({self.k}*{self.h})={np.sum(plist)}'))
    def help():
        string="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------Welcome to the Cossette and Marceau Panjer's Algorithm in Python---------------------------------------------------------------------------------------------------------------------------------------------------------\n\n In order to find fX and FX with Panjer's recursive method, please enter the argument as follow:\n\n k=3  (the epoch)\n\n h=1000 (the step, default value is 1) \n\n parameters=[2] (the parameters from X composed distribution) \n\n method='Binomial' (the method of the X composed distribution, note that only 4 method are available: method='Binomial' for a Binomial distribution, method='NegBinomial' for a Negative Binomial distribution, method='Geometric' for a Geometric distribution and method='Poisson' for a Poisson distribution) \n\n fb=[0.1,0.23...] (an list of size k+1, corresponding to the pmf of B positive random variable, default value is empty)\n\n generator_param=[10,0.4] (the parameter of the B distribution, only needed if B pmf fb is empty, default value is empty) \n\n generator_method='Binomial' (the method of the B distribution, note that only 4 method are available: generator_method='Binomial' for a Binomial distribution, generator_method='NegBinomial' for a Negative Binomial distribution, generator_method='Geometric' for a Geometric distribution and generator_method='Poisson' for a Poisson distribution) \n\n\n ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
        return((print(string)))
    def example():
        string1="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------Example 1-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\n If X follow a Poisson Composed distribution (lambda=2, FB) and B follow a Binomial distribution (10,0.4) \n\n We compute the following in order to find FX(k=10):\n model= Marceau.Cossette(k=10,parameters=[2],method='Poisson',generator_method='Binomial',generator_param=[10,0.4]) \n\n And then computing model.panjer() will return\n f(10*1)=0.05434563071580669 \n F(10*1)=0.6980136730471336 \n\n\n\n -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------Example 2-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\n If X follow a Poisson Composed distribution (lambda=1.25, FB) and B has the following pmf:\nfb=np.zeros(30*1000+1)\nfb[0]=0\nfb[1000]=0.2\nfb[2000]=0.3\nfb[3000]=0.2\nfb[4000]=0.15\nfb[5000]=0.1\nfb[6000]=0.05  \n\n We compute the following in order to find FX(h*k=1000*10)):\n model= Marceau.Cossette(k=10,h=1000,parameters=[1.25],method='Poisson',fb=fb) \n\n And then, computing model.panjer() will return\n f(10*1000)=0.02089842353538644 \n F(10*1000)=0.9536818666811318 "
        return((print(string1)))






















