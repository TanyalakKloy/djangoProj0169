class Product:
    def __init__(self, id, brand, type, model, color, price, warranty, vat, net):
        self.id = id
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.warranty = warranty
        self.type = type
        self.vat = vat
        self.net = net

    def __str__(self):
        return  "ID.{}, Name.{}, Brand.{}, Color.{}, Price.{}, Warranty.{}, Vat.{}, Net.{}"\
            .format(self.id, self.brand, self.model, self.color,  self.price, self.warranty, self.vat, self.net)

