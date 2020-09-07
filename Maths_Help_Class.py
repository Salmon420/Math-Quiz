from tkinter import *
from functools import partial  # To prevent unwanted windows

import random





class Help:
    def __init__(self, partner):
        background_color = "cyan"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Set up child window (ie: help box)
        self.help_box = Toplevel()

        # If user press cross at top, closes export and 'releases' export button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background_color)
        self.help_frame.grid()
        # Set up help heading (row 0)
        self.how_heading = Label(self.help_frame,
                                 text="Help / Instruction",
                                 font="arial 20 bold", bg=background_color)
        self.how_heading.grid(row=0)
        # Help text (label, row 1)
        self.help_text = Label(self.help_frame,
                               text="This is a math game "
                                    " It will help you to learn addition and multiplication \n"
                                    "\n"
                                    "How do you play?\n"
                                    "\n"
                                    "The first box is for the amount of questions  you want\n"
                                    "\n"
                                    "The second box is for the lowest number you want your questions to be\n"
                                    "\n"
                                    "The third box is for the highest number you want your questions to be \n "
                                    "\n"
                                    "you will need to click enter to continue to choose what type of questions"
                                    " you want to play \n ",
                               justify=LEFT, width=50, bg=background_color, wrap=400, font="arial 15 ")
        self.help_text.grid(column=0, row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="#FAD9D5",
                                  font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

