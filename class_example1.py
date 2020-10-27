class V(object):
    def __init__(self, beta, mu0, n, R):
        self.beta = beta
        self.mu0 = mu0
        self.n = n
        self.R = R

        #Thsi can be mentioned as below also.
        #self.beta, self.mu0, self.n, self.R = beta, mu0, n, R

    def value(self,r):
        beta, mu0, n, R = self.beta, self.mu0, self.n, self.R
        n = float(n) #for float division
        v = (beta/(2.0*mu0))**(1/n)*(n/(n+1))**(R**(1+1/n) - r**(1+1/n))
        return v


