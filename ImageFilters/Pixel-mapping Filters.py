########################################################################
##
## CS 101
##
## Name     Diego Brown
## Email    xxxxxx@xxxx.xxxx.edu
##
## PROBLEM : This program will alter the pixel values of an original PPM
##           and transport them to a destination. Only color values will
##           be altered so color palatte will be different when destination
##           file is opened
##
## ALGORITHM : 
##      ##
##      Open file:
##      display menu
##          ask for .ppm file
##          ask for file destination
##      construct list from .txt version of file
##      (List the Red, Blue and Green values of the list
##      since the actual pixel values do not show until the 3rd line,
##      I began initializing at index 2. since every red, green and blue value is
##      equidistant from the last, I iterated through every 3rd item to populate
##       the color list... Color is dependent on where list starts)
##
##      Ask user for input to determine original file behavior
##
##      Inform user when file is done generating and is ready to be viewed
##      Close file
##
##      
##          
## ERROR HANDLING:
##
##      I ran into a problem where IDLE would crash everytime I tried to run
##      the code on files other than small.ppm. This was because I printed
##      new pixel values to the destination file. Since there are hundreds of
##      thousands of iterations, python would time out. This was resolved by
##      removing the print functions. I learned that values do not have to be
##      printed in order to affect the original file.
##
## OTHER COMMENTS:
##      Funky filer is fully functional
##      Grayscale pending a fix.
##      
##
########################################################################
#Open beginning file



Greeting = """ Welcome!

G. Grayscale
F. Funky
Q. Quit
"""
## Asking for file location
original = input('What file do you want to open? ')
"""

    Must be <filename>.ppm format
    Options:

            BadHeader1.ppm
            BadHeader2.ppm
            UMKCCampus.ppm
            Ocean.ppm
            park.ppm
            umkc.ppm
            
"""

original = open(original,'r')

## Asking for file destination
filtered = input('What will be the file destination after filtering? ')
filtered = open(filtered,'w')



# Empty set that gets populated with altered RGB values
threelist=[]

# Strips line and arranges value of next color component in list until the
# end of the file. This is a placeholder so values can be convered to mathable
# ints

for line in original:
    linelist = line.strip('\n')
    threelist.append(linelist)

#List the Red, Blue and Green values of the list
#since the actual pixel values do not show until the 3rd line,
#I began initializing at index 2. since every red, green and blue value is
#equidistant from the last, I iterated through every 3rd item to populate
#the color list... Color is dependent on where list starts

redlist    = (threelist[3:3])
for index, item in enumerate(redlist):
    redlist[index] = int(item)
    
#since greenlist begins with 4th index, 4 marks beginning of green iteration   
greenlist  = (threelist[4:3])
for index, item in enumerate(greenlist):
    greenlist[index] = int(item)

#Like greenlist, bluelist will begin at first instance of the blue component
bluelist   = (threelist[5:3])
for index, item in enumerate(bluelist):
    bluelist[index] = int(item)



#Prefix values do not represent pixel values. Since altering these can make the
#program crash, These 3 components are isolated so newpixelvalues can be altered
#independantly of them
prefix = threelist[:3]



#constructing new list make these values match the original




#All color components are equidistant from next in sequence.
#Therefore step in indexing list is constant

newpixelvalue = ['']*(len(redlist) + len(greenlist) + len(bluelist))
#Placement in redlist will begin with 0 index of new list

newpixelvalue[:3] = redlist

#placement begins with idex 1 for greenlist
newpixelvalue[1:3] = greenlist
#placement begins with idex 2 for bluelist
newpixelvalue[2:3] = bluelist




#reconstruct in same format as original
newpixelvalue = tuple([item for item in newpixelvalue if item != '' ])


    ##Add 3 line prefix to beginning of list
for item in prefix:
    print (item, file = filtered)
    
    ## Add remaining RGB pixel values to the list
ask = input('Please choose (G)rayscale  or (F)unky: ').upper()


# Filter options
if ask == 'G':
    for redlist in newpixelvalue:
        print ((redlist), file = filtered)
    for greenlist in newpixelvalue:
        print ((greenlist), file = filtered)
    for bluelist in newpixelvalue:
        print ((bluelist), file = filtered)
        
if ask == 'F':
    for redlist in threelist:
        print ((redlist), file = filtered)
    for greenlist in threelist:
        print ((greenlist), file = filtered)
    for bluelist in threelist:
        print ((bluelist), file = filtered)

        
print('Your filtered image has generated! Please navigate to the specified destination file to see your result')

#
       
original.close()
filtered.close()


### 
