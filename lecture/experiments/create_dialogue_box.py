#===============
# Import modules
#===============

from psychopy import gui, core, visual, event, data # import psychopy modules/functions
import os # import os module
import pandas as pd

#========================================
# Create GUI dialog box for user input
#========================================

# Get subject name, age, handedness and other information through a dialog box
exp_info = {
            'participant': '', # participant name as string
            'age': '', # age name as string
            'left-handed':False, # handedness as boolean
            'like this course':('yes', 'no') # course feedback as tuple
            }

# define name of experiment
exp_name = 'pfp_2022' # set experiment name

# create GUI dialog box from dictionary
dlg = gui.DlgFromDict(dictionary=exp_info, title=exp_name)

# If 'Cancel' is pressed, quit experiment
if dlg.OK == False:
    core.quit()

#=================================================
# Data storage: basic information, filename & path
#=================================================

# get current working directory for easier creation/saving of files
cwd = os.getcwd()

# Get date and time
exp_info['date'] = data.getDateStr(format="%Y-%m-%d_%H_%M") # get date and time via data module
exp_info['exp_name'] = exp_name # add experiment name to info dict

# Check if set data path exists, if not create it
data_path = os.path.join(cwd, exp_info['exp_name'], exp_info['participant'])

if not os.path.isdir(data_path):
    os.makedirs(data_path)  # create subject directory
    print(data_path)  # print subject_directory in terminal


# Create a unique filename for the experiment data    
data_fname = exp_info['participant'] + '_' + exp_info['date'] # create initial file name from participant ID and date/time
data_fname = os.path.join(data_path, data_fname) # add path from GUI dialog box

#======================
# Save your Data
#======================
# create a "DataFrame" for easier file handling

df_data = pd.DataFrame.from_dict(exp_info)
print(df_data)

# save Dataframe as a .csv file to the provided subject directory
df_data.to_csv(data_fname + '.csv', sep = ',', encoding='utf-8', index=False)