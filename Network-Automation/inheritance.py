# Program for Inheritance

class Parent:
    def common(self):
        print("nationality - Indian")
        print("Identity = Passport")
class Child1(Parent):
    def actions(self):
        print(self)
class Child2(Parent):
    def behaviors(self):
        print()



gen1 = Child1()
gen1.common()
gen2=Child2()
gen2.common()

