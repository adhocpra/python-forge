class Call:
    def start(self):
        print(" I am calling")

class Camera:
    def start(self):
        print(" I click pictures")

class Music:
    def start(self):
        print(" I can play music")

class Mobile:
    def __init__(self):
        self.call= Call() #OBJECT
        self.camera= Camera()
        self.music= Music()
     
    def start(self):
        self.call.start() #OBJECT taking method
        self.camera.start()
        self.music.start()
        print(" I am mobile")
m1= Mobile()
m1.start()