import numpy as np


#values of single node network
inputs = np.array([2,1,4])
weights = np.array([4,6,2])
bias = -5

#defines and activated relu function
def relu(x):
  return np.maximum(0, x)

# Function to compute the output of a single neuron network
def single_neuron_network(weights, bias, inputs):
    #calculate neuron's output before activation
    output_before_activation = sum(w * x for w, x in zip(weights, inputs)) + bias

    #apply the relu function
    activated_output = relu(output_before_activation)

    #add the calculation step








