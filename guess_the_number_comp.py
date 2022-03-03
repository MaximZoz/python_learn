import guess_the_number_user


class Game(guess_the_number_user.Game):
    def Start(self) -> None:
        print('загадай число')
        while True:
            guess = ((self.minGuess + self.maxGuess) // 2)  # число, которое загадал комп
            print(f'Ты загадал число {guess}?')
            while True:  # валидируем введенное значение
                try:
                    answer = input('введите: <  , > , =\n')
                    if answer != '<' and answer != '>' and answer != '=':
                        raise Exception
                    break
                except Exception:
                    print('нужно ввести символ: < , > , =')

            if self.count == self.maxCount:
                print(f'комп не отгадал число за {self.maxCount} попыток, ты выиграл')
                break

            elif answer == '<':
                self.count += 1  # увеличиваем счетчик числа попыток
                self.maxGuess = int(guess - 1)
                guess = ((self.minGuess + self.maxGuess) // 2)

            elif answer == '>':
                self.count += 1  # увеличиваем счетчик числа попыток
                self.minGuess = guess + 1
                guess = ((self.minGuess + self.maxGuess) // 2)

            else:
                print('комп выиграл!')
                break
