"""
Authors:
    - Jack Taylor, Fiebach -lab; Goethe University Frankfurt
Copyright 2022
"""
# import os - this is a very useful library for working with files and folders across different operating systems
import os

# import shutil - this is used at the end to delete the folder once we've finished
import shutil

# assign a variable which stores the location of the desktop
# os.path.join() is better than joining folder names with '\' or '/', because it will work consistently across different operating systems
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# assign a path which will be the addams_family folder location
addams_path = os.path.join(desktop_path, 'addams_family')

# if it doesn't already exist, make the addams_family folder
if not os.path.exists(addams_path):
    os.makedirs(addams_path)

# assign a path for the the_new_yorker folder
newyorker_path = os.path.join(addams_path, 'the_new_yorker')

# if it doesn't already exist, make the addams_family folder
if not os.path.exists(newyorker_path):
    os.makedirs(newyorker_path)

# create a list containing the Addams family members we want to create a subfolder for
addams_family = ['pugsely', 'gomez', 'fester']

# loop over the Addams family characters and create the scooby_doo_* files
for character in addams_family:

    # if the subfolder doesn't already exist, make character's subfolder
    character_path = os.path.join(addams_path, character)
    if not os.path.exists(character_path):
        os.makedirs(character_path)

    # create the text files
    # note that we use i+1 in various places, because by default Python starts counting at zero!
    for i in range(10):

        # if i is an odd number, save in the current character's folder
        # otherwise (if i is an even number), save in a the_new_yorker folder, with a file path showing their origin
        # this conditional works by detecting whether the remainder, after dividing i by 2, is 1, in which case the number must be odd
        if (i+1) % 2 == 1:  # i.e., if odd
            # generate the file name:
            # 'f' at the start of the string tells python that this is a formatted string
            # {i} tells python to insert at that position the current value for i, plus one because Python starts counting at zero
            file_i_name = f"scooby_doo_{i+1}.txt"

            # get the path of the file to create
            file_i_path = os.path.join(character_path, file_i_name)

        else:  # i.e., if even

            # generate the file name
            file_i_name = f'scooby_doo_{i+1}_{character}.txt'

            # get the path of the file to create
            file_i_path = os.path.join(newyorker_path, file_i_name)

        # create the file
        open(file_i_path, 'w').close()

# when done, you can uncomment and run the following line to delete the created folder
# shutil.rmtree(addams_path, ignore_errors=True)
