import datasets
import random
import sys


class Game:
    def __init__(self):
        self.score = 0
        self.wrongGuess = 10
        self.input = None
        self.lastInput = None
        self._loadData()

    def _loadData(self):
        self.datasets = datasets.getData()
        print(self.datasets)

    def _displayMenu(self):
        print('Select Category:')
        categories = [data['category'] for data in self.datasets]
        print('\n'.join(categories))

        categoryIndex = input('>')
        while not categoryIndex.isdigit() or int(categoryIndex) not in range(1, len(categories)+1):
            print('select category')
            categoryIndex = input('>  ')

        self.data = self.datasets[int(categoryIndex) - 1]
        print('You select {}'.format(self.data['category']))

        self.words = self.data['words']

        word = self.words[random.randint(0, len(self.words))]
        self.setWord(word['name'], word['hint'])

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

        self._displayMenu()

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
                print('Answer: {}'.format(self.name))
                print('Your score is {}'.format(self.score))
                exit()
            self.lastInput = self.input


game = Game()
game.run()
