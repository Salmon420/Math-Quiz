from tkinter import *
from functools import partial  # To prevent unwanted windows

import random




class Game:
    def __init__(self, partner, op, starting_question, low_amount, high_amount):

        starting_question = int(starting_question)
        questions_played = int(1)
        how_many_right = int(0)

        self.correct = IntVar()
        self.correct.set(0)

        low_amount = int(low_amount)
        high_amount = int(high_amount)
        self.history_questions = []
        background_color = "cyan"

        op = int(op)

        if op == 1:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} + {}".format(hi_lo_num, hi_lo_num2)
            var_correct = hi_lo_num + hi_lo_num2
            self.correct.set(var_correct)
            op_text = "Addition"
        elif op == 3:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} x {}".format(hi_lo_num, hi_lo_num2)
            var_correct = hi_lo_num * hi_lo_num2
            self.correct.set(var_correct)
            op_text = "Multiplication"

        self.history_questions.append(questions)

        # disable button
        partner.addition_btn.config(state=DISABLED)
        partner.multiplication_btn.config(state=DISABLED)
        partner.help_button.config(state=DISABLED)

        # Set up Geo game one
        self.addition_box = Toplevel()

        # Set up GUI Frame
        self.game_frame = Frame(self.addition_box, width=300, bg=background_color)
        self.game_frame.grid()
        # Set up Geo Instruction heading (row 0)
        self.heading = Label(self.game_frame, text=op_text,
                             font="arial 20 bold", bg=background_color)
        self.heading.grid(row=0)
        # Geo text (label, row 1)
        self.game = Label(self.game_frame,
                          text="Fill the boxes",
                          justify=LEFT, width=50, bg=background_color, wrap=200)
        self.game.grid(row=1)

        self.ask_questions_frame = Frame(self.game_frame, bg=background_color)
        self.ask_questions_frame.grid(row=1)

        self.get1_label = Label(self.ask_questions_frame,
                                text=questions,
                                font="arial 10 bold", fg="black", bg=background_color)
        self.get1_label.grid(row=1)

        self.game_entry = Entry(self.ask_questions_frame, font="arial 15 bold")
        self.game_entry.grid(row=2)

        self.dismiss_export_frame = Frame(self.game_frame, bg=background_color)
        self.dismiss_export_frame.grid(row=2)

        # Dismiss button (row 4)
        self.dismiss_btn = Button(self.dismiss_export_frame, text="Dismiss", width=10, bg="#FAD9D5",
                                  font="arial 10 bold", pady=7,
                                  command=partial(self.close_game, partner))
        self.dismiss_btn.grid(row=1)
        self.check_ans_btn = Button(self.dismiss_export_frame, text="Check Answer", font="arial 10 bold", fg="black",
                                    bg="#D0CEE2", pady=7, width=13,
                                    command=lambda: self.check_ans(low_amount, high_amount, op, starting_question,
                                                                   questions_played, how_many_right,
                                                                   self.history_questions))
        self.check_ans_btn.grid(row=1, column=1)

    def check_ans(self, low_amount, high_amount, op, starting_question, questions_played, how_many_right,
                  history_questions):
        answer = self.game_entry.get()
        self.game_entry.config(state=DISABLED)

        # Set error background colour
        # error at the start
        error_back = "#ffafaf"
        has_error = "no"
        error_feedback = ""

        var_correct = self.correct.get()

        # change background to white (for testing purposes) ...
        self.check_ans_btn.config(bg="white")
        self.check_ans_btn.config(text="")

        try:
            answer = int(answer)
            correct = int(var_correct)
            self.history_questions.append(answer)

            if answer != correct:
                has_error = "yes"
                self.feedback_label = Label(self.ask_questions_frame, text="Wrong answer ",
                                            font="arial 10 bold", fg="black", bg="cyan", pady=8, width=25)
                self.feedback_label.grid(row=3)

            elif answer == correct:
                has_error = "no"
                self.feedback_label = Label(self.ask_questions_frame, text=" That's the right answer",
                                            font="arial 10 bold", fg="black", bg="cyan", pady=7, width=25)
                self.feedback_label.grid(row=3)
                how_many_right += 1

        except ValueError:
            has_error = "yes"
            self.feedback_label = Label(self.ask_questions_frame, text=" No answer was given",
                                        font="arial 10 bold", fg="black", bg="cyan", pady=7, width=25)
            self.feedback_label.grid(row=3)

        if questions_played >= starting_question:
            self.finished_btn = Label(self.dismiss_export_frame, text="Finished", font="arial 10 bold", fg="black",
                                      bg="cyan", pady=9, width=14)
            self.finished_btn.grid(row=1, column=1)
            self.export_btn = Button(self.dismiss_export_frame, text="Export", font="arial 10 bold", fg="black",
                                     bg="#D0CEE2", pady=7, width=10,
                                     command=lambda: self.export(low_amount, high_amount, questions_played,
                                                                 how_many_right, history_questions))
            self.export_btn.grid(row=1, column=2)
        else:
            self.check_ans_btn.config(text="")
            self.next_btn = Button(self.dismiss_export_frame, text="Next", font="arial 10 bold", fg="black",
                                   bg="#D0CEE2", pady=7, width=13,
                                   command=lambda: self.next(low_amount, high_amount, op, starting_question,
                                                             questions_played, how_many_right, history_questions))
            self.next_btn.grid(row=1, column=1)

        self.played_label = Label(self.ask_questions_frame, font="arial 10 bold", fg="black",
                                  bg="cyan", pady=7,
                                  text="Question:{}/{}".format(questions_played, starting_question))
        self.played_label.grid(row=0)

    def next(self, low_amount, high_amount, op, starting_question, questions_played, how_many_right, history_questions):
        starting_question = int(starting_question)
        self.game_entry.config(state=NORMAL)
        self.game_entry.delete(0, 'end')

        if op == 1:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} + {}".format(hi_lo_num, hi_lo_num2)
            self.get1_label.config(text=questions)
            var_correct = hi_lo_num + hi_lo_num2
            self.correct.set(var_correct)
            questions_played += 1
            print(questions_played)
        elif op == 2:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} - {}".format(hi_lo_num, hi_lo_num2)
            self.get1_label.config(text=questions)
            var_correct = hi_lo_num - hi_lo_num2
            self.correct.set(var_correct)
            questions_played += 1
        elif op == 3:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} x {}".format(hi_lo_num, hi_lo_num2)
            self.get1_label.config(text=questions)
            var_correct = hi_lo_num * hi_lo_num2
            self.correct.set(var_correct)
            questions_played += 1

        self.history_questions.append(questions)

        self.check_ans_btn = Button(self.dismiss_export_frame, text="Check Answer", font="arial 10 bold", fg="black",
                                    bg="#D0CEE2", pady=7, width=13,
                                    command=lambda: self.check_ans(low_amount, high_amount, op,
                                                                   starting_question, questions_played, how_many_right,
                                                                   history_questions))
        self.check_ans_btn.grid(row=1, column=1)

    def close_game(self, partner):
        # Put help button back to normal
        partner.addition_btn.config(state=DISABLED)
        partner.question_amount_btn.config(state=NORMAL)
        partner.multiplication_btn.config(state=DISABLED)
        partner.help_button.config(state=NORMAL)
        partner.low_num_entry.config(state=NORMAL)
        partner.high_num_entry.config(state=NORMAL)
        partner.amount_entry.config(state=NORMAL)

        self.addition_box.destroy()

    def export(self, low_amount, high_amount, questions_played, how_many_right, history_questions):
        Export(self, low_amount, high_amount, questions_played, how_many_right, history_questions)

