
class GFXCard:
    def __init__(self, title, price, score):
        self.title = title
        self.brand = title.split()[0]
        self.category = title.split()[1]
        self.price = price
        self.score = score
        self.value = score/price
