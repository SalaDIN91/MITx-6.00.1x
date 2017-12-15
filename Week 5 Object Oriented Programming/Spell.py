# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 03:03:58 2017

@author: Mayur
"""

# =============================================================================
# Exercise: spell
# 
# How do we need to modify Accio so that print(Accio()) will print the following 
# description?
# 
# Summoning Charm Accio
# This charm summons an object to the caster, potentially over a significant distance.
# =============================================================================

#code
class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)

spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())
