from tkinter import *
from functools import partial  # To prevent unwanted windows

import random

class Quiz:
    def __init__(self):

        # Formatting variables...
        background_color = "cyan"

        self.starting_question = IntVar()
        self.starting_question.set(0)

        self.low_amount = IntVar()
        self.low_amount.set(0)

        self.high_amount = IntVar()
        self.high_amount.set(0)

        # Quiz frame
        self.quiz_frame = Frame(bg=background_color, height=300, width=300,
                                pady=10, padx=10)
        self.quiz_frame.grid(row=4)

        # Entry Frame
        self.entry_frame = Frame(bg=background_color, height=300, width=300,
                                 pady=10, padx=10)
        self.entry_frame.grid(row=2)

        self.error_frame = Frame(bg=background_color, height=300, width=300,
                                   pady=10, padx=10)
        self.error_frame.grid(row=3)

        # Heading (row 0)
        self.maths_label = Label(text="Math Quiz",
                                 font="Arial 32 bold",
                                 bg="cyan",
                                 padx=10, pady=10)
        self.maths_label.grid(row=0)

        # Entry (for numbers they wanna play between)(row 1)
        self.amount_error_label = Label(self.error_frame, font="arial 10 italic",
                                        text="", bg=background_color)
        self.amount_error_label.grid(row=5, columnspan=6)

        self.entry_label_1 = Label(self.entry_frame, text="Number Of Questions", font="Arial 10",
                                   bg="cyan",pady=1)
        self.entry_label_1.grid(row=1, column=2, columnspan=3)
        self.amount_entry = Entry(self.entry_frame, width=5,
                                  font="Arial 10 bold", bg="white")
        self.amount_entry.grid(row=1)

        self.entry_label_1 = Label(self.entry_frame, text="Low Number", font="Arial 10",
                                   bg="cyan",pady=1)
        self.entry_label_1.grid(row=2, column=2, columnspan=3)
        self.low_num_entry = Entry(self.entry_frame, width=5,
                                   font="Arial 10 bold", bg="white")
        self.low_num_entry.grid(row=2)

        self.entry_label_1 = Label(self.entry_frame, text="High Number", font="Arial 10",
                                   bg="cyan",pady=1)
        self.entry_label_1.grid(row=3, column=2, columnspan=3)
        self.high_num_entry = Entry(self.entry_frame, width=5,
                                    font="Arial 10 bold", bg="white")
        self.high_num_entry.grid(row=3)


        # Game Buttons (row 2)
        self.game_buttons_frame = Frame(self.quiz_frame, bg="cyan")

        self.game_buttons_frame.grid(row=3, pady=10)

        self.question_amount_btn = Button(self.game_buttons_frame, text="Enter", font="Arial 10", width=7,
                                          bg="#FC08FC", padx=10, pady=10, command=self.check_question)
        self.question_amount_btn.grid(row=0, column=1 )

        self.addition_btn = Button(self.game_buttons_frame,
                                   text="ADDITION", font="Arial 10", width=10,
                                   bg="#05FC26", padx=10, pady=10,
                                   command=lambda: self.to_game(1))
        self.addition_btn.grid(row=1, column=0)

        self.multiplication_btn = Button(self.game_buttons_frame,
                                         text="MULTIPLICATION", font="Arial 10", width=10,
                                         bg="#FCFC0F", padx=10, pady=10,
                                         command=lambda: self.to_game(3))
        self.multiplication_btn.grid(row=1, column=2)

        self.help_frame = Frame(self.quiz_frame)
        self.help_frame.grid(row=3)

        self.addition_btn.config(state=DISABLED)
        self.multiplication_btn.config(state=DISABLED)

        # stats / help button frame (row 5)
        self.stats_help_frame = Frame(self.quiz_frame)
        self.stats_help_frame.grid(row=4, pady=10)

        self.help_button = Button(self.stats_help_frame, font="Arial 12", bg="#FC430A",
                                  text="How To Play", width=12, command=self.help)
        self.help_button.grid(row=0, column=1)

    def help(self):
        print("you need help")
        get_help = Help(self)
        get_help.help_text.configure()

    def check_question(self):
        starting_question = self.amount_entry.get()
        low_amount = self.low_num_entry.get()
        high_amount = self.high_num_entry.get()

        # Set error background colour (and assum that there are no
        # error at the start
        error_back = "#ffafaf"
        has_error = "no"
        error_feedback = ""

        # change background to white (for testing purposes) ...
        self.amount_entry.config(bg="white")
        self.amount_error_label.config(text="")
        self.low_num_entry.config(bg="white")
        self.low_num_entry.config(text="")
        self.high_num_entry.config(bg="white")
        self.high_num_entry.config(text="")

        self.addition_btn.config(state=DISABLED)
        self.multiplication_btn.config(state=DISABLED)

        try:
            starting_question = int(starting_question)

            if starting_question < 5:
                has_error = "yes"
                error_feedback = "You need to enter a number"
            elif starting_question > 20:
                has_error = "yes"
                error_feedback = "unfortunately that's to high"


        except ValueError:
            has_error = "yes"
            error_feedback = "Please fill the boxes with whole numbers"

        try:
            low_amount = int(low_amount, )

            if low_amount < -100:
                has_error = "yes"
                error_feedback = "Your low number cant be lower then -100"
            elif low_amount > 99:
                has_error = "yes"
                error_feedback = "unfortunately your low number can not exceed 99 "


        except ValueError:
            has_error = "yes"
            error_feedback = "Please fill the boxes with whole numbers"

        try:
            high_amount = int(high_amount)

            if high_amount <= low_amount:
                has_error = "yes"
                error_feedback = "Your high number needs to be greater then your low number"
            elif high_amount > 100:
                has_error = "yes"
                error_feedback = "unfortunately your high number can not exceed 100 "


        except ValueError:
            has_error = "yes"
            error_feedback = "Please fill the boxes with whole numbers"

        if has_error == "yes":
            self.amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)
            self.high_num_entry.config(bg=error_back)
            self.low_num_entry.config(bg=error_back)

        else:
            self.starting_question.set(starting_question)
            self.low_amount.set(low_amount)
            self.high_amount.set(high_amount)
            self.addition_btn.config(state=NORMAL)
            self.multiplication_btn.config(state=NORMAL)
            self.low_num_entry.config(state=DISABLED)
            self.high_num_entry.config(state=DISABLED)
            self.amount_entry.config(state=DISABLED)

    def to_game(self, op):
        starting_question = self.amount_entry.get()
        low_amount = self.low_num_entry.get()
        high_amount = self.high_num_entry.get()
        print(starting_question, low_amount, high_amount)

        Game(self, op, starting_question, low_amount, high_amount)
