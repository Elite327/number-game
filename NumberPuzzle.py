import tkinter as tk
import dis
import random
from functools import partial

# *MARK Variables
buttonTexts = ['1', '2', '3', '4', '5', '6', '7', '8', '']
buttonList = []
window = tk.Tk()
numberFrame = tk.Frame(master=window, width=300, height=300)

# *MARK Functions


def buildNumberFrame():
    buttonList.clear()
    for buttonIndex in range(9):
        buttonText = buttonTexts[buttonIndex]
        button = tk.Button(master=numberFrame, text=buttonText, width=9,
                           height=4, command=partial(buttonEventHandler, buttonText))
        if button['text'] == '' :
            button['state'] = tk.DISABLED
            button['bg'] = 'lightgray'
        buttonList.append(button)

    numberFrame.columnconfigure(3)
    numberFrame.rowconfigure(3)

    buttonIndex = 0

    for x in range(3):
        for y in range(3):
            buttonList[buttonIndex].grid(row=x, column=y)
            buttonIndex = buttonIndex+1


def newgamebuttonEventHandler():
    random.shuffle(buttonTexts)
    buildNumberFrame()

def switch(clickedButtonPosition, blankButtonPosition, clickedButtonText):
    # switch elements in buttonTexts at positions blankButtonPosition and clickedButtonPosition
    buttonTexts[blankButtonPosition] = clickedButtonText
    buttonTexts[clickedButtonPosition] = ''
    # build number frame again
    buildNumberFrame()

def buttonEventHandler(clickedButtonText):
    # get the text of button clicked:
    print('clicked button text', clickedButtonText)
    # find position of the button clicked:
    clickedButtonPosition = buttonTexts.index(clickedButtonText)
    print('clicked button position', clickedButtonPosition)
    # find index of blank button
    blankButtonPosition = buttonTexts.index('')
    print('blankButtonPosition', blankButtonPosition)
    # write logic to switch blank and clicked buttons based on their positions
    if blankButtonPosition == 0:
        if clickedButtonPosition == 1 or clickedButtonPosition == 3:
            switch(clickedButtonPosition, blankButtonPosition, clickedButtonText)
        else:
            wrongButton()
        # else :
        #     playsound('number-game/Resources/zapsplat_multimedia_error_tone_buzz_17636.mp3')
    elif blankButtonPosition == 1:
        if clickedButtonPosition == 0 or clickedButtonPosition == 4 or clickedButtonPosition == 2:
            switch(clickedButtonPosition, blankButtonPosition, clickedButtonText)
        else:
            wrongButton()
        # else :
        #     playsound('number-game/Resources/zapsplat_multimedia_error_tone_buzz_17636.mp3')
    elif blankButtonPosition == 2:
        if clickedButtonPosition == 1 or clickedButtonPosition == 5:
            switch(clickedButtonPosition, blankButtonPosition, clickedButtonText)
        else:
            wrongButton()
        # else :
        #     playsound('number-game/Resources/zapsplat_multimedia_error_tone_buzz_17636.mp3')
    elif blankButtonPosition == 3:
        if clickedButtonPosition == 0 or clickedButtonPosition == 4 or clickedButtonPosition == 6:
            switch(clickedButtonPosition, blankButtonPosition, clickedButtonText)
        else:
            wrongButton()
        # else :
        #     playsound('number-game/Resources/zapsplat_multimedia_error_tone_buzz_17636.mp3')
    elif blankButtonPosition == 4:
        if clickedButtonPosition == 1 or clickedButtonPosition == 3 or clickedButtonPosition == 5 or clickedButtonPosition == 7:
            switch(clickedButtonPosition, blankButtonPosition, clickedButtonText)
        else:
            wrongButton()
        # else :
        #     playsound('number-game/Resources/zapsplat_multimedia_error_tone_buzz_17636.mp3')
    elif blankButtonPosition == 5:
        if clickedButtonPosition == 2 or clickedButtonPosition == 4 or clickedButtonPosition == 8:
            switch(clickedButtonPosition, blankButtonPosition, clickedButtonText)
        else:
            wrongButton()
        # else :
        #     playsound('number-game/Resources/zapsplat_multimedia_error_tone_buzz_17636.mp3')
    elif blankButtonPosition == 6:
        if clickedButtonPosition == 3 or clickedButtonPosition == 7:
            switch(clickedButtonPosition, blankButtonPosition, clickedButtonText)
        else:
            wrongButton()
        # else :
        #     playsound('number-game/Resources/zapsplat_multimedia_error_tone_buzz_17636.mp3')
    elif blankButtonPosition == 7:
        if clickedButtonPosition == 4 or clickedButtonPosition == 6 or clickedButtonPosition == 8:
            switch(clickedButtonPosition, blankButtonPosition, clickedButtonText)
        else:
            wrongButton()
    elif blankButtonPosition == 8:
        if clickedButtonPosition == 7 or clickedButtonPosition == 5:
            switch(clickedButtonPosition, blankButtonPosition, clickedButtonText)
        else:
            wrongButton()


# *MARK Main

print('Audio is not supported on replit, so if you want audio download to your computer')

random.shuffle(buttonTexts)

window.title('N.P.')

window.resizable(width=False, height=False)

buildNumberFrame()

newgameframe = tk.Frame(master=window)

newgamebutton = tk.Button(master=newgameframe, text='New Game',
                          width=30, bg='gray', command=lambda: newgamebuttonEventHandler())

numberFrame.pack()
newgameframe.pack()
newgamebutton.pack()

window.mainloop()
