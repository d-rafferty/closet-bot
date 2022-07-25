from treelib import Node, Tree  #todo: tkinter to build GUI for menuing;  let user change which items are optional (jacket, glasses, hat)
import tkinter as tk
import treeEditing
import outfits
import os
import json
import sys

def main():
    # guiInit()
    filepath = 'wardrobe_data.txt'
    fileTree = open("wardrobe.txt", "w+")   #overwrites file
    fileList = open("wardrobe_data.txt", "a+")    #appends to file, don't overwrite data
    wardrobe = Wardrobe()

    if os.path.getsize(filepath) != 0:
        wardrobe = treeEditing.loadWardrobe(wardrobe)   # if file isn't empty, load wardrobe
        wardrobe = treeEditing.loadTree(wardrobe)
    else:
        print("No current wardrobe exists. Creating one now.")
        wardrobe = treeEditing.createWardrobe(fileList, wardrobe)
        tree = wardrobe.tree

    while True:
        menu_text = "1. Receive new random outfit \n2. Receive new personalized outfit.\n3. Display current wardrobe\n4. Add new clothing\n5. Delete a single item\n6. Save your progress\n9. Delete current wardrobe\n0. Exit the program\n"
        # create menu list of things to do
        print("Enter the number of the option you desire, then press enter. Inputting 0 at any point will terminate the program")
        selection = str(input(menu_text))
        if selection == "1":
            outfits.getNewOutfit(wardrobe)

        elif selection == "2":
            # ask for desired options, then pass in
            outfits.getNewOutfitAdv(wardrobe)

        elif selection == "3":
            treeEditing.showTree(wardrobe)


        elif selection == "4":
            treeEditing.addNewClothes(wardrobe)


        elif selection == "5":
            treeEditing.deleteItem(wardrobe)
            continue

        elif selection == "6":
            with open('wardrobe_data.txt', 'w') as filehandle:
                json.dump(wardrobe.data, filehandle)
            continue

        elif selection == "9":
            print("WARNING: THIS WILL ERASE THE CURRENT WARDROBE COMPLETELY!!!!")
            warning_text = input("ARE YOU SURE YOU WISH TO CONTINUE??")
            if warning_text == "yes":
                warning_text2 = input("ARE YOU SURE YOU'RE SURE BECAUSE THIS WILL DELETE EVERYTHING. EVERY SINGLE THING?? **MAKING A BACKUP COPY OF YOUR .TXT FILES IS HIGHLY RECOMMENDED**")
                if warning_text2 == "yes":
                    print("You have made a grave mistake. Program will now close.")
                    treeEditing.deleteWardrobe(fileTree, fileList)
            break
        elif selection == "0":
            quit_text = "1. Save and exit.\n2. Exit without saving.\n"
            selection = int(input(quit_text))
            if selection == 1:
                print("Saving....")
                print("Program will now close.")
                with open('wardrobe_data.txt', 'w') as filehandle:
                    json.dump(wardrobe.data, filehandle)
                sys.exit()
            elif selection == 2:
                print("Program will now close.")
                sys.exit()

def guiInit():
    window = tk.Tk()
    greeting = tk.Label(text="Welcome to your wardrobe :)", foreground="black", background="pink")
    greeting.pack()
    window.mainloop()

class Wardrobe:
    def __init__(self):
        self.tree = Tree()
        self.data = [[], [], [], [], [], [], []]


if __name__ == '__main__':
    main()