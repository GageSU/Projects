
from BaseFrame import *
# TODO: Figure out if this import is required here?
from PlayerEntry import PlayerEntry


class SplashScreen(MyBaseFrame):

    def __init__(self, master: Tk,):
        """Splash screen frame - shows for x number of seconds - denoted in main

        Args:
            master (Tk): Widget that is directly resposible for owning this widget - always Container.
        """
        # Set Object Attributes
        super().__init__(master)
        self.image = PhotoImage(file='logo.png')

        # Configure
        self.config(bg='black')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Populate
        splash = Canvas(self, bg='black')
        splash.create_image(SCREEN_WIDTH/2,
                          SCREEN_HEIGHT/2, anchor=CENTER, image=self.image)

        # Layout
        splash.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='NSEW')
        
        # Countdown Begin
        self.set_timer()

    def set_timer(self):
        # Switches the screen after x seconds - denoted in main.py config
        self.after(SPLASHSCREEN_LENGTH *
                   1000, lambda: self.master.switch_frame(PlayerEntry))




