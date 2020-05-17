class Jack:
    type = 'mechanical'

    def __init__(self, weight=None, max_lifting_weight=None, producer=None,  color=None, price_in_uah=None, model=None, max_hight=None, min_hight=None):
        self._weight = weight
        self._max_lifting_weight = max_lifting_weight
        self._producer = producer
        self._color = color
        self._price_in_uah = price_in_uah
        self._model = model
        self._max_hight = max_hight
        self._min_hight = min_hight

    def __str__(self):
        weight = f'Weight: {self.weight}\n'
        max_lifting_weight = f'Max lifting weight: {self.max_lifting_weight}\n'
        producer = f'Producer: {self.producer}\n'
        color = f'Color: {self.color}\n'
        price_in_uah = f'Price in UAH: {self.price_in_uah}\n'
        model = f'Model: {self.model}\n'
        max_hight = f'Max hight of Jack: {self.max_hight}\n'
        min_hight = f'Min hight of Jack:{self.min_hight}\n'
        type = f'Type: {Jack.type}\n'
        return weight + max_lifting_weight + producer + color + price_in_uah + model + max_hight + min_hight + type

    def __repr__(self):
        weight = f"Weight('{self.weight}')\n"
        max_lifting_weight = f"Max lifting weight('{self.max_lifting_weight}')\n"
        producer = f"Producer('{self.producer}')\n"
        color = f"Color('{self.color}')\n"
        price_in_uah = f"Price in UAH('{self.price_in_uah}')\n"
        model = f"Model('{self.model}')\n"
        max_hight = f"Max hight of Jack('{self.max_hight}')\n"
        min_hight = f"Min hight of Jack('{self.min_hight}')\n"
        type = f"Type('{Jack.type}')\n"
        return weight + max_lifting_weight + producer + color + price_in_uah + model + max_hight + min_hight + type

    def __del__(self):
        print("Deleted " + self.__class__.__name__ + " | ID: " + str(id(self)))
        return

    @staticmethod
    def get_type_of_zoom():
        return Jack.type

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def max_lifting_weight(self):
        return self._max_lifting_weight

    @max_lifting_weight.setter
    def max_lifting_weight(self, max_lifting_weight):
        self._max_lifting_weight = max_lifting_weight

    @property
    def producer(self):
        return self._producer

    @producer.setter
    def producer(self, producer):
        self._producer = producer

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def price_in_uah(self):
        return self._price_in_uah

    @price_in_uah.setter
    def price_in_uah(self, price_in_uah):
        self._price_in_uah = price_in_uah

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def max_hight(self):
        return self._max_hight

    @max_hight.setter
    def max_hight(self, max_hight):
        self._max_hight = max_hight

    @property
    def min_hight(self):
        return self._min_hight

    @min_hight.setter
    def min_hight(self, min_hight):
        self._min_hight = min_hight