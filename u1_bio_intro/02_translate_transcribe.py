
# coding: utf-8

# # Day 2 (9/10) in-class notebook
# 
# The objectives of this notebook are to practice
# * the concept of transcription of DNA to RNA
# * the concept of translation of RNA to protein
# * determining the consequences of mutations in protein-coding DNA
# * using dictionaries
# * using list comprehensions
# * using the methods of string objects

# ## PROBLEM 1 - transcription (1 POINT)
# As a warm-up problem, write a function that takes as input a DNA string (sense strand) and outputs the string representing the RNA that would result from transcribing this DNA sequence.

# You will likely find one of [methods of string objects](https://docs.python.org/3/library/stdtypes.html#string-methods) very convenient for accomplishing this with a single line.  For example, to obtain a string with characters of a string in uppercase, you can use the `upper` method.

# In[1]:


"AcTggggTTatgatTAG".upper()


# In[2]:


def transcribe(dna_sequence):
#
# YOUR CODE HERE
    return dna_sequence.replace("T","U")
    
#


# In[3]:


# tests for function transcribe
assert transcribe("ACGT") == "ACGU", "Failed on input 'ACGT'"
assert transcribe("") == "", "Failed on empty string input"
assert transcribe("CTACTACTGCTA") == 'CUACUACUGCUA', "Failed on input 'CTACTACTGCTA'"
print("SUCCESS: transcribe passed all tests!")


# ## PROBLEM 2 - codon translation (1 POINT)

# Next we will explore the use of the Python [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) data structure as a convenient way in which to implement a function that translates RNA to protein.

# First, we will start by translating a single codon.  We could write a giant set of if-elif statements for this, but it will be more elegant, convenient, and (usually) efficient to implement this as a lookup in a table, such as a dictionary object.  I have done the hard work for you and specified the standard genetic code (RNA codon to amino acid) as a dictionary below. 

# In[4]:


genetic_code = {
 'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N',
 'ACA': 'U', 'ACC': 'U', 'ACG': 'U', 'ACU': 'U',
 'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGU': 'S',
 'AUA': 'I', 'AUC': 'I', 'AUG': 'M', 'AUU': 'I',
 'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H',
 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
 'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
 'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAU': 'D',
 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
 'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
 'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
 'UAA': '*', 'UAC': 'Y', 'UAG': '*', 'UAU': 'Y',
 'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
 'UGA': '*', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C',
 'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F'}


# Note that in the table above, `*` is used to represent a stop codon, and is not an amino acid.

# Using this dictionary object, write a function that takes as input a single RNA codon string and outputs its corresponding amino acid, or the symbol representing the stop codon.  You need not check that the input is valid.

# In[5]:


def translate_codon(rna_codon):
#
# YOUR CODE HERE
    return genetic_code[rna_codon]
#


# In[6]:


# tests for function translate_codon
assert translate_codon("ACG") == "U", "Failed on input 'ACG'"
assert translate_codon("UUU") == "F", "Failed on input 'UUU'"
assert translate_codon("UGA") == "*", "Failed on input 'UGA'"

# Check that the genetic_code dictionary is being used
orig_genetic_code = genetic_code
del genetic_code
try:
    translate_codon("ACG")
except NameError:
    pass
else:
    raise AssertionError("translate_codon does not use genetic_code")
finally:
    genetic_code = orig_genetic_code

print("SUCCESS: translate_codon passed all tests!")


# ## PROBLEM 3 - Splitting an RNA into its codons (1 POINT)

# We will next write a function that takes as input an RNA string and returns a list of its codons, in the same order as they appear in the RNA.  We will assume that the first three bases of the RNA correspond to a codon and that the length of RNA is a multiple of three.

# In this problem I encourage you to learn about and use Python's [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) syntax, which is concise way to construct a list.  For example, the code below, which constructs a list of the squares of the first ten non-negative integers

# In[7]:


squares = []
for x in range(10):
    squares.append(x**2)


# can be more concisely writtten as

# In[8]:


squares = [x**2 for x in range(10)]


# In[9]:


