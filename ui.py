THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizzBrainInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title('Quizz Brain')
        self.quiz = quiz_brain
        self.answer = None
        # window.minsize(400,600)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=250, text="Click the Button to Start",
                                                     fill=THEME_COLOR, font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # pady bo trong grid
        self.score_label = Label(text="Score: 0/0", bg=THEME_COLOR, font=("Time New Roman", 20))
        self.score_label.grid(row=0, column=1)
        # BUTTON
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, bg=THEME_COLOR, command=self.start_game)
        self.false_button.grid(row=2, column=0)
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, bg=THEME_COLOR, command=self.start_game)
        self.true_button.grid(row=2, column=1)
        self.window.mainloop()

    def start_game(self):
        self.get_next_question()
        self.true_button.config(command=self.true_click)
        self.false_button.config(command=self.false_click)

    def score_update(self):
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

    def get_next_question(self):
        if self.quiz.still_has_questions() == True:
            self.canvas.config(bg='white')
            q_data = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=f"{q_data}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(command=self.passed)
            self.false_button.config(command=self.passed)

    def passed(self):
        pass

    def true_click(self):
        self.answer = 'True'
        is_right = self.quiz.check_answer(self.answer)
        self.give_feedback(is_right)
        self.score_update()

    def false_click(self):
        self.answer = 'False'
        is_right = self.quiz.check_answer(self.answer)
        self.give_feedback(is_right)
        self.score_update()

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
