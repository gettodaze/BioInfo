
# coding: utf-8

# # Day 3 (9/12) in-class notebook
# 
# The objectives of this notebook are to practice
# * the concept of gene regulatory networks
# * creating and using Python modules
# * reading input from files
# * calling functions on lists of arguments using unpacking

# # The lac operon gene regulatory network
# In this notebook, we will practice with very simple modeling of the lac operon gene regulatory network that was described in lecture.  
# 
# We will add one more component to this network, which is the *CAP* protein.  In an environment with low levels of glucose the CAP protein binds to the regulatory region for the lac operon and increases transcription of the lac operon, but only when *lacI* is not bound to the regulatory region.  This allows the cell to try to make up for the lack of glucose by increasing its metabolism of lactose instead.
# 
# The entire network, along with the deterministic functions/circuits for each downstream variable, is defined by the figure below.  The `lactose`, `lacI`, `glucose`, and `CAP` input variables take the value `True` when they are present and the value `False` when they are absent.  The `lacI_bound` and `CAP_bound` variables are also boolean valued and depend on a subset of the input variables.  The `lacZ` variable represents the transcription level of the lac operon, and can take one of three values: "absent", "low", and "high."

# ![Lac circuit](day3_network.png)

# We will define this network in Python using a series of very simple functions, which can then be composed.

# ## PROBLEM 1 - lacI_bound (1 POINT)
# Write a function that specifies the lacI-bound circuit, as defined in the figure above.  This should be a simple one-liner that uses a boolean expression.

# In[38]:


def lacI_bound(lactose, lacI):
#
# YOUR CODE HERE
    return lacI and not lactose
#


# In[39]:


# tests for function lacI_bound
assert lacI_bound(False, False) == False, "Failed on input False, False"
assert lacI_bound(False, True) == True, "Failed on input False, True"
assert lacI_bound(True, False) == False, "Failed on input True, False"
assert lacI_bound(True, True) == False, "Failed on input True, True"
print("SUCCESS: lacI_bound passed all tests!")


# ## PROBLEM 2 - CAP_bound (1 POINT)
# Write a function that specifies the CAP-bound circuit, as defined in the figure above.  This should also be a simple one-liner that uses a boolean expression.

# In[40]:


def CAP_bound(glucose, CAP):
#
# YOUR CODE HERE
    return CAP and not glucose
#


# In[41]:


# tests for function CAP_bound
assert CAP_bound(False, False) == False, "Failed on input False, False"
assert CAP_bound(False, True) == True, "Failed on input False, True"
assert CAP_bound(True, False) == False, "Failed on input True, False"
assert CAP_bound(True, True) == False, "Failed on input True, True"
print("SUCCESS: CAP_bound passed all tests!")


# ## PROBLEM 3 - lacZ (1 POINT)
# Write a function that specifies the lacZ circuit, as defined in the figure above.

# In[42]:


def lacZ(is_lacI_bound, is_CAP_bound):
#
# YOUR CODE HERE
    if is_lacI_bound: return "absent"
    elif is_CAP_bound: return "high"
    else: return "low"
#


# In[43]:


# tests for function lacZ
assert lacZ(False, False) == "low", "Failed on input False, False"
assert lacZ(False, True) == "high", "Failed on input False, True"
assert lacZ(True, False) == "absent", "Failed on input True, False"
assert lacZ(True, True) == "absent", "Failed on input True, True"
print("SUCCESS: lacZ passed all tests!")


# ## PROBLEM 4 - lacZ full circuit (1 POINT)
# Finally, let us write a function that gives the value of lacZ depending on the input variables `lactose`, `lacI`, `glucose`, and `CAP`.  Use composition of the functions above to accomplish this in a simple one-liner.

# In[44]:


def lacZ_full_circuit(lactose, lacI, glucose, CAP):
#
# YOUR CODE HERE
    is_lacI_bound = lacI_bound(lactose, lacI)
    is_CAP_bound = CAP_bound(glucose, CAP)
    return lacZ(is_lacI_bound, is_CAP_bound)
#


# In[45]:


# tests for function lacZ_full_circuit
# note that these are only a subset of the possible inputs
assert lacZ_full_circuit(False, False, False, False) == "low", "Failed on input False, False, False, False"
assert lacZ_full_circuit(False, False, False, True) == "high", "Failed on input False, False, False, True"
assert lacZ_full_circuit(False, True, False, True) == "absent", "Failed on input False, True, False, True"
assert lacZ_full_circuit(False, True, True, True) == "absent", "Failed on input False, True, True, True"
print("SUCCESS: lacZ_full_circuit passed all tests!")


