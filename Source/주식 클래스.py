class Stock:
    def __init__(self, name, symbol, previousPrice, currentPrice) :
        self.name = name
        self.symbol = symbol
        self.previousPrice = previousPrice
        self.currentPrice = currentPrice

    def getname(self):
        return self.name

    def getSymbol(self):
        return self.symbol

    def getPreviousPrice(self):
        return self.previousPrice

    def getCurrentPrice(self):
        return self.currentPrice

    def setPreviousPrice(self, previousPrice):
        self.previousPrice = previousPrice

    def setCurrentPrice(self, crrentPrice):
        self.crrentPrice = currentPrice

    def getChangePercent(self):
        return format((self.currentPrice - self.previousPrice) * 100 / self.previousPrice, "5.2f") + "%"

def main():
    stock = Stock("Intel Corporation", "INTC", 20500, 20350)
    print("가격 변동률은", stock.getChangePercent(), "입니다.")

main()
