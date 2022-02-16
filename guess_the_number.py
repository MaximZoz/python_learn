import random


class Game:
    count = 0
    number = random.randint(0, 10)  # случайное число от 1 до 10

    def __init__(self, maxCount):
        """
        :param maxCount: количество попыток
        """

        self.maxCount = maxCount  # максимально ко-во попыток

    def Start(self):
        while self.count < self.maxCount:
            guess = int(input('Введи число от 1 до 10: '))
            self.count += 1  # увеличиваем счетчик числа попыток
            if guess < self.number and self.maxCount - self.count != 0:
                print('число больше загаданного, осталось попыток:{0}'.format(self.maxCount - self.count))

            if guess > self.number and self.maxCount - self.count != 0:
                print('число меньше загаданного, осталось попыток: {0}'.format(self.maxCount - self.count))

            if guess == self.number:
                break

        if guess == self.number:
            print('ты отгадал число за {0} попыток!'.format(self.count))
        else:
            print('ты не отгадал число за {0} попыток, загаданноe число: {1}'.format(self.maxCount, self.number))
