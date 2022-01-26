from Config import *


class MyBaseFrame(Frame):

    def __init__(self, master: Tk, *args, **kwargs):
        """Basis for all frames - Uses a 3x3 grid to display widgets - 2x2 position used for main interactions.

        Args:
            master (Tk) : Widget that is directly resposible for owning this widget - always Container. 
            header_text (str, optional) : Text to be used in the header position. 
            subheader_text (str, optional) : Text to be used in the subheader position.
            *args : unused
            **kwargs : unused
        """
        # Set Object Attributes
        super().__init__(master)

        # Configure
        self.config(bg='black')

        # - Rows
        self.rowconfigure((0, 2), weight=1)
        self.rowconfigure(1, weight=20)

        # - Columns
        self.columnconfigure((0, 2), weight=1, minsize=5)
        self.columnconfigure(1, weight=18)

        # Testing
        # self.screen_setup_TESTING()

    # DEBUG Function
    def screen_setup_TESTING(self):
        """Layout testing function"""
        label1 = Label(self, bg='red',)
        label1.grid(row=0, column=0, sticky='NSEW')
        label2 = Label(self, bg='red')
        label2.grid(row=1, column=1, sticky='NSEW')
        label3 = Label(self, bg='red')
        label3.grid(row=2, column=2, sticky='NSEW')


class Header(Frame):

    def __init__(self, master: MyBaseFrame, header_text: str = "", subheader_text: str = ""):
        """Creates a label to hold a 1x2 grid to hold header and subheader text.

        Args:
            master (MyBaseFrame): Widget that is directly resposible for owning this widget - contains text information.
            header_text (str, optional) : Text to be used in the header position. 
            subheader_text (str, optional) : Text to be used in the subheader position.
        """
        # Set Object Attributes
        super().__init__(master)

        # Configure
        self.config(borderwidth=0, bg='black')
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1)

        # Populate
        header = Label(self, text=header_text, font=HEADER_FONT,
                       wraplength=750, justify='center', fg='white', bg='black')
        subheader = Label(self, text=subheader_text, font=SUBHEADER_FONT,
                          wraplength=750, justify='center', fg='white', bg='black')

        # Layout
        header.grid(row=0, column=0, sticky='N')
        subheader.grid(row=1, column=0, sticky='N')
        
        
class TableHeaderLabel(Label):

    def __init__(self, master: Frame, text: str, color: str):
        """Table header label class.

        Args:
            master (Frame): Frame widget thats directly owns this.
            text (str): Text to be dispalyed.
            color(str): Team color to be used as text color
        """
        # Set Object Attributes
        super().__init__(master)
        self.text = text
        self.color = color

        # Configure
        self.config(text=self.text, fg=self.color,
                    font=SUBHEADER_FONT, bg='black', justify='center')
