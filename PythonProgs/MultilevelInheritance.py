
class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

Prakash= Dad()
Keval = Son()
Jack = Grandson()

print(Prakash.basketball)
print(Keval.basketball)
print(Jack.dance)

# electronic device
# pocket gadget
# phone



