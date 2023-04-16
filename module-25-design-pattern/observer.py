class GroupChat:
    def __init__(self) -> None:
        self.__observers=[]
    def attach(self,observer):
        self.__observers.append(observer)
    def add_new_message(self,msg):
        self.notify(msg)
    def notify(self,msg):
        for observer in self.__observers:
            observer.update(msg)

class Observer:
    def __init__(self,name) -> None:
        self.name=name
    def update(self,msg):
        print(f'New message for {self.name}:{msg}')

messanger=GroupChat()
abid=Observer('Abid')
navid=Observer('Navid')
kabid=Observer('Kavid')
messanger.attach(abid)
messanger.attach(kabid)
messanger.attach(navid)
messanger.add_new_message('Hey bro!!How are you?')
messanger.add_new_message('Yah!We all are fine')