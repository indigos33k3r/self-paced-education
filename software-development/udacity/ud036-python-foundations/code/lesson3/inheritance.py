class Parent():
    def __init__(self, last_name, eye_color):
        print "Parent constructor called"
        self.last_name = last_name
        self.eye_color = eye_color
        
    def show_info(self):
        print 'Last Name: ' + self.last_name
        print 'Eye Color: ' + self.eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, num_toys):
        print "Child constructor called"
        Parent.__init__(self, last_name, eye_color)
        self.num_toys = num_toys

print "Creating bob..."		
bob = Parent('Jones', 'blue')

print "Creating joe..."
joe = Child('Jones', 'green', 5)

print "\n\n\n"

bob.show_info()
joe.show_info()