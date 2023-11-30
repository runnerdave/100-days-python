from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, padx=10, pady=10)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)

        self.question_text = self.canvas.create_text(150, 125, text="Question goes here", width=250, font=("Arial", 20, "italic"),fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)    

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.press_true)
        self.true_button.grid(row=2, column=0)
        
        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.press_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=f"{self.quiz.next_question()}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            

    def press_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def press_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, lambda: self.canvas.config(bg="white"))
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.get_next_question()