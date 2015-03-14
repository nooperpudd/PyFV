# -*- coding: utf-8 -*-
'''
.. codeauthor:: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
'''
__author__ = 'Hung-Hsin Chen'

import numpy as np

n_path=1000
T = 200
W =np.random.randn(n_path, T)
W2 = W*W
print W2.sum(axis=1).mean()