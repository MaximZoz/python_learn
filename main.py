class MoneyBox:
    v = 0  # количество монет

    def __init__(self, capacity):
        self.capacity = capacity  # вместимость копилки

    def can_add(self, v):
        """
        Вмещаются ли монеты в копилку
        :param v: количество монет
        :return: boolean
        """
        return self.v + v <= self.capacity

    def add(self, v):  # добавляем монеты в копилку
        if self.can_add(v):
            self.v += v
