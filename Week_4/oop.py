class Car:

    wheels = 4
    vendor = "cfao"

    def __init__(self,color,model,yom):

        self.color = color
        self.model = model
        self.yom = yom

car1 = Car("Indigo","Vezel",2019)

car2 = Car("Blue","Benz",2020)

car3 = Car("Red","Volvo",2018)

print(car1.color)