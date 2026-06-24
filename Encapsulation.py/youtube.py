class Analytics:
    def __init__(self,name):
        self.__name = name
        self.__subscribers = 0
        self.__views = 0
        self.__likes = 0
        self.__comments = 0
    
    def Vlog1 (self):
        print(" You uploaded first video")
    
    def add_subscribers(self, count):
        self.__subscribers += count

    def add_views(self, count):
        self.__views += count

    def add_likes(self, count):
        self.__likes += count
   
    def add_comments(self, count):
        self.__comments += count

    def show_analytics(self):
        print(f" {self.__name}'s first video gained {self.__subscribers}, {self.__views}, {self.__likes}, {self.__comments}")

A1= Analytics("Python")
A1.Vlog1()
A1.add_subscribers(1)
A1.add_views(3)
A1.add_likes(1)
A1.add_comments(2)
A1.show_analytics()


