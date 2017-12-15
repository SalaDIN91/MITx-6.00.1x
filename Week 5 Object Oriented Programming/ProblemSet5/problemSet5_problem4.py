# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 04:08:08 2017

@author: Mayur
"""

# =============================================================================
# Problem 4 - Decrypt a Story
# 
# For this problem, the graders will use our implementation of the Message, 
# PlaintextMessage, and CiphertextMessage classes, so don't worry if you did not 
# get the previous parts correct.
# 
# Now that you have all the pieces to the puzzle, please use them to decode the 
# file story.txt. The file ps6.py contains a helper function get_story_string() 
# that returns the encrypted version of the story as a string. Create a 
# CiphertextMessage object using the story string and use decrypt_message to 
# return the appropriate shift value and unencrypted story string.
# =============================================================================

#code
def decrypt_story():
    encryptedStory = get_story_string()
    decryptedStory = CiphertextMessage(encryptedStory)
    return decryptedStory.decrypt_message()