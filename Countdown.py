
from BaseFrame import *
from PlayerAction import PlayerAction


class Countdown(MyBaseFrame):

    def __init__(self, master):
        MyBaseFrame.__init__(self, master)
        # Object Attributes
        self.master = master
        self._time_seconds = COUNTDOWN_LENGTH
        self._sec = StringVar()
        
        # Populate 
        self._timer = Label(self, textvariable=self._sec,
                           font='Times 300', fg='Purple', bg='Black')
        
        # Layout
        self._timer.grid(row=0, column=0, rowspan=3, columnspan=3, sticky="NSEW" )

        # Update
        self._update_clock()

    def _update_clock(self):
        if self._time_seconds < 1:
            self.master.switch_frame(PlayerAction)
            return
        # Set the sec var to contain the correct time
        self._sec.set(self._time_seconds)
        self.update()
        self._time_seconds -= 1
        self.after(1000, self._update_clock)
