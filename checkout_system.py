# Name  : Calum Lim Sheng En
# Date  : 23/11/2019
# Title : Checkout System for Digi-X "Lightning" Assessment Section 2

# A simple class denoting the interface for a simple checkout system
class Checkout:

    # Initialisation of variables
    def __init__(self, pricingRules):
        self.prices =  [] # dynamic variable to update the current price of each item
        for i in range(len(pricingRules)):
            self.prices.append(pricingRules[i])
        self.count = [0,0,0,0]      # array to keep track of count of each scanned item ( assuming that we know the number of SKUs )

    # Function to scan an item given its SKU
    def scan(self,item):
        # increment of count for each item (SKU) given
        # increment or decrement of items depending on the various conditions set
        if item == 'ipd': # bulk discount
            self.count[0] += 1
            if self.count[0] >= 4:
                self.prices[0] = 499.99
                
        elif item == 'mbp': # 1 free vga per mbp
            self.count[1] += 1
            if self.count[3]!=0:
                self.count[3]-=1
            
        elif item == 'atv': # buy 3 atv for the price of 2
            self.count[2] += 1
            if self.count[2] >= 3:
                remainder = self.count[2]%3
                self.count[2] = self.count[2] + remainder - (self.count[2]//3)
            
        elif item == 'vga': # if number of mbp is same as vga then decrement by 1
            self.count[3] += 1


    # Function to compute the total amount needed for all the scanned items
    def total(self):
        n = len(self.count)
        finalPrice = 0
        
        for i in range(n):
            finalPrice += (self.prices[i]*self.count[i])

        finalPrice = "$" + str(finalPrice)
        
        return finalPrice

pricingRules = [549.99,1399.99,109.50,30]

# Example Scenarios

# SKUs Scanned: atv, atv, atv, vga
# Total expected: $249.00
co = Checkout(pricingRules)
co.scan('atv')
co.scan('atv')
co.scan('atv')
co.scan('vga')
print(co.total())

# SKUs Scanned:  atv, ipd, ipd, atv, ipd, ipd, ipd
# Total expected: $2718.95
co = Checkout(pricingRules)
co.scan('atv')
co.scan('ipd')
co.scan('ipd')
co.scan('atv')
co.scan('ipd')
co.scan('ipd')
co.scan('ipd')
print(co.total())

# SKUs Scanned: mbp, vga, ipd
# Total expected: $1949.98
co = Checkout(pricingRules)
co.scan('mbp')
co.scan('vga')
co.scan('ipd')
print(co.total())
