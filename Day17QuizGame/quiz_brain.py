class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        answer = input(
            f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)? "
        )
        self.check_answer(answer)
        self.question_number += 1

    def still_has_questions(self):
        if self.question_number != len(self.question_list):
            return True
        return False

    def check_answer(self, user_answer):
        if (
            user_answer.lower()
            == self.question_list[self.question_number].answer.lower()
        ):
            print("You got it right!")
            self.score += 1
            print(f"Your score is: {self.score}/{self.question_number+1}")
        else:
            print("You got it wrong")
            print(f"Answer is: {self.question_list[self.question_number].answer}")
            print(f"Your score is: {self.score}/{self.question_number+1}")
