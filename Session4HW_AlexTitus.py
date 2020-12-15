from psychopy import visual, sound, core, event 
import pandas as pd 
import numpy as np


class Experiment:
    def __init__(self, window_size, text_color, background_color):
        self.text_color = text_color
        self.win = visual.Window(window_size, color=background_color)
        self.fixation = visual.TextStim(self.window, text='+', color=text_color)
        self.clock = core.Clock()
    
    def introduction(self, introduction, key):
        stimulus = visual.TextStim(self.win, text = introduction, color = self.text_color, key = 'space')
        stimulus.draw()
        self.key = key
        self.win.flip()
        
    
    def intstructions(self, instructions, key):
        stimulus = visual.TextStim(self.win, text = instructions, color = self.text_color, key = 'space')
        stimulus.draw()
        self.key = key
        self.win.flip()
        

    # Show a fixation cross on the experiment window for the given amount of time.
    def show_fixation(self, time=0.5):
        self.fixation.draw()
        self.win.flip()
        core.wait(time)


class audio_trial:
    def __init__(self,Experiment, name, audio, showText, left_choice, right_choice, fixation_time = 0.5, max_keyWait = 5, keyList=['a', 'l']):
        self.Experiment = Experiment
        self.name = name
        self.audio = audio
        self.fixation_time = fixation_time
        self.max_keyWait = max_keyWait
        self.keyList = keyList
        self.left_choice = left_choice
        self.right_choice = right_choice
        self.showText = showText

    def left_choice(self):
        left_choice = visual.TextStim(self.win, pos =(-0.5, 0), text = "Real Word", bold= True, color =self.text_color)
        left_choice.draw()
    
    def right_choice(self):
        right_choice = visual.TextStim(self.win, pos =(-0.5, 0), text = "Real Word", bold= True, color =self.text_color)
        right_choice.draw()


    def run_trial(self):
        # Show the trial
        
        def showText(self, message):
            message = visual.TextStim(self.win, alignVert="center", alignHoriz= 'center', text = message, color = (-1, -1, -1), bold= True)
            message.draw()

        self.Experiment.show_fixation.draw()
        self.Experiment.win.flip()
        core.wait(self.fixation_time)
        self.win.flip()

        core.wait(0.3)
        self.audio.play()
        self.win.flip()

        self.left_choice() 
        self.right_choice()
        self.window.flip()
        core.wait(0.4)
    

        # Wait for user input
        start_time = self.clock.getTime()  # You could also start a new clock for each user input
        keys = event.waitKeys(max_keyWait=self.max_keyWait, keysList=self.wait_keys, timeStamped= self.clock, clearEvents=True)
        if keys is not None:
            key, end_time = keys[0]
        else:  # If no keys were pressed:
            key = None
            showText("Please, remember to answer as quickly as possible!")
            core.wait(0.3)
            end_time = self.clock.getTime()
            
            # Store the results
        return {
            'trial': self.name,
            'key': key,
            'start_time': start_time,
            'end_time': end_time
            }
        # Create a dataframe based on the results, and store them to a csv file


#create the window for the experiment
experiment = Experiment((800, 600), (-1, -1, -1,), (1, 1, 1))

sound_path = 'C:\\Users\\Gebruiker\\OneDrive\\CLS PhD\MPI\\Python_workshop\\Session4_ObjectOrientedProgramming.py'
# Load one of the stimuli files as a dataframe
sound_stimuli = pd.read_csv('lexical_decision_stimuli.csv')

#empy list to create the sound file that we will play
trials = []

for i, row in sound_stimuli.iterrows():
    trials.append(sound.Sound(value = 'sounds' + '\\' + row['freq_category'] + '\\'  + row['word'] + '.wav'))

# Here we randomly permute the stimuli
trials = np.random.permutation(trials) 

Experiment.introduction('Welcome to the experiment! ' +
                        'Press the SPACEBAR to to continue to the next page')

Experiment.instructions('In this experiment, you will be presented with an audio sound' +
                        'Press the SPACEBAR to to continue to the next page')

Experiment.instructions('Your task is to determine if the audio sounds are real words or not' +
                        'To respond, you will have to press either the A or the L button on the keyboard' +
                        'A represents Real Word and L represents NonWord')

Experiment.instructions('Please try to answer as quickly and accurately as possible')

results = []
for trial in trials:
    result = trial.run()
    results.append(result)

# Store results to dataframe and save to CSV
results = pd.DataFrame(results)
results['reaction_time'] = results['end_time'] - results['start_time'] # Calculate all the reaction times
results.to_csv('results.csv')
