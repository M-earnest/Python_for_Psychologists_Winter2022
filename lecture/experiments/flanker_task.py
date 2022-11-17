# Copyright 2022, Michael Ernst

#===============
# Import modules
#===============

from psychopy import gui, core, visual, event, data # import psychopy modules/functions
import os # import os module
import numpy.random as rnd # import random module from numpy
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
exp_name = 'pfp_22' # set experiment name

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
exp_info['date'] = data.getDateStr(format="%Y-%m-%d_%H:%M") # get date and time via data module
exp_info['exp_name'] = exp_name # add experiment name to info dict

# Check if set data path exists, if not create it
data_path = os.path.join(cwd, exp_info['exp_name'], exp_info['participant'])

if not os.path.isdir(data_path):
    os.makedirs(data_path)
    # print subject_directory in terminal
    print(data_path)
# otherwise print that subject directory already exists and where data will be stored
else:
    print('participant directory exists for = ' + exp_info['participant'])
    print('data path = ' + data_path)


# Create a unique filename for the experiment data    
data_fname = exp_info['participant'] + '_' + exp_info['date'] # create initial file name from participant ID and date/time
data_fname = os.path.join(data_path, data_fname) # add path from GUI dialog box


#===============================
# Creation of window and messages
#===============================

# Open a window
win = visual.Window(size=(900,700), color='gray', units='pix', fullscr=False) # set size, background color, etc. of window

# Define experiment start text
welcome_message = visual.TextStim(win,
                                text="Welcome to the experiment. Please press spacebar to continue.",
                                color='black', height=40)


# Define trial start text
start_message = visual.TextStim(win,
                                text="""In this experiment you will be presented with the different targets '>>>' and '<<<', \n\nPlease indicate the direction that these arrows are pointing in using the a (left) and l (right) buttons, respectively. \n\nBefore every target you will be presented with one the following arrow configurations:\n\n '>>> >>> >>>' or  '<<< <<< <<<'. \n\nPlease only react to the targets ('>>>' or '<<<') """,
                                color='black', height=20, anchorVert='center')

# Define experiment end text
end_message = visual.TextStim(win,
                                text="You have reached the end of the experiment, thanks for participating.",
                                color='black', height=40)


#==========================
# Define the trial sequence
#==========================


# define stimuli to be presented
targets = [
    '<<<', '>>>'
]

distractors = [
    '<<< <<< <<<', '>>> >>> >>>'
]

# define number of trials
trials_n = 4

# multiply list of stimuli by trial number
stimuli = targets*trials_n
flankers = distractors*trials_n

# randomize order of presented stimuli
rnd.shuffle(stimuli)
rnd.shuffle(flankers)

# if participants press `escape`, stop the experiment
if event.getKeys(['escape']):
    core.quit()   
#=====================
# Start the experiment
#=====================

# display welcome message
welcome_message.draw() # draw welcome message to buffer screen
win.flip() # flip it to the front screen
keys = event.waitKeys(keyList=['space']) # wait for spacebar key press before advancing or quit when escape is pressed 

# display start message
start_message.draw() # draw start message to buffer screen
win.flip() # flip it to the front screen
keys = event.waitKeys(keyList=['space']) # wait for spacebar key press before advancing or quit when escape is pressed

# establish dictionary to save data in
trial_counter = 0
data_info = {
'target':[],
'flanker':[],
'rt':[],
'response':[],
'trial_num':[]
}

trial_counter = 0
# Run through the trials, stimulus by stimulus
for stim in stimuli:
    
    flanker = flankers[trial_counter]

    # display/draw fixation cross
    visual.TextStim(win, text='+', pos=[0, 30], height=40).draw()
    # after everything is drawn, flip it to the front screen
    win.flip()

    core.wait(0.5)

    # display/draw flanker to prime participants
    visual.TextStim(win, text=flanker, bold=True, pos=[0, 30], height=40).draw()

    # after everything is drawn, flip it to the front screen
    win.flip()

    core.wait(0.8)

    # display/draw respective stimulus within each iteration, notice how the stimulus is set "on the fly"
    visual.TextStim(win, text=stim, bold=True, pos=[0, 30], height=40).draw()

    # if participants press `escape`, stop the experiment
    if event.getKeys(['escape']):
        core.quit()   
        
    # after everything is drawn, flip it to the front screen
    win.flip()
    trial_keys = event.waitKeys(keyList=['a', 'l'], timeStamped=True) # wait for spacebar key press before advancing or quit when escape is pressed 


    # write data into dict
    data_info['target'].append(stim)
    data_info['flanker'].append(flanker)
    data_info['response'].append(trial_keys[0][0])
    data_info['rt'].append(trial_keys[0][1])
    data_info['trial_num'].append(trial_counter)
    
    trial_counter += 1

#======================
# End of the experiment
#======================

# Display end message
end_message.draw() # draw end message to buffer screen
win.flip() # flip it to the front screen
keys = event.waitKeys(keyList=['space', 'escape']) # wait for spacebar key press before advancing or quit when escape is pressed

print('Experiment ended' + data.getDateStr(format="%Y-%m-%d_%H_M"))


#======================
# Save your Data
#======================
# create a "DataFrame" for easier file handling
df_data = pd.DataFrame.from_dict(data_info)

# translate stimuli to language descriptors for later analysis
df_data.loc[df_data['target'] == '>>>', 'target'] = 'right'
df_data.loc[df_data['target'] == '<<<', 'target'] = 'left'
df_data.loc[df_data['flanker'] == '>>> >>> >>>', 'flanker'] = 'right'
df_data.loc[df_data['flanker'] == '<<< <<< <<<', 'flanker'] = 'left'
df_data.loc[df_data['response'] == 'a', 'response'] = 'left'
df_data.loc[df_data['response'] == 'l', 'response'] = 'right'

# add condition column based on wether stimulus and flanker were matching
cond_list = []

for idx in range(len(df_data['target'])):
    stim = df_data['target'][idx]
    flank = df_data['flanker'][idx]
    
    cond = ' '
    if stim==flank:
#        print('congruent')
        cond='congurent'
    elif stim!=flank:
 #       print('incongruent')
        cond='incongurent'
    cond_list.append(cond)

#  evaluate wether participants made correct desicions
result_list = []
for idx in range(len(df_data['target'])):
    stim = df_data['target'][idx]
    resp = df_data['response'][idx]
    
    correct = ' '
    if stim==resp:
        correct='correct'
    elif stim!=resp:
        correct='false'

    result_list.append(correct)



# add results and exp_info to data_info dict
df_data['result'] = result_list
df_data['condition'] = cond_list
df_data['subject'] = exp_info['participant']
df_data['date'] = exp_info['date']
df_data['left_handed'] = exp_info['left-handed']
df_data['exp_name'] = exp_info['exp_name']

# save Dataframe as .csv
print(df_data)
df_data.to_csv(data_fname + '.csv', sep = ',', encoding='utf-8', index=False)



#import time #time module is built into Python
#t0=time.time() #time in secs
#nReps = 0
#while (time.time()-t0) < 0.5: #continue this loop for 0.5s
    #nReps = nReps+1 # (try using the shorthand n+=1 in the shell)
#print(f"we did {nReps:.0f} loops in 0.5s")