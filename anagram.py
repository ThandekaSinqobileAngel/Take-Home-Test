#!/usr/bin/env python
# coding: utf-8

# 
# Correctness: 2/4
# Effeciency: 2/4
# Style:3/4
# Documentation: 1/4
# 
# Positive aspect of the submission
# Thank you for your attempt to this task. You have shown that you have some understanding of how to go about solving this task. Your program is heading towards the right direction.
# 
# Aspects of the submission that could be improved
# However they are minor issues that you need to pay attention to in order for your program to run accordingly. In line 5, provide list value that you are sorting. Correctly indent your code to avoid unnecessary errors. Initialise the list in your code. So that the program will group the anagrams together. Please keep in mind that commenting your code is another important factor. Below is a link with more details on the importance of commenting your code.
# 
# https://www.simplilearn.com/tutorials/python-tutorial/comments-in-python#:~:text=Comments%20in%20Python%20is%20the,line%20of%20code%20was%20written.
# 
# Overall feedback
# Kindly make the necessary changes on your code and resubmit. 

# In[34]:


# This is how the program should look like.
class Solution:
    
  # iniialise the list  
  strs = ["eat","tea","tan","ate","nat","bat"]
    
  # Create a function with two parameters  
  def groupAnagrams(self, strs):
        
      # initialise an empty dictionary  
      result = {}
        
      # iterate over the list to group all anagrams  
      for i in strs:
            
         # sorts the list of items in ascending order 
         x = "".join(sorted(i))
         
         # checking the string in dictionary
         if x in result:
            
            # adding the string to the group anagrams 
            result[x].append(i)
         else:
            
            # initializing a list with current string
            result[x] = [i]  
      
      # returning the list of anagrams
      return list(result.values())

# calling the class with function used to groups anagrams 
ob1 = Solution()

# printing the values of the dict (anagram groups)
print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

