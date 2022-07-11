import random

class Game:
    def __init__ (self, _player1):
        self.player1 = _player1
        # self.player2 = _player2
    
    def roshambo(self, p1_input):
        p2_input = random.randint(1,3)
        if p2_input == 1:
            p2_input = "rock"
        elif p2_input == 2:
            p2_input = "paper"
        elif p2_input == 3:
            p2_input = "scissor"
        if p1_input == "rock":
            if p2_input == "rock":
                return None
            elif p2_input == "paper":
                return f"Player 2 wins"
            elif p2_input == "scissor":
                return f"Player 1 wins"
        elif p1_input == "paper":
            if p2_input == "paper":
                return None
            elif p2_input == "rock":
                return f"Player 1 wins"
            elif p2_input == "scissor":
                return f"Player 2 wins"
        elif p1_input == "scissor":
            if p2_input == "scissor":
                return None
            elif p2_input == "paper":
                return f"Player 1 wins"
            elif p2_input == "rock":
                return f"Player 2 wins"



    # def roshambo(self, input_p1, input_p2):
    #     if input_p1 == "rock" and input_p2 == "scissors":
    #         return f"Player 1 wins by playing {input_p1}"
    #     elif input_p1 == "rock" and input_p2 == "paper":
    #         return f"Player 2 wins by playing {input_p2}"
    #     elif input_p1 == "paper" and input_p2 == "rock":
    #         return f"Player 1 wins by playing {input_p1}"
    #     elif input_p1 == "paper" and input_p2 == "scissors":
    #         return f"Player 2 wins by playing {input_p2}"
    #     elif input_p1 == "scissors" and input_p2 == "paper":
    #         return f"Player 1 wins by playing {input_p1}"
    #     else:
    #         if input_p1 == "scissors" and input_p2 == "rock":
    #             return f"Player 2 wins by playing {input_p2}"
    
    # # def rock_vs_rock(input_p1, input_p2):
    #     if input_p1 == "rock" and input_p2 == "rock":
    #         return None
    
    # def paper_vs_paper(input_p1, input_p2):
    #     if input_p1 == "paper" and input_p2 == "paper":
    #         return None
    
    # def scissors_vs_scissors(input_p1, input_p2):
    #     if input_p1 == "scissors" and input_p2 == "scissors":
    #         return None
    