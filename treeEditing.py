from main import Node, Tree
import json
from dependencies import clothing_list

def createWardrobe(fileList, wardrobe):
    item = 'tmp'
    tree = Tree()
    clothing_list_nested = [[], [], [], [], [], [], []]
    tree.create_node("Wardrobe", "wardrobe",)
    print("Press ENTER to exit")

    for clothing_type in clothing_list:
        tree.create_node(clothing_type, clothing_type, parent="wardrobe")
    index = 0

    tree.save2file("wardrobe.txt")
    with open('wardrobe_data.txt', 'w') as filehandle:
        json.dump(clothing_list_nested, filehandle)
    wardrobe.tree = tree
    wardrobe.data = clothing_list_nested
    return wardrobe


def loadWardrobe(wardrobe):                 #get json into list
    with open('wardrobe_data.txt', 'r') as filehandle:
        wardrobe.data = json.load(filehandle)
    return wardrobe

def loadTree(wardrobe):                     #turn list into tree for readability
    wardrobe.tree.create_node("Wardrobe", "wardrobe")
    for clothing_type in clothing_list:
        wardrobe.tree.create_node(clothing_type, clothing_type, parent="wardrobe")
    index = 0
    for nested_type_ID in wardrobe.data:
        clothing_type = clothing_list[index]
        for article in nested_type_ID:
            wardrobe.tree.create_node(article[0], article[0], parent=clothing_type)
        index += 1
    wardrobe.tree.save2file("wardrobe.txt")
    return wardrobe


def addNewClothes(wardrobe):
    menu_text = "Please input the number corresponding to what you'd like to add.\n1. Shirt \n2. Jacket\n3. Coat\n4. Pants\n5. Socks\n6. Shoes\n7. Hat\n"
    index = int(input(menu_text))
    article = str(input("Enter description: "))
    color_val = str(input("Enter color: "))
    color_val.lower()


    while True:                                                                             # loops until input is valid, this is used multiple times elsewhere
        thermal_val = input("Enter seasonal: \n1. Summer\n2. Spring/Fall\n3. Winter\n4. All\n")
        if thermal_val.isdigit() and 1 <= int(thermal_val) <= 4:
            if thermal_val == 1:
                thermal_val = "Summer"
            elif thermal_val == 2:
                thermal_val = "Spring"
            elif thermal_val == 3:                                                          # USER INPUT GOES INTO PACKAGE ARRAY, CONSISTING OF [ITEM NAME] THEN A DICT OF IT'S ATTRIBUTES
                thermal_val = "Winter"                                                      # the dict is for use of access when sorting for color schemes, etc.
            elif thermal_val == 4:
                thermal_val = "All"
            break



    while True:
        tier_val = input("Enter occasion: \n1. Casual\n2. Party\n3. Business\n4. All\n")
        if tier_val.isdigit() and 1 <= int(tier_val) <= 4:
            if tier_val == 1:
                tier_val = "Casual"
            elif tier_val == 2:
                tier_val = "Party"
            elif tier_val == 3:
                tier_val = "Business"
            elif tier_val == 4:
                tier_val = "All"
            break


    article_dict = {'color': color_val, 'thermal': thermal_val, 'tier': tier_val}
    flat_list = [item for sublist in wardrobe.data for item in sublist]  # flattens list to check easily
    package = (article, article_dict)
    if article in flat_list:                                             #TODO THIS METHOD FOR CHECKING DUPES MAY NO LONGER WORK
        print("Item already in list, did not add\n")
    else:
        wardrobe.data[index - 1].append(package)
        wardrobe.tree.create_node(article, article, parent=clothing_list[index-1])
    wardrobe.tree.save2file("wardrobe.txt")
    with open('wardrobe_data.txt', 'w') as filehandle:
        json.dump(wardrobe.data, filehandle)

    return wardrobe

def deleteWardrobe(fileTree, fileList):
    fileTree.truncate()
    fileList.truncate(0)
    quit()

def deleteItem(wardrobe):
    menu_text = "Please input the number corresponding to what you'd like to delete.\n1. Shirt \n2. Jacket\n3. Coat\n4. Pants\n5. Socks\n6. Shoes\n7. Hat\n"
    while True:
        index = input(menu_text)
        if index.isdigit(): index = int(index)
        if 1 <= int(index) <= 7: break

    index -= 1
    parent_node = clothing_list[index]
    sub_t = wardrobe.tree.subtree(parent_node)
    sub_t.show()
    article = str(input("Enter item name for removal: "))

    for entry in wardrobe.data[index]:
        if article == entry[0]:       # entry[0] is identifying the name of the clothing, [big list[name of clothing, dict]]
            wardrobe.data[index].remove(entry)
            wardrobe.tree.remove_node(article)
            print("Item: " + article + " successfully removed.")
            return wardrobe

    print("Item could not be found. Make sure you type it exactly and try again.\n\n")
    return wardrobe


def showTree(wardrobe):
    wardrobe.tree.show(line_type="ascii-em")