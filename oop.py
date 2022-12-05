class Human:
    #атрибуты уровня класса
    head=1
    body=1
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #метод
    def run(self):
        print(f'{self.name} is run')

hum = Human('амир', 12)
hum.run