# ## PROBLEM 5 - creating and using a module (1 POINT)
# We will now practice with creating a Python module.  Modules make it easy to reuse your code and keep related functions, variables, and classes in a separate namespace.
# 
# For this problem, you are to do the following:
# 1. Create a new file `lac_network.py` in your workspace by clicking on the jupyter icon above, clicking on the "new" drop down menu at the right of the interface, and selection "text file".
# 2. Copy the Python code for each of your lac circuit functions that you have written above into the `lac_network.py` file.
# 3. Import your `lac_network` module within this notebook and test that you can call functions defined within the module.

# In[46]:


# tests for the lac_network module
import lac_network
assert lac_network.lacZ_full_circuit(False, False, False, False) == "low", "lac_network.lacZ_full_circuit failed"
assert lac_network.lacI_bound(False, False) == False, "lac_network.lacI_bound failed"
assert lac_network.CAP_bound(False, False) == False, "lac_network.CAP_bound failed"
assert lac_network.lacZ(False, False) == "low", "lac_network.lacZ failed"
print("SUCCESS: lacZ_network module passed all tests!")


# ## PROBLEM 6 - reading from a file (1 POINT)
# We will now practice with reading data from a text file.  In particular, we will read a file that contains some input values for the `lacZ_full_circuit`, with a different set of input values on each line.  The input values will be specified for the variables `lactose`, `lacI`, `glucose`, and `CAP`, and in that order.  On each line, the values will be separated by one or more whitespace characters.
# 
# Write a function that takes as input the name of a file containing input values for the `lacZ_full_circuit` function and outputs a list of lists of the input values.  The first tuple in the list should correspond to the input values from the first line of the file, and so on for the other lines in the file.
# 
# You will likely find the following function, which converts the strings "True" and "False" to Python boolean values, of use.
# 
# You will also likely find the `split` method of string functions helpful.

# In[47]:


def str_to_bool(s):
    if s == 'True':
         return True
    elif s == 'False':
         return False
    else:
         raise ValueError("Input is neither 'True' nor 'False': " + s)


# In[48]:


def read_lacZ_full_circuit_inputs(filename):
    #
    # YOUR CODE HERE
    lacZ_full_circuit_inputs = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            parameters_str = line.split(" ")
            print(parameters_str)
            parameters_bool = [str_to_bool(parameter) for parameter in parameters_str]
            lacZ_full_circuit_inputs.append(parameters_bool)
    return lacZ_full_circuit_inputs
    #


# In[49]:


# tests for read_lacZ_full_circuit_inputs
assert read_lacZ_full_circuit_inputs("lac_network_inputs.txt") == [[False, False, False, False],
                                                                   [False, False, False, True],
                                                                   [False, False, True, False],
                                                                   [False, False, True, True]]
print("SUCCESS: read_lacZ_full_circuit_inputs passed all tests!")


# ## PROBLEM 7 - calling functions with arguments in a list (1 POINT)
# Finally, we will practice calling a function that takes multiple arguments when the arguments are packed within a single list or tuple.  For this we will use Python's [unpacking](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists) syntax.
# 
# For example, suppose we have a number of words in a list, and we want to use the print statement to print all of the words on a single line, separated by a single space character.  We can use unpacking to make this easy.

# In[50]:


some_words = ["Here", "are", "some", "words"]


# In[51]:


print(some_words)


# In[52]:


print(*some_words)


# Notice the difference in the output from the two print statements above.  In the first statement, `print` is given a single argument, a list of strings.  In the second statement, `print` is given multiple arguments, each an element from the list `some_words`.

# Use this argument unpacking technique to write a function that calls `lacZ_full_circuit` on each of a list of input value lists, such as is returned by the `read_lacZ_full_circuit_inputs` function you defined in the previous problem.  The function should return a list of the corresponding outputs from the `lacZ_full_circuit` function.

# In[53]:


def call_lacZ_full_circuit_on_list(inputs_list):
    #
    # YOUR CODE HERE
    output = []
    for single_input in inputs_list:
        output.append(lacZ_full_circuit(*single_input))
    return output
        
    #


# In[54]:


# tests for call_lacZ_full_circuit_on_list
test1_list = [[False, False, False, False],
              [False, False, False, True],
              [False, False, True, False],
              [False, False, True, True]]
assert call_lacZ_full_circuit_on_list(test1_list) == ['low', 'high', 'low', 'low'], "Failed on test1_list"
test2_list = [[False, False, False, True]]
assert call_lacZ_full_circuit_on_list(test2_list) == ['high'], "Failed on test2_list"
print("SUCCESS: call_lacZ_full_circuit_on_list passed all tests!")


# ## Submitting your notebook

# Congratulations, you have reached the end of this notebook!  To submit your work, press the big blue "Submit" button at the top of this web page.  You may submit as many times as you wish and your final grade will be based on your most recent submission.  After you submit, a grade report will become available telling you how many points you received on each problem in the notebook.

# In[ ]:




