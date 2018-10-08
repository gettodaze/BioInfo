
# coding: utf-8

# # Day 1 (9/7) in-class notebook
# 
# The objectives of this notebook are to practice
# * representing DNA molecules as strings
# * determining the complementary strand of a double-stranded DNA molecule
# * working with strings
# * working with lists
# * writing functions
# * looping over sequences
# * using and submitting Jupyter notebooks
# 

# ## Providing answers to problems in Jupyter Notebooks
# 
# Much of your in-class and homework will be done in Jupyter Notebooks with a Python 3 kernel.  In general, you will be provided with a *template* notebook and your job will be to fill in the missing sections by following the specifications preceding each missing section.  The missing sections may be either code blocks, text (in Markdown), or perhaps even a plot.  
# 
# Following each missing section will be some tests (in the form of `assert` statements) of the accuracy of your solutions.  Some tests will be visible to you and others may be hidden for the purposes of grading.  You should not modify the test blocks, but you should certainly run them to see if your code is passing the visible tests.  Do not worry if you modify the test blocks.  They will be automatically replaced with their original tests when you submit.

# ### PROBLEM 1 - variable assignment (10 POINTS)
# Your first excercise/problem is to simply assign to the variable `my_name` a string containing your name.  Please do so in the code cell below.

# In[5]:


#
# YOUR CODE HERE
my_name = "John McCloskey"
#


# The code block below will test that you have successfully assigned a non-empty string to the variable `my_name`.

# In[4]:


assert isinstance(my_name, str) and my_name != ""


# ## Representing and working with DNA molecules as strings
# 
# In this notebook we will work with a fragment of the DNA sequence for the human gene *CFTR*, mutations in which are known to cause the disease [Cystic Fibrosis](https://en.wikipedia.org/wiki/Cystic_fibrosis).

# In[6]:


cftr_gene_fragment = ("ACTTCACTTCTAATGGTGATTATGGGAGAACTGGAGCCTTCAGAGGGTAA"
                      "AATTAAGCACAGTGGAAGAATTTCATTCTGTTCTCAGTTTTCCTGGATTA"
                      "TGCCTGGCACCATTAAAGAAAATATCATCTTTGGTGTTTCCTATGATGAA"
                      "TATAGATACAGAAGCGTCATCAAAGCATGCCAACTAGAAGAG")
print(cftr_gene_fragment)


# Just to get you familiar with writing functions in Python, here is a silly function that returns the concatenation of the first and last characters of a string.

# In[7]:


def first_and_last(s):
    return s[0] + s[-1]


# In[8]:


first_and_last(cftr_gene_fragment)


# ### PROBLEM 2 - slicing and concatenating strings (1 POINT)
# 
# One of the most famous disease causing mutations in humans is the deltaF508 mutation in the *CFTR* gene.  This is most common mutation carried by people with Cystic Fibrosis.  This mutation occurs in the gene fragment specified above and corresponds to the deletion of 3 consecutive bases, starting at base 129 (using 1-based numbering).  The code below shows how to "slice" the string represnting this gene fragment to determine the identify of the 3 bases that are deleted by this mutation.  Note that Python uses 0-based indexing!
# 

# In[9]:


print("The deleted bases in the deltaF508 mutation are", cftr_gene_fragment[128:131])


# In this problem, you are to write a function that takes as input a string, a `start` position (0-based index), and a `length`, and returns a new string that is the result of deleting `length` characters starting at the `start position` from the input string.  We will use this function to determine the sequence of the gene fragment that results from the deltaF508 mutation.

# In[14]:


def delete_substring(s, start, length):
    #
    # YOUR CODE HERE
    return s[:start]+s[start+length:]
    #
#delete_substring("John",1,2)


# In[15]:


# Here are some tests of your function
assert delete_substring("Testing", 0, 2) == "sting"
assert delete_substring("Testing", 4, 3) == "Test"
assert delete_substring("Testing", 1, 3) == "Ting"


# Now let's use your function to determine the sequence of the gene fragment that results from the deltaF508 mutation:

# In[16]:


delete_substring(cftr_gene_fragment, 128, 3)


# ### PROBLEM 3 - complementary bases (1 POINT)
# In this problem we will practice using the Python `if` statement to write a function that returns the complement of a single-base (single-character) string.  You are provided with the first few lines of the function.

# In[17]:


def complement(base):
    if base == 'A':
        return 'T'
    elif base == 'C':
    #
    # YOUR CODE HERE
        return 'G'
    elif base == 'T':
        return 'A'
    elif base == 'G':
        return 'C'
    #
    else:
        raise ValueError(base + " is not a valid DNA base")


# In[18]:


assert complement('A') == 'T'
assert complement('T') == 'A'
assert complement('C') == 'G'
assert complement('G') == 'C'


# ### PROBLEM 4 - reverse complement (1 POINT)
# Finally, in this problem, we will write a function that is given the string representing one strand of a double-stranded DNA molecule and returns a string representing the opposite (complementary) strand, specified in the 5' to 3' direction.  To do this, we will first construct a `list` containing the characters of the opposite strand and then use the `join` method of string objects to convert from a `list` back to a `string`.  This will be more efficient than repeated concatentation.

# One function you might consider using is `reversed`, which allows you to loop over sequences in reverse order.  For example:

# In[19]:


for number in reversed(range(5)):
    print(number)


# In[30]:


def reverse_complement(s):
    # we first start with an empty list
    opposite_bases = []
    # using a for loop, we loop through the bases of s in *reverse* order
    # and append the complementary base to the opposite bases list
    #
    # YOUR CODE HERE
    for base in reversed(s):
        opposite_bases.append(complement(base))
    #
    # we can use the 'join' method with an empty string
    # to concatenate all strings in the list
    return ''.join(opposite_bases)
# reverse_complement("ATG")


# In[31]:


assert reverse_complement("ATCG") == "CGAT"
assert reverse_complement("A") == "T"
assert reverse_complement("") == ""


# Finally, let us use your `reverse_complement` function to determine the opposite strand of the *CFTR* gene fragment that we have working with in this notebook.

# In[32]:


reverse_complement(cftr_gene_fragment)


# ## Submitting your notebook

# Congratulations, you have reached the end of this notebook!  To submit your work, press the big blue "Submit" button at the top of this web page.  You may submit as many times as you wish and your final grade will be based on your most recent submission.  After you submit, a grade report will become available telling you how many points you received on each problem in the notebook.
