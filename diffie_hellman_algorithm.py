from random import randint
class Diffie_Hellman_Algo():
    def __init__(self, p, g):
        self.P = p
        self.G = g

    def value(self):
        print(f"The value of P: {self.P}\nThe value of G: {self.G}")

    def alice(self, num:int):
        self.a = num
        print(f"Secret number for alice is: {self.a}")
        return int(pow(self.G, self.a, self.P))

    def bob(self, num:int):
        self.b = num
        print(f"Secret number for bob is: {self.b}")
        return int(pow(self.G, self.b, self.P))

    def Key(self, alice:int, bob:int):
        Ka = int(pow(bob, self.a, self.P))
        Kb = int(pow(alice, self.b, self.P))
        print(f"Secret key for alice is: {Ka}\nSecret key for bob is: {Kb}")

if __name__ == "__main__":
    num = randint(1,100)
    dha = Diffie_Hellman_Algo(23, num)
    dha.value()
    a=int(input("Enter secret number for alice: "))
    x = dha.alice(a)
    b=int(input("Enter secret number for bob: "))
    y = dha.bob(b)
    dha.Key(x, y)
