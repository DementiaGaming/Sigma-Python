import random as r

def gambling():
    return r.randint(1,100)

class wClass:
    def __init__(self, name, auraLevel):
        self.auraLevel = auraLevel
        self.name = name
    
    def wAura(self, amount):
        self.auraLevel += amount

    def lAura(self, amount):
        self.auraLevel -= amount

    def yapAura(self):
        print(f"{self.name} aura level: {self.auraLevel}")

print("on skibidi")

yes = True
cooking = input("you may now cook ")

if yes:
    print("on sigma")
elif not yes:
    print("what the skibidi")
else:
    print("what the sigma")

if cooking == "real":
    print("ong")
else:
    print("frfr")

print("gambling time")
print(f"gamble is {gambling()}")

walterWhite = wClass("walter white", 10)

walterWhite.yapAura()
walterWhite.wAura(69)
walterWhite.yapAura()
walterWhite.lAura(9)
walterWhite.yapAura()