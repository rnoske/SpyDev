# -*- coding: utf-8 -*-

import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

######################################
# Setting up test data
def norm(x, mean, sd):
  norm = []
  for i in range(x.size):
    norm += [1.0/(sd*np.sqrt(2*np.pi))*np.exp(-(x[i] - mean)**2/(2*sd**2))]
  return np.array(norm)

mean1, mean2 = 0, -2
std1, std2 = 0.5, 1 

x = np.linspace(-20, 20, 500)
y_real = norm(x, mean1, std1) + norm(x, mean2, std2)

######################################

def gauss(x, mean, sd):
  norm = []
  for i in range(x.size):
    norm += [1.0/(sd*np.sqrt(2*np.pi))*np.exp(-(x[i] - mean)**2/(2*sd**2))]
  return np.array(norm)
  
def multiGaussFit(x, y, n, m, s):
    """ Fit n Gauss functions do data
    
    x (np.array): numpy array with x-axis
    y (np.array): numpy array with data
    n (int): number of Gauss functions to fit
    m (np.array): m[0]= initial mean value for first gauss
                m[n]= differenzes to mean before    
    s (np.array): array of standard deviations
    
    """    
    # Initial fit
    y_init = gauss(x, m[0], s[0])
    for i in xrange(1, n):
        y_init += gauss(x, m[i]+m[i-1], s[i])
            
    def res(p, y, x):
        #initialisation of paramters
        m = []
        s = []
        for i in xrange(n):
            m.append(p[i])
            s.append(p[i+n])
        absm = []
        for i in xrange(n):
            if i == 0:
                absm.append(m[i])
            elif i >= 1:
                absm.append(m[i] + m[i-1])
        #generation fit function
        y_fit = gauss(x, absm[0], s[0])
        for i in xrange(1,n):
            y_fit += gauss(x, absm[i], s[i]) 
        err = y - y_fit
        return err
    #parameter magic
    p = []
    for item in m:
        p.append(item)
    for item in s:
        p.append(item)
    p = np.array(p)
    param, success = leastsq(res, p, args = (y, x))
    #print param
    
    #result function
    y_est = gauss(x, param[0], param[2]) + gauss(x, param[1], param[3])
    
    #plotting
    plt.plot(x, y_real, label='Real Data')
    plt.plot(x, y_init, 'r.', label='Starting Guess')
    plt.plot(x, y_est, 'g.', label='Fitted')
    plt.legend()
    plt.show()

def beispiel():
    # Solving
    m, dm, sd1, sd2 = [5, 10, 1, 1]
    p = [m, dm, sd1, sd2] # Initial guesses for leastsq
    y_init = norm(x, m, sd1) + norm(x, m + dm, sd2) # For final comparison plot
    
    def res(p, y, x):
      m, dm, sd1, sd2 = p
      m1 = m
      m2 = m1 + dm
      y_fit = norm(x, m1, sd1) + norm(x, m2, sd2)
      err = y - y_fit
      return err
    
    plsq = leastsq(res, p, args = (y_real, x))
    print plsq
    
    y_est = norm(x, plsq[0][0], plsq[0][2]) + norm(x, plsq[0][1], plsq[0][3])
    
    plt.plot(x, y_real, label='Real Data')
    plt.plot(x, y_init, 'r.', label='Starting Guess')
    plt.plot(x, y_est, 'g.', label='Fitted')
    plt.legend()
    plt.show()

#beispiel()
n = 2
m = [5., 5.]
s = [1, 1]
multiGaussFit(x, y_real, n, m, s)