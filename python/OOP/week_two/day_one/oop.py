name = 'edgar'
age = 9999

pen_black = {
    'color':'black',
    'has_ink':True,
}

pen_red = {
    'color':'red',
}

class Utensil:
    def __init__(self, color, has_ink = True):
        self.color = color
        self.has_ink = has_ink

    def write(self, words = None):
        if words == None:
            print('Buddy, you have to write something')
        else:
            print(words)
        return self

    def erase(self):
        print("Your words were smudged and your paper is now ruined")
        return self



redPen = Pen('red', True)

pen_black2 = Pen('black', True)
pen_black3 = Pen('black', False)
pen_red = Pen('red')

# print(pen_black['color']) #black
# print(pen_red.has_ink) #red
# print(pen_black3.has_ink) 


pen_red.write("something").write("something else").erase()
print(pen_red.__dict__)


