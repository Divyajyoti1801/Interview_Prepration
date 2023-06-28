class Cookie:
    #Constructor declaration
    def __init__(self,color):
        self.color=color;

    def get_color(self):
        return self.color;

    def set_color(self,color):
        self.color=color;

cookie_one=Cookie("green");
cookie_two=Cookie("blue");

print("Cookie One is: ",cookie_one.get_color());
print("Cookie Two is: ",cookie_two.get_color());

cookie_one.set_color("Yellow");

print("Cookie One is: ",cookie_one.get_color());
print("Cookie Two is: ",cookie_two.get_color());