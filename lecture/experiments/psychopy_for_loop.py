from psychopy import core, visual, event, data # import psychopy modules/functions


# Open a window
win = visual.Window(size=(800,600), color='gray', units='pix', fullscr=False) # set size, background color, etc. of window


for i in range(10):

    # draw number to screen
    visual.TextStim(win, text=i, pos=[0, 90], height=40, italic=True).draw()
    # after everything is drawn, flip it to the front screen
    win.flip()

    core.wait(0.5)  #?

        # if participants press `escape`, stop the experiment
    if event.getKeys(['escape']):
        core.quit()
        