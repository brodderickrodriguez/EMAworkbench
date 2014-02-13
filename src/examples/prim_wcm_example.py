'''
Created on Feb 13, 2014

This example demonstrates the use of PRIM. The dataset was generated
using the world container model (Tavasszy et al 2011; http://dx.doi.org/10.1016/j.jtrangeo.2011.05.005)

@author: jhkwakkel
'''
import numpy as np
import matplotlib.pyplot as plt

from analysis import prim
from expWorkbench import ema_logging, load_results
ema_logging.log_to_stderr(ema_logging.INFO);

default_flow = 2.178849944502783e7

def classify(outcomes):
    ooi = 'throughput Rotterdam'
    outcome = outcomes[ooi]
    outcome = outcome/default_flow
    
    classes = np.zeros(outcome.shape[0])
    classes[outcome<1] = 1
    return classes

results = load_results(r'./data/5000 runs WCM 64 bit.bz2')
prim_obj = prim.Prim(results, classify, mass_min=0.05, threshold=0.75)

# let's find a first box
box1 = prim_obj.find_box()

# let's analyze the peeling trajectory
box1.show_ppt()
box1.show_tradeoff()

box1.write_ppt_to_stdout()

# based on the peeling trajectory, we pick entry number 44
box1.select(44)

# show the resulting box
prim_obj.show_boxes()
prim_obj.write_boxes_to_stdout()

plt.show()