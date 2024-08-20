class Smartphone:
	
    def __init__(self, marka_phone, model_phone, number_phone):
        self.marka = marka_phone
        self.model = model_phone
        self.number = number_phone

    def PrintName(self):
        print("Marka ", self.marka, end=' '), print("Model ", self.model,end=' '), print("Number ", self.number)


sumsung = Smartphone ("Sumsung", "M-555", "+79001234567")
sumsung.PrintName()