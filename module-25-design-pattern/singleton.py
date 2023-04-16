class SingleTon:
    __instance=None
    def __init__(self) -> None:
        if SingleTon.__instance is None:
            SingleTon.__instance=self
        else:
            raise Exception('This is a singleTon.Already have an instance')
        
    @staticmethod
    def get_instance():
        if SingleTon.__instance is None:
            SingleTon()
        return SingleTon.__instance
    

first=SingleTon.get_instance()
second=SingleTon.get_instance()
third=SingleTon.get_instance()

print(first)
print(second)
print(third)