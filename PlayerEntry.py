
from BaseFrame import *
from Countdown import Countdown
import dbconnect
import json


class PlayerEntry(MyBaseFrame):
    # TODO: move the lists to main3.py or Container or a different class ?
    red_ids, red_names, green_ids, green_names = ([] for i in range(4))

    header_text = "Press enter to get your code name if you have played before, otherwise, submit your team before playing"
    subheader_text = "Press F5 to start game once teams have been submitted"

    def __init__(self, master: Tk):
        """[summary]

        Args:
            master (Tk): Widget that is directly resposible for owning this widget (Container)
        """
        # Set Object Attributes
        super().__init__(master)

        # Configure
        # - Pull Names Keystroke
        self.bind_all("<Return>", lambda event=NONE: self.pull_names(event))

        # - Countdown Keystroke
        self.bind_all("<KeyPress-F5>",
                      lambda event=NONE: self.next_screen(event))

        # Populate
        header = Header(self, self.header_text, self.subheader_text)
        master_widget = MasterWidget(self)

        # Layout
        header.grid(column=1, row=0, sticky='NSEW')
        master_widget.grid(column=1, row=1, sticky='NSEW')

    def pull_names(self, *event):
        records = []

        for i in range(15):
            if len(self.red_ids[i].get()) != 0:
                red_id = int(self.red_ids[i].get())
                red_name = self.red_names[i].get()
                record = (red_id, red_name)
                records.append(record)
            if len(self.green_ids[i].get()) != 0:
                green_id = int(self.green_ids[i].get())
                green_name = self.green_names[i].get()
                record = (green_id, green_name)
                records.append(record)

        newRecords = dbconnect.connect(records)

        for x in newRecords:
            id = x[0]
            name = x[1]
            for i in range(15):
                if len(self.red_ids[i].get()) != 0:
                    if (int(self.red_ids[i].get()) == id):
                        self.setName(self.red_names[i], name)
                if len(self.green_ids[i].get()) != 0:
                    if (int(self.green_ids[i].get()) == id):
                        self.setName(self.green_names[i], name)

    def setName(self, name, text):
        name.delete('0', 'end')
        name.insert('0', text)

    def next_screen(self, *event):
        redTeam = []
        greenTeam = []
        redID = []
        greenID = []
        for i in range(NUM_PLAYERS):
            if len(self.red_ids[i].get()) != 0:
                name = self.red_names[i].get()
                id = self.red_ids[i].get()
                redTeam.append(name)
                redID.append(id)
            if len(self.green_ids[i].get()) != 0:
                name = self.green_names[i].get()
                id = self.green_ids[i].get()
                greenTeam.append(name)
                greenID.append(id)
        with open('redTeam.txt', 'w') as file:
            file.write(json.dumps(redTeam))
        with open('greenTeam.txt', 'w') as file:
            file.write(json.dumps(greenTeam))
        with open('redID.txt', 'w') as file:
            file.write(json.dumps(redID))
        with open('greenID.txt', 'w') as file:
            file.write(json.dumps(greenID))

        self.master.switch_frame(Countdown)


