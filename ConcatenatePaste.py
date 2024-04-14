#version 0.5

import pystray
import pyperclip
import pandas as pd
from PIL import Image, ImageDraw
from pystray import Menu, MenuItem as Item

#Create a simple system tray icon
def create_image(width, height, color1, color2):
    image = Image.new('RGB', (width, height), "white")
    dc = ImageDraw.Draw(image)
    dc.rounded_rectangle(
        (5, 19, 45, 59), radius=6, fill="red")
    dc.rounded_rectangle(
        (27, 6, 58, 37), radius=6, fill="blue")
    return image

def after_click(icon, query):
    
    #Define the conjunction to be used
    if str(query) == "OR":
        conjunction = " OR "
    elif str(query) == "AND":
        conjunction = " AND "
    elif str(query) == "AND <>":
        conjunction = " AND <>"
    elif str(query) == "Quit":
        icon.stop()

    #Reads the clipboard and concatenates the strings.
    appunti = pd.read_clipboard("\s\s+", dtype=str, header=None)

    for i in range(len(appunti)):
        
        #If "Remove spaces" is true, remove the spaces
        if stateSpaces == True:
            ClipboardRow = appunti.iloc[i, 0].replace(' ','')
        else:
            ClipboardRow = str(appunti.iloc[i, 0])
            print("entro 1")
        print ("1"+ClipboardRow)

        #If "Front Asterisk" is true, adds the asterisk at the beginning of each row
        if stateFrAsterisk == True:
            ClipboardRow = "*" + ClipboardRow
            print("entro 2")
        print ("2"+ClipboardRow)

        #If "End Asterisk" is true, adds the asterisk at the end of each row
        if stateEnAsterisk == True:
            ClipboardRow = ClipboardRow + "*"
            print("entro 3")
        print ("3"+ClipboardRow)

        #Concatenates the rows (puts a <> where the selected conjunction is AND <> )
        if i == 0:
            output_tree = ClipboardRow
            if conjunction == " AND <>":
                output_tree = "<>" + ClipboardRow
        else:
            output_tree =  output_tree + conjunction + ClipboardRow
        print ("4"+ClipboardRow)

    #If "All capitals" is true, it turns all the text upper case
    if stateCapitals == True:
        output_tree=output_tree.upper()

    #Put the concatenated string the clipboard
    pyperclip.copy(output_tree)

def Capitals(icon, item):
    global stateCapitals
    stateCapitals = not item.checked

def Spaces(icon, item):
    global stateSpaces
    stateSpaces = not item.checked

def FrAsterisk(icon, item):
    global stateFrAsterisk
    stateFrAsterisk = not item.checked

def EnAsterisk(icon, item):
    global stateEnAsterisk
    stateEnAsterisk = not item.checked

#MAIN FUNCTION
global stateCapitals
global stateSpaces
global stateFrAsterisk
global stateEnAsterisk

stateCapitals = True
stateSpaces = True
stateFrAsterisk = False 
stateEnAsterisk = True

#Creates the icon and the menu with the commands

image = create_image(64, 64, 'blue', 'white')
icon = pystray.Icon("CP", image, "ConcatenatePaste",
					menu=pystray.Menu(
	pystray.MenuItem("OR", after_click),
	pystray.MenuItem("AND", after_click),
    pystray.MenuItem("AND <>", after_click),
    pystray.MenuItem("Settings",
                     Menu(Item('All capitals', Capitals, checked=lambda item: stateCapitals),
                          Item('Remove spaces', Spaces, checked=lambda item: stateSpaces),
                          Item('Front asterisk', FrAsterisk, checked=lambda item: stateFrAsterisk),
                          Item('End asterisk', EnAsterisk, checked=lambda item: stateEnAsterisk))
                        ),
	pystray.MenuItem("Quit", after_click)))
icon.run()