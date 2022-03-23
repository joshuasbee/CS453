########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, Joshua Bee
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

from cgitb import text
from turtle import clear


SECRET = 3
PRIVILEGED = 2
CONFIDENTIAL = 1
PUBLIC = 0

clearance_dict = {
  "Public": PUBLIC,
  "Confidential" : CONFIDENTIAL,
  "Privileged" : PRIVILEGED,
  "Secret" : SECRET
}

def get_text_clearance(text_control):
  return clearance_dict.get(text_control, PUBLIC)

def security_condition_read(clearance, text_clearance):
  return get_text_clearance(text_clearance) <= clearance

def security_condition_write(clearance, text_clearance):
  return get_text_clearance(text_clearance) >= clearance