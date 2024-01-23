from tkinter import Tk, Canvas, PhotoImage, Button, Label
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface(Tk):
    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()

        self.quiz = quiz_brain

        self.title("Quizzler")
        self.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,  # width
            125,  # height
            width=280,
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=self.true_image, highlightthickness=0, command=self.true_pressed
        )
        self.true_button.grid(row=2, column=1)

        self.wrong_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(
            image=self.wrong_image, highlightthickness=0, command=self.false_pressed
        )
        self.wrong_button.grid(row=2, column=0)

        self.get_next_question()

        self.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've reached the end of the quiz.\n"
                f"Your final score was {self.quiz.score}!",
            )
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.after(1000, self.get_next_question)
        self.score_label.config(text=f"Score: {self.quiz.score}")
