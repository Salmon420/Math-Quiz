from tkinter import *
from functools import partial # To prevent unwanted videos
import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.starting_equation = IntVar()
        self.starting_equation.set(0)

        # Math Quiz Heading (row 0)
        self.Math_Quiz_label = Label(self.start_frame, text="Maths Quiz",
                                        font="Arial 19 bold")
        self.Math_Quiz_label.grid(row=0)

        # Initial Instructions(row 1)
        self.math_instructions = Label(self.start_frame,
                                        font="Arial, 10 italic",
                                        text="Please enter an amount "
                                             "of questions (between 1 and 50 ) in the box "
                                             "below. Then choose the type of equation"
                                             "you would like to do",
                                             wrap=275, justify=LEFT, padx=10, pady=10)
        self.math_instructions.grid(row=1)

        # Entry box...(row=2)
        self.get_question_frame = Frame(self.start_frame, width=200)
        self.get_question_frame.grid(row=2)

        self.start_quiz_entry = Entry(self.get_question_frame,
                                      font="Arial 19 bold", width=10)
        self.start_quiz_entry.grid(row=0, column=0)

        self.add_equation_button = Button(self.get_question_frame,
                                          font="Arial 19 bold",
                                          text="Number Of Equations",
                                          command=self.check_equation)
        self.add_equation_button.grid(row=0, column=1)

        self.equation_error_label = Label(self.get_question_frame, fg="maroon",
                                          text="", font="Arial 10 bold", wrap=275,
                                          justify=LEFT)
        self.equation_error_label.grid(row=1, columnspan=2, pady=5)

        # Button frame (row 3)
        self.level_frame = Frame(self.start_frame)
        self.level_frame.grid(row=3)

        self.maths_instructions = Label(self.start_frame, font="Arial 19 italic",
                                        text="Please select the type of equation below to start.")
        self.maths_instructions.grid(row=2)



        # Buttons goes here
        # Blue Addition Button
        button_font = "Arial 12 bold"
        self.addition_button = Button(self.level_frame, text="Addition",
                                      command=lambda: self.to_game(1),
                                      font=button_font, bg="Blue")
        self.addition_button.grid(row=0, column=0, pady=10)

        # Purple Multiplication Button
        self.Multiplication_button= Button(self.level_frame,text="Multiplication",
                                           command=lambda: self.to_game(2),
                                           font=button_font, bg="purple")
        self.Multiplication_button.grid(row=0, column=1, padx=5, pady=10)

        # Disable all Buttons at start
        self.addition_button.config(state=DISABLED)
        self.Multiplication_button.config(state=DISABLED)

    def check_equation(self):
        starting_equation = self.start_quiz_entry.get()

































































































# main routine
if __name__ == "__main__":
    root = Tk()
    root.title ("Math quiz")
    something = Start(root)
    root.mainloop()

