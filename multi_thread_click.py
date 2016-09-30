# -*- coding: utf-8 -*-
import multiprocessing
from multiprocessing import Pool

import time

def f(x):
    print 'start'
    print x
    #print y
    time.sleep(3)
    print 'end'

if __name__ == '__main__':
    p = Pool(64)
    print(p.map(f, range(10)))

