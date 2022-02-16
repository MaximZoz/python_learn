import guess_the_number

maxCount = int(input('ведите максимальное количество попыток: '))
myGame = guess_the_number.Game(maxCount)
myGame.Start()
