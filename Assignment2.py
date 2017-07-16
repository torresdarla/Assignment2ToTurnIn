#Programmed by Darla Torres
#July 16, 2017
#This program will guide you in creating a song by asking for four verses, a chorus, and a chorus repeater.

#Program begins by importing a package with very useful functions
import Short

#Here we have a "for each" loop that asks for each of the five components of the song
song=[]
verse=['first verse','second verse','third verse','fourth verse','chorus']
for time in verse:
    verses= Short.userString("Enter the %s:" %time)
    song = song + ["%s" %verses]

#Program now asks for chorus repeater
repeat = Short.userInt("Enter the chorus repeat:")

#Program will now turn each chunk of the song into its own list, applying the chorus repeater at the end
p1= song[0].upper()
p2= song[1].upper()
p3= song[2].upper()
p4= song[3].upper()
p5= (song[4].lower() + " ") * repeat
p6= (song[4].lower() + " ") * (repeat + 1)

#Program orders the separate parts appropriately and creates a list
finalsong=[p1,p5,p2,p5,p3,p5,p4,p6, "...one more time!...",p1,p5,p2,p5,p3,p5,p4,p6]
print finalsong


print" "

#Program prints each verse in a readable form
for verse in finalsong:
    print verse











