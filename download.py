import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import input_data

mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)