class MasterWidget(Frame):
    def __init__(self, master: MyBaseFrame):
        """Creates the action grid in the (1,1) cell that contains the table titles,
        as well as the player entry section

        Args:
            master (MyBaseFrame): [description]
        """
        # Set Object Attributes
        super().__init__(master)

        # Configure
        self.config(borderwidth=1, bg='black')

        self.columnconfigure([0, 3], weight=1, minsize=1)   # ID Cols
        self.columnconfigure(2, weight=2, minsize=1)        # Filler Col
        self.columnconfigure([1, 4], weight=5, minsize=1)   # Team Cols
        self.rowconfigure(0, weight=2)                      # Title Row
        self.rowconfigure(tuple(range(1, 16)), weight=1)    # Entry Rows
        self.rowconfigure(16, weight=3, minsize=15)         # Button Row

        # Populate
        red_ids_label = TableHeaderLabel(self, "IDS", 'red')
        red_team_label = TableHeaderLabel(self, "RED TEAM", 'red')
        green_ids_label = TableHeaderLabel(self, "IDS", 'green')
        green_team_label = TableHeaderLabel(self, "GREEN TEAM", 'green')

        # - Button Creation
        left_button_frame = Frame(self, bg='black')
        left_button_frame.columnconfigure([0, 1, 2], weight=2)
        right_button_frame = Frame(self, bg='black')
        right_button_frame.columnconfigure([0, 1, 2], weight=1)
        exit_game_btn = Button(left_button_frame, text="<F1>\nExit Game", font=SUBHEADER_FONT,
                               width=20, bd='3', command=lambda: self.master.master.destroy())
        send_data_btn = Button(left_button_frame, text="<F3>\nSubmit Teams", font=SUBHEADER_FONT,
                               width=20, bd='3', command=lambda: self.master.pull_names())
        pull_data_btn = Button(right_button_frame, text="<Return>\nGet Names", font=SUBHEADER_FONT,
                               width=20, bd='3', command=lambda: self.master.pull_names())
        start_game_btn = Button(right_button_frame, text="<F5>\nStart Game", font=SUBHEADER_FONT,
                                width=20, bd='3', command=lambda: self.master.master.switch_frame(Countdown))

        # Layout
        red_ids_label.grid(row=0, column=0, sticky='NSEW')
        red_team_label.grid(row=0, column=1, sticky='NSEW')
        green_ids_label.grid(row=0, column=3, sticky='NSEW')
        green_team_label.grid(row=0, column=4, sticky='NSEW')

        # - Left Button Alignment
        left_button_frame.grid(row=17, column=0, columnspan=2, sticky='NSEW')
        exit_game_btn.grid(row=0, column=0)
        send_data_btn.grid(row=0, column=2)

        # - Right Button Alignment
        right_button_frame.grid(row=17, column=3, columnspan=2, sticky='NSEW')
        pull_data_btn.grid(row=0, column=0)
        start_game_btn.grid(row=0, column=2)

        # Entry Fieds
        self.create_entry_fields()

    def create_entry_fields(self):
        for i in range(1, 16):
            red_id = Entry(self, width=3)
            red_id.grid(row=i, column=0, sticky='NSEW')
            self.master.red_ids.append(red_id)

        for i in range(1, 16):
            red_name = Entry(self, width=1)
            red_name.grid(row=i, column=1, sticky='NSEW')
            self.master.red_names.append(red_name)

        for i in range(1, 16):
            green_id = Entry(self, width=3)
            green_id.grid(row=i, column=3, sticky='NSEW')
            self.master.green_ids.append(green_id)

        for i in range(1, 16):
            green_name = Entry(self,  width=1)
            green_name.grid(row=i, column=4, sticky='NSEW')
            self.master.green_names.append(green_name)


class ButtonHolder(Frame):

    def __init__(self, master: Frame):
        """Frame to hold buttons - contained in the MasterWidget

        Args:
            master (Frame): Frame widget thats directly owns this.
        """
        # Set Object Attributes
        super().__init__(master)

        # Configure
        self.config(bg='black')

        self.rowconfigure(1, weight=1)
        self.columnconfigure(tuple(range(8)), weight=1, minsize=5)

        # Populate
        exit_game_btn = Button(self, text="<F1> - Exit Game", font=SUBHEADER_FONT,
                               width=10, height=2, bd='3', command=lambda: self.master.master.master.destroy())
        send_data_btn = Button(self, text="<F3> - Submit Teams", font=SUBHEADER_FONT,
                               width=10, height=2, bd='3', command=lambda: self.master.master.send_data())
        pull_data_btn = Button(self, text="<Return> - Get Names", font=SUBHEADER_FONT,
                               width=10, height=2, bd='3', command=lambda: self.master.master.pull_names())
        start_game_btn = Button(self, text="<F5> - Start Game", font=SUBHEADER_FONT, width=10,
                                height=2, bd='3', command=lambda: self.master.master.next_frame())

        # Layout
        exit_game_btn.grid(column=0, row=0, sticky='NSEW')
        send_data_btn.grid(column=3, row=0, sticky='NSEW')
        pull_data_btn.grid(column=5, row=0, sticky='NSEW')
        start_game_btn.grid(column=7, row=0, sticky='NSEW')
