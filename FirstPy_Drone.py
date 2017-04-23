########################################################################
##
## CS 101
## Program #1
## Name Diego Brown
## Email xxxxxx@xxxx.xxxx.edu
##
## PROBLEM : We need a program that will quickly yeild the total energy
##           consumption (in Amps) and total operational time given the:
##
##           *  Battery Rating (mAh)
##           *  Motor Quantity (mtr_num)
##           *  Amps per motor (amp_mtr)
##
##           *  From these variables, this program should be able to
##              calculate the values: Total Amps, Amp Hours,and Flight Time
##           *  It will then convert the float value of 'flt_tme' (represe-
##              nting hours) into hours, minutes and seconds.
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import math

# Request for battery rating, # of motors, and average draw per motor.
mAh               = float(input('Please enter your battery rating in mAh: '))
mtr_num           = float(input('Thanks! How many motors does your drone have: '))
amp_mtr           = float(input('Got it. Lastly, how many amps are drawn per motor: '))

# Establishing base units.
ttl_amp           = mtr_num * amp_mtr                                       #Total amps.
amp_hrs           = mAh*.001                                                #Amp Hours.
flt_tme           = (amp_hrs)/ttl_amp                                       #Total flight time.

# Unit conversions and int isolation.
hours             = (amp_hrs)//ttl_amp                                      #Represent 'hours' as whole number integers.
minutes           = (((amp_hrs)/(ttl_amp)) - int(hours)) *60                #Convert float value into whole number minutes.
seconds_percent   = (((amp_hrs)/(ttl_amp)) - int(hours)) *60 - int(minutes) #Isolates the float value associated with the right side of the '.'.
seconds           = seconds_percent * 60                                    #Converts the float value on the right of the decimal into seconds.


print('Your flight time will be:',flt_tme,'hours')                          #This gives the floating value for hours.
print('In other words, your drone will use', ttl_amp,'AMPS, ' \
          'over the course of a ', hours,'hour(s),',minutes, 'minute(s),',seconds,'second long flight.')
