# -*- coding: utf-8 -*-
"""
Spyder Editor
Michael Fredericks
02.05.2020
myicon
This is a temporary script file.
"""
#icon is a dictionary. each key must have a list of the same legnth as the
#previous keys.
myicon = {
        1  : [1,1,1,1,1,1,1,1,1,1],
        2  : [1,1,1,1,0,0,0,0,0,0],
        3  : [1,1,1,0,0,0,0,1,1,0],
        4  : [1,1,0,0,0,0,1,0,0,0],
        5  : [1,0,0,0,0,1,0,0,0,0],
        6  : [0,0,0,0,1,0,0,0,0,1],
        7  : [0,0,0,1,0,0,0,0,1,1],
        8  : [0,1,1,0,0,0,0,1,1,1],
        9  : [0,0,0,0,0,0,1,1,1,1],
        10 : [1,1,1,1,1,1,1,1,1,1]
        }

#scale icon function. it will take a function and a scale value, and add
# correspoding width and legnth to the icon. given more time, i would like to
# add a way to validate that the scale value is a positive integer.         
def scale_icon(icon, scale_value):
    scaled_icon = {}
    counter = 1
    for key in icon:
        key_list = icon[key]
        value_list = []
        for value in key_list:
            for i in range(scale_value):
                value_list.append(value)
        for i in range(scale_value):
            scaled_icon.update( {counter : value_list} )
            counter += 1
    return scaled_icon

#print icon by cycling through each digit in each list in each dictionary key.
def print_icon(icon):
    for key in icon:
        key_list = icon[key]
        list_legnth = len(key_list)
        counter = 0
        for value in key_list:
            print(value, end="")
            if counter < (list_legnth - 1):
                print(" ", end="")
            else:
                print(end="\n")
            counter += 1

#will rotate the icon 90 degrees.
def rotate_90(icon):
    print("The following is the icon rotated 90 degrees:")
    icon_legnth = len(icon)
    validation_key_list = icon[1]
    key_legnth = len(validation_key_list)
    same_legnth_validate = 0
    for key in range(1, icon_legnth):
        if len(icon[key]) != key_legnth:
            same_legnth_validate += 1
    if same_legnth_validate > 0:
        print("Not a Valid Icon")
    else:
        for key_i in range(key_legnth):
            for dict_i in range(icon_legnth, 0, -1):
                key_list = icon[dict_i]
                if dict_i > 1:
                    print(key_list[key_i], end=" ")
                else:
                    print(key_list[key_i], end="")
            print(end="\n")

#will rotate the icon 270 degrees.
def rotate_270(icon):
    print("The following is the icon rotated 270 degrees:")
    icon_legnth = len(icon)
    validation_key_list = icon[1]
    key_legnth = len(validation_key_list)
    same_legnth_validate = 0
    for key in range(1, icon_legnth):
        if len(icon[key]) != key_legnth:
            same_legnth_validate += 1
    if same_legnth_validate > 0:
        print("Not a Valid Icon")
    else:
        for key_i in range(key_legnth - 1, 0, -1):
            for dict_i in range(1, icon_legnth + 1):
                key_list = icon[dict_i]
                if dict_i < icon_legnth:
                    print(key_list[key_i], end=" ")
                else:
                    print(key_list[key_i], end="")
            print(end="\n")

#will rotate the icon 180 degrees.
def rotate_180(icon):
    print("The following is the icon rotated 180 degrees:")
    icon_legnth = len(icon)
    validation_key_list = icon[1]
    key_legnth = len(validation_key_list)
    same_legnth_validate = 0
    for key in range(1, icon_legnth):
        if len(icon[key]) != key_legnth:
            same_legnth_validate += 1
    if same_legnth_validate > 0:
        print("Not a Valid Icon")
    else:
        for dict_i in range(icon_legnth, 0, -1):
            key_list = icon[dict_i]
            for key_i in range(key_legnth - 1, -1, -1):
                if key_i > 0:
                    print(key_list[key_i], end=" ")
                else:
                    print(key_list[key_i], end="")
            print(end="\n")

#main function - putting it all together                    
def main(icon):
    print_icon(scale_icon(icon, 3))
    print()
    rotate_90(scale_icon(icon, 3))
    rotate_180(scale_icon(icon, 3))
    rotate_270(scale_icon(icon, 3))

#run main
main(myicon)
    
     