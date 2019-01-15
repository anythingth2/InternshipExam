from data import Data


class Game:

    def __init__(self):

        self.setWord('United State !@', 'World')
        self.score = 0
        self.wrongGuess = 10
        self.input = None
        self.lastInput = None

    def _displayMenu(self):
        pass

    def setWord(self, name, hint):
        self.name = name
        self.hint = hint
        self.answer = [False for i in range(len(self.name))]
        for index, char in enumerate(self.name):
            if not char.isalpha():
                self.answer[index] = True

    def _check(self, inputChar):
        if inputChar == None:
            return -1
        for index, nameChar in enumerate(self.name.lower()):
            if not self.answer[index] and nameChar == inputChar.lower():
                return index
        return -1

    def checkHang(self):
        index = self._check(self.input)
        if index != -1:
            self.correct(index)
        else:
            self.incorrect()

    def correct(self, index):
        self.answer[index] = True
        self.score += 1

    def incorrect(self):
        self.wrongGuess -= 1

    def hang(self, result=True):
        secret = ''
        for i in range(len(self.name)):
            if self.answer[i] or not self.name[i].isalpha():
                secret += self.name[i]
            else:
                secret += '_'
        secret = ' '.join(list(secret))

        message = '{}\t score {}, remaining wrong guess {}'.format(
            secret, self.score, self.wrongGuess)

        if not result:
            message += 'wrong guessed: ' + self.lastInput

        print(message)

    def checkWinOrLose(self):
        if all(self.answer):
            return True
        elif self.wrongGuess < 0:
            return False
        else:
            return None

    def run(self):
        print('Hint: "{}"\n'.format(self.hint))
        while True:
            self.hang()
            self.input = input('> ')
            if not self.input.isalpha() or len(self.input) != 1:
                print('Please type alphabet character')
                continue
            
            self.checkHang()
            status = self.checkWinOrLose()
            if status != None:
                if status:
                    print('win')
                else:
                    print('lose')
                exit()
            self.lastInput = self.input

    def start(self):
        pass


game = Game()
game.run()
