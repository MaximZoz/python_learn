import guess_the_number_comp

maxCount = int(input('ведите максимальное количество попыток: '))
# myGame = guess_the_number_user.Game(maxCount)
# myGame.Start()

myGame = guess_the_number_comp.Game(maxCount)
myGame.Start()
