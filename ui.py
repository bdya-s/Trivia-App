from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_q = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas()
        self.canvas.config(height=250, width=300, selectforeground="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Questions",
            fill=THEME_COLOR,
            font=("Arial", 12, "normal")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text=f"Score: {0}/10", bg=THEME_COLOR, foreground="white")
        self.score_label.grid(column=1, row=0)

        image_true = PhotoImage(file="images/true.png")
        image_false = PhotoImage(file="images/false.png")

        self.button_true = Button(image=image_true, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(column=0, row=2)
        self.button_false = Button(image=image_false, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_q.still_has_questions():
            question = self.quiz_q.next_question()
            self.canvas.itemconfig(self.question_text, text=question, fill=THEME_COLOR)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Game over!\nScore:{self.score}/10", fill=THEME_COLOR)
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz_q.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz_q.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, text="True", fill="white")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}/10")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, text="False", fill="white")
        self.window.after(500, self.get_next_question)






