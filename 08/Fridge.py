class Fridge:
    isOpened = False
    foods = []

    def open(self):
        self.isOpened = True
        print('[ INFO ] 냉장고 문이 열렸습니다.')

    def put(self, thing):
        if self.isOpened == False:
            print('[ FAIL ] 냉장고 문이 닫혀 있습니다.')
        else:
            self.foods.append(thing)
            print('[ OK ] 냉장고 안에  {thing}을 넣었습니다.')


class Food:
    pass