def codons(rna):
#
# YOUR CODE HERE
    return [codon for codon in [rna[i*3:(i+1)*3] for i in range(len(rna)//3)]]
    #print(codons)
    #print(len(rna))
    
#codons("")
#


# In[10]:


# tests for function codons
assert codons("ACGCCUGGG") == ["ACG", "CCU", "GGG"], "Failed on input 'ACGCCUGGG'"
assert codons("UUU") == ["UUU"], "Failed on input 'UUU'"
assert codons("") == [], "Failed on empty string"
print("SUCCESS: translate_codon passed all tests!")


# ## PROBLEM 4 - RNA fragment translation (1 POINT)

# Next let us write a function that translates all codons of a string representing an RNA fragment, where we again assume that the first three bases of the RNA correspond to a codon and that the length of RNA is a multiple of three. At this point, we will not require that the first codon is the start codon and that the last codon is a stop codon.

# As in the previous in-class activities, you will likely find the `join` method of the empty string convenient for concatenating all of the strings in a list together.  For example,

# In[11]:


bases = ["A", "C", "G", "T"]
''.join(bases)


# In[12]:


def translate_rna_fragment(rna):
#
# YOUR CODE HERE
    amino_acids = []
    for codon in codons(rna):
        aa = translate_codon(codon)
        if aa is "*": break
        amino_acids.append(aa)
    return ''.join(amino_acids)
#
# print(translate_rna_fragment("AGGCUA"))
# rna = "ACGUUU"
# codonsvar = codons(rna)
# translate_codonvar = [translate_codon(codon) for codon in codonsvar]
# print(rna)
# print(codonsvar)
# print(translate_codonvar)


# In[13]:


# tests for translate_rna_fragment
assert translate_rna_fragment("UUUGCGACUUAU") == "FAUY", "Failed on input 'UUUGCGACUUAU'"
assert translate_rna_fragment("ACG") == "U", "Failed on input 'UGA'"
assert translate_rna_fragment("") == "", "Failed on the empty string"
print("SUCCESS: translate_codon passed all tests!")


# ## PROBLEM 5 - RNA translation (1 POINT)

# In this problem we step up the complexity and perform RNA translation of an entire RNA molecule.  Recall that RNA translation of a full RNA molecules involves:
# 1. Scanning for the first occurrence of a start codon ("AUG")
# 2. Translation of the start codon and successive codons in the same reading frame
# 3. Termination of translation when a stop codon is reached
# 
# You may assume that the RNA molecule contains a start codon as well as a downstream, in-frame, stop codon.

# In[14]:


def translate_rna(rna):
#
# YOUR CODE HERE
    start_index = rna.find("AUG")
    return translate_rna_fragment(rna[start_index:])
#


# In[15]:


# tests for translate_rna
assert translate_rna("AUGACUUAUUAG") == "MUY", "Failed on input 'AUGACUUAUUAG'"
assert translate_rna("AAUGACUUAUUAG") == "MUY", "Failed on input 'AAUGACUUAUUAG'"
assert translate_rna("AUGACUUAUUAGCT") == "MUY", "Failed on input 'AUGACUUAUUAGCT'"
assert translate_rna("AAUGACUUAUUAGCT") == "MUY", "Failed on input 'AAUGACUUAUUAGCT'"
print("SUCCESS: translate_rna passed all tests!")


# ## PROBLEM 6 - Consequences of the deltaF508 mutation in CFTR (2 POINTS)
# 
# We will now revisit the CFTR gene fragment that we saw in the last in-class activities and examine how the deltaF508 mutation impacts the resulting amino acid sequence of the encoded protein.  Below is again the sequence of the CFTR gene fragment.

# In[16]:


cftr_gene_fragment = ("ACTTCACTTCTAATGGTGATTATGGGAGAACTGGAGCCTTCAGAGGGTAA"
                      "AATTAAGCACAGTGGAAGAATTTCATTCTGTTCTCAGTTTTCCTGGATTA"
                      "TGCCTGGCACCATTAAAGAAAATATCATCTTTGGTGTTTCCTATGATGAA"
                      "TATAGATACAGAAGCGTCATCAAAGCATGCCAACTAGAAGAG")
print(cftr_gene_fragment)


# And here is the sequence of the mutated CFTR gene fragment, which has bases 129, 130, and 131 (1-based coordinates) removed.

# In[17]:


deltaf508_fragment = cftr_gene_fragment[:128] + cftr_gene_fragment[131:]
print(deltaf508_fragment)


# Recall that the removed bases were

# In[18]:


print(cftr_gene_fragment[128:131])


# Using your translation function and considering the coordinates of the deltaF508 mutation, determine
# 1. how many codons of the non-mutant fragment overlap with this deletion
# 2. which single amino acid is effectively deleted from the resulting mutant RNA fragment
# 
# Note that this CFTR sequence is only a fragment (substring) of the entire CFTR gene and so will not begin with a start codon or end with a stop codon.  You will also need to know that first three bases of the fragment are a codon.
# 
# Answer the above two questions by assigning your answers to the variables in the code below.

# In[28]:


# Assign to the variable 'num_codons_overlapping_with_deletion' an integer
#
# YOUR CODE HERE
cftr_gene_fragment_RNA = transcribe(cftr_gene_fragment)
deltaf508_fragment_RNA = transcribe(deltaf508_fragment)
cftr_polypeptide = translate_rna_fragment(cftr_gene_fragment_RNA)
deltaf508_polypeptide = translate_rna_fragment(deltaf508_fragment_RNA)
print(cftr_polypeptide)
print(deltaf508_polypeptide)

# print((cftr_gene_fragment_codons))
common = 0
for i in range(len(deltaf508_polypeptide)):
    str1 = deltaf508_polypeptide[i]
    str2 = cftr_polypeptide[i]
    #print(str1,str2,str1 == str2)
    if str1 == str2:
        common = common + 1
    else: break
    
num_codons_overlapping_with_deletion = common
print(common)

num_codons_overlapping_with_deletion = 2
print(num_codons_overlapping_with_deletion)

#
# Assign to the variable 'amino_acid_deleted' a single character string
#
# YOUR CODE HERE
amino_acid_deleted = cftr_polypeptide[common]
# print(amino_acid_deleted)
# wild_cut = cftr_gene_fragment_codons[:len(deltaf508_fragment_codons)]
# for a,b in enumerate(zip(wild_cut, deltaf508_fragment_codons)):
#     print(a+1,b)
#


# In[25]:


# test for num_codon_overlapping_with_deletion
assert isinstance(num_codons_overlapping_with_deletion, int), "num_codons_overlapping_with_deletion is not an integer"
#
# AUTOGRADER TEST - DO NOT REMOVE
#


# In[26]:


# test for amino_acid_deleted
assert isinstance(amino_acid_deleted, str), "amino_acid_deleted is not a string"
#
# AUTOGRADER TEST - DO NOT REMOVE
#


# ## Submitting your notebook

# Congratulations, you have reached the end of this notebook!  To submit your work, press the big blue "Submit" button at the top of this web page.  You may submit as many times as you wish and your final grade will be based on your most recent submission.  After you submit, a grade report will become available telling you how many points you received on each problem in the notebook.

# In[ ]:





# In[ ]:




