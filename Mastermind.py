#Mastermind game
class mastermind(object):
    def __init__(self):
        #yellow, blue, green, red, white, orange
        self.colors = ['y','b','g','r','w','o']
        self.past = []
        self.turns = 0
        self.answer =[]
        self.guess = []
        self.clue = []

    def instructions(self):
        print('Rules:')
        print('1. Computer picks 4 colors\n',
              '2. The colors are yellow, blue, green, red, white, and orange\n',
              '3. User also picks 4 colors trying to get close to the computers choices.\n',
              "4. If the user has colors close to the computer's the computer would put a b or w.\n",
              '5. b symbolizes black which means a correct color and its in the right place. \n ',
              '6. w symbolizes white which means there is a correct color. \n',
              '7. The position of the clue does not correspond to the position it is in. \n',
              '8. To take a turn type the first initial of the four colors you want to chose \n',
              '9. Type help to read the instructions again \n',
              )
        

    def print_board(self):
        pass

    def check_solutions(self):
        pass

    def inc_turn(self):
        pass

    def simulate_game(self):
        self.instructions(self)



game = mastermind()

#after 20 turns
while(20 == game.turns):
    game.simulate_game()




