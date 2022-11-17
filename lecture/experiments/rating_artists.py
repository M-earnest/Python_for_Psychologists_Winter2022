# 2022, Michael Ernst

#===============
# Import modules
#===============

from psychopy import gui, core, visual, event, data # import psychopy modules/functions
import os # import os module
import pandas as pd
import numpy.random as rnd # import random module from numpy

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

#===============================
# Creation of window and messages
#===============================

# Open a window
win = visual.Window(size=(800,600), color='gray', units='pix', fullscr=False) # set size, background color, etc. of window

# Define experiment start text
welcome_message = visual.TextStim(win,
                                text="Welcome to the experiment. Please press spacebar to continue.",
                                color='black', height=40)


# Define trial start text
start_message = visual.TextStim(win,
                                text="In this experiment you will rate different musical artists, snacks and animals on a scale from 1 to 7. Please press the spacebar to start.",
                                color='black', height=40)

# Define experiment end text
end_message = visual.TextStim(win,
                                text="You have reached the end of the experiment, thanks for participating.",
                                color='black', height=40)


#=====================
# Start the experiment
#=====================

# display welcome message
welcome_message.draw() # draw welcome message to buffer screen
win.flip() # flip it to the front screen
keys = event.waitKeys(keyList=['space', 'escape']) # wait for spacebar key press before advancing or quit when escape is pressed 

# display start message
start_message.draw() # draw start message to buffer screen
win.flip() # flip it to the front screen
keys = event.waitKeys(keyList=['space', 'escape']) # wait for spacebar key press before advancing or quit when escape is pressed

#==========================
# Define the trial sequence
#==========================

# define stimuli to be presented
artists = [
    'Queen Adreena', 'Mac Miller', 'Nirvana', 'Álvaro Soler', 'Kanye West', 'Taylor Swift',
    'BTS', 'SYML', 'Ed Sheeran', 'Betterov', 'Mark Medlock',
    'Drake', 'NF', 'Lauv', 'Arctic Monkeys', 'Alfa Mist', 'Nepumuk',
    'Reezy', 'Cat Burns', 'Aurora', 'Godspeed You! Black Emperor'
]

# randomize order of presented stimuli
rnd.shuffle(artists)

#================================
# Define a rating scale
#================================

ratingScale = visual.RatingScale(win, 
          scale = None,          # This makes sure there's no subdivision on the scale
          low = 1,               # This is the minimum value I want the scale to have
          high = 7,             # This is the maximum value of the scale
          showAccept = True,    # This shows the user's chosen value in a window below the scale
          markerStart = 4,       # This sets the rating scale to have its marker start on 5
          labels = ['1 - Not at all', '7 - A lot'], # This creates the labels
          pos = [0, -80]) # set the position of the rating scale within the window

trial_counter = 0

# define a dictionary to save responses in
data_info = {
'stimulus':[],
'rating_rt':[],
'rating':[],
'trial_num':[]
}


# Run through the trials, stimulus by stimulus
for artist in artists:

    ratingScale.reset()
    while ratingScale.noResponse:  # show & update until a response has been made

        # display/draw task question to remind participants
        visual.TextStim(win, text='How much do you like the following?', pos=[0, 90], italic=True).draw()
        # display/draw respective stimulus within each iteration, notice how the stimulus is set "on the fly"
        visual.TextStim(win, text=artist, bold=True, pos=[0, 30], height=40).draw()
        # display/draw help message regarding rating scale
        visual.TextStim(win, text='(Move the marker along the line and click "enter" to indicate your rating from 1 to 7.)', 
                        pos=[0,-200], height=14).draw()
        # display/draw the rating scale
        ratingScale.draw()

        # after everything is drawn, flip it to the front screen
        win.flip()

        # if participants press `escape`, stop the experiment
        if event.getKeys(['escape']):
            core.quit()   
                

    # get the current rating        
    rating = ratingScale.getRating()
    # get the response time of the current rating 
    rt = ratingScale.getRT()

    # write trial data into dict
    data_info['stimulus'].append(artist)
    data_info['rating'].append(rating)
    data_info['rating_rt'].append(rt)
    data_info['trial_num'].append(trial_counter)

    # if participants press `escape`, stop the experiment
    if event.getKeys(['escape']):
        core.quit()   
            

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

# Also add data from experiment info gui into DataFrame
df_data['subject'] = exp_info['participant']
df_data['date'] = exp_info['date']
df_data['left_handed'] = exp_info['left-handed']
df_data['exp_name'] = exp_info['exp_name']

# save Dataframe as .csv
print(df_data)
df_data.to_csv(data_fname + '.csv', sep = ',', encoding='utf-8', index=False)
