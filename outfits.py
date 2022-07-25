import treeEditing              #TODO add attribute for weather, casual, etc.
from main import Node, Tree
from dependencies import clothing_list
import random
optionals = [1, 2, 6]
def getNewOutfit(wardrobe):                                 # random outfit given
    result_tree = Tree()
    result_tree.create_node("Outfit", "Outfit")

    i = 0
    for index in wardrobe.data:
        if not index: continue      #check for empty section
        if i in optionals:
            num = random.randint(0, 1)
            if num == 0:                #rolls to see if optional clothing items are chosen
                i += 1
                continue
        result_tree.create_node(clothing_list[i], clothing_list[i], parent="Outfit")
        length = len(index) - 1
        selection = random.randint(0, length)
        article = (index[selection])[0]                     # subscript is to access name value, not the dict paired with it
        result_tree.create_node(article, article, parent=clothing_list[i])
        i += 1
    print("\nHERE IS YOUR NEW OUTFIT\n---------")
    result_tree.show(line_type="ascii-em")

def outfitOptions(wardrobe_list):                       #utility for advanced wardrobe, gets possible clothes for given criteria, then uses this to generate it
    result_tree = Tree()
    result_tree.create_node("Outfit", "Outfit")

    i = 0
    for index in wardrobe_list:
        if not index:
            result_tree.create_node(clothing_list[i], clothing_list[i], parent="Outfit")
            article = ("N/A " + clothing_list[i])  # check for empty section
            result_tree.create_node(article, article, parent=clothing_list[i])
            i += 1
            continue
        if i in optionals:
            num = random.randint(0, 1)
            if num == 0:  # rolls to see if optional clothing items are chosen
                i += 1
                continue
        result_tree.create_node(clothing_list[i], clothing_list[i], parent="Outfit")
        length = len(index) - 1
        selection = random.randint(0, length)
        article = index[selection]  # subscript is to access name value, not the dict paired with it
        result_tree.create_node(article, article, parent=clothing_list[i])
        i += 1
    print("\nHERE IS YOUR NEW OUTFIT\n---------")
    result_tree.show(line_type="ascii-em")


def getNewOutfitAdv(wardrobe):                                              # get outfit but options to match parameters given by user
    outfit_text = "Enter 1 for yes, 2 for no. You may say yes to multiple options."
    color_text = "Sort by color?"
    thermal_text = "Sort by seasonal?"
    tier_text = "Sort by informal/formal?"
    season_list = "Enter season: \n1. Summer\n2. Spring/Fall\n3. Winter"
    tier_list = "Enter occasion: \n1. Casual\n2. Party\n3. Business"
    print(outfit_text)

    while True:
        color_choice = input(color_text)
        if color_choice.isdigit():
            color_choice = int(color_choice)
        if 0 < color_choice <= 2: break

    while True:
        thermal_choice = input(thermal_text)
        if thermal_choice.isdigit():
            thermal_choice = int(thermal_choice)
        else: continue
        if 1 <= thermal_choice <= 2: break

    while True:
        tier_choice = input(tier_text)
        if tier_choice.isdigit(): tier_choice = int(tier_choice)
        else: continue
        if 1 <= tier_choice <= 2: break


    print(color_choice + thermal_choice + tier_choice)
    if int(color_choice) == 1:
        print("Which color would you like to choose?")
        color_sort = input("Input color: ")
        color_sort.lower()

    if thermal_choice == 1:
        while True:
            thermal_sort = input(season_list)
            if thermal_sort.isdigit(): thermal_sort = int(thermal_sort)
            if 1 <= thermal_sort <= 3: break

    if tier_choice == 1:
        while True:
            tier_sort = input(tier_list)
            if tier_sort.isdigit(): tier_sort = int(tier_sort)
            if 1 <= tier_sort <= 3: break
                                                                                        # make new list, only add items that match params, grab random from that list, put those in new tree, display

    filtered_list = [[], [], [], [], [], [], []]
    outer_index = 0
    for outer_array in wardrobe.data:                                     # do color first, then filter thermal, then filter that by tier
        for i in outer_array:
            match1 = False
            match2 = False
            match3 = False

            if color_choice == 1:
                if color_sort.casefold() == i[1].get("color").casefold(): match1 = True
            else: match1 = True

            if thermal_choice == 1:
                if thermal_sort == int(i[1].get("thermal")) or int(i[1].get("thermal")) == 4: match2 = True         #matches if item is in same category, or if the listed item is categorized as matching for all (4)
            else: match2 = True

            if tier_choice == 1:
                if tier_sort == int(i[1].get("tier")) or int(i[1].get("tier")) == 4: match3 = True
            else: match3 = True                                   # gets dict key, compares to desired color palette, case-insensitive with case_fold

            if match1 == True and match2 == True and match3 == True:
                filtered_list[outer_index].append(i[0])   # if all criteria met, add item to the filtered list
        outer_index += 1
    print("FILTERED LIST: ", filtered_list)
    while True:
        outfitOptions(filtered_list)
        repeat = input("Would you like a different outfit with the same criteria?\n1. Yes\n2. No\n")
        if int(repeat) == 1: continue
        else: break


