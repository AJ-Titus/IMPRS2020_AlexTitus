from psychopy import visual, sound, core, event 
import pandas as pd 
import numpy as np

#create the window for the experiment
win = visual.Window((800, 600), color=(1, 1, 1,))

def showText(inputText = "Text"):
    message = visual.TextStim(win, alignVert="center", alignHoriz= 'center', text = inputText, color = (-1, -1, -1), bold= True)
    message.draw()
    win.flip()

# Load one of the stimuli files as a dataframe
sound_stimuli = pd.read_csv('lexical_decision_stimuli.csv')

sounds = []

# for sound in sound_stimuli['word']:
#     sounds.append(sound +'.wav') 

#the below allows the program to iterate over multiple columns within the 'sounds' file and create a sound. 
#additionally, when using the Sound module, it is best to use a different name for the variables (e.g., soundFile, filename, etc.)
#it is also necessary to use \\ in the path to the rows we want to iterate over. 
#value= is used for sound files and image= is used for image files
# #within value, you need to specify the path at each step, so sounds = the folder and within that folder we loop over freq AND word
#Within the folders or df, it is best to not name your variables or outputs none or other functions because it will confuse python

for i, row in sound_stimuli.iterrows():
    sounds.append(sound.Sound(value = 'sounds' + '\\' + row['freq_category'] + '\\'  + row['word'] + '.wav'))

# sounds = []
# for sound in sound_stimuli['sounds']:
#     sound_stimuli.append(sound.SoundStim(win, sound=sound))

# Here we randomly permute the stimuli
sounds = np.random.permutation(sounds)

#create the fixation cross
fixation = visual.TextStim(win, text='+', alignHoriz= 'center', alignVert= 'center', bold = True, color=(-1, -1, -1))

#Welome message for the experiment
showText("Welcome to the experiment! \r\n\r\nPress the SPACEBAR to to continue to the next page")
event.waitKeys(keyList=['space'])

#Explain how the experiment will work
showText("In this experiment, you will be presented with and audio sound \r\n\r\nPress the SPACEBAR to to continue to the next page")
event.waitKeys(keyList=['space'])

showText("Your task is to determine if the audio sounds are real words or not \r\n\r\nPress the SPACEBAR to to continue to the next page")
event.waitKeys(keyList=['space'])

showText("To respond, you will have to press either the A or the L button on the keyboard \r\n\r\nA represents Real Word and L represents NonWord")
event.waitKeys(keyList=['space'])

showText("Please try to answer as quickly and accurately as possible.")
event.waitKeys(keyList=['space'])

#the below allows you to draw the fixation cross in the window you have created
clock = core.Clock()

def left_msg(): 
    left_msg = visual.TextStim(win, pos =(-0.5, 0), text = "Real Word", bold= True, color = (-1,-1,-1))
    left_msg.draw()
    core.wait(0.5)

def right_msg():
    right_msg = visual.TextStim(win, pos =(0.5, 0), text = "NonWord", bold= True, color = (-1,-1,-1))
    right_msg.draw()
    core.wait(0.5)

results = []

for sound in sounds:
    # Show the trial
    fixation.draw()
    core.wait(0.350)
    win.flip()

    core.wait(0.750)
    sound.play()
    win.flip()

    left_msg() 
    right_msg()
    win.flip()
    core.wait(0.350)

    # Wait for user input
    start_time = clock.getTime()  # You could also start a new clock for each user input
    keys = event.waitKeys(maxWait=4, keyList=['a', 'l'], timeStamped=clock, clearEvents=True)
    if keys is not None:
        key, end_time = keys[0]
    else:  # If no keys were pressed:
        key = None
        showText("Please, remember to answer as quickly as possible!")
        core.wait(0.3)
        end_time = clock.getTime()
    
    # Store the results
    results.append({
        'sound': sound.sound,
        'key': key,
        'start_time': start_time,
        'end_time': end_time
    })

# Create a dataframe based on the results, and store them to a csv file
results = pd.DataFrame(results)
results['reaction_time'] = results['end_time'] - results['start_time']  # Calculate all the reaction times
results.to_csv('results.csv')