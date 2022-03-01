from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizzInterface:


    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("QuizzGame")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)

        # score label
        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0,column=1)

        # creating the canvas
        self.canvas = Canvas(width=300,height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="SOME QUESTION",
            font=("Arial", 20, "italic")
        )

        # creating the buttons
        self.right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0, bg=THEME_COLOR, command= self.true_button)
        self.right_button.grid(row=2,column=0)

        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, bg=THEME_COLOR, command= self.false_button)
        self.wrong_button.grid(row=2,column=1)

        # calling the question
        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text="The questions ended")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_button(self):
        righ_or_wrong = self.quiz.check_answer("True")
        self.give_feedback(righ_or_wrong)

    def false_button(self):
        righ_or_wrong = self.quiz.check_answer("False")
        self.give_feedback(righ_or_wrong)

    def give_feedback(self,righ_or_wrong ):
        if righ_or_wrong:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.next_question)






