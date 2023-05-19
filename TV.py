#create a class called TV
class Tv:
    #function initialization
    def __init__(self, Channel, VolumeLevel, Status):
        self.Channel = Channel
        self.VolumeLevel = VolumeLevel
        self.Status = Status
    
    #funtion of behaviors
    def TV(self):
        tv_number = int(input("What is the number of the TV you want to check?: "))
        self.tv = tv_number
    def TurnOn(self):
        self.Status = True
    
    def TurnOff(self):
        self.Status = False
    
    def GetChannel(self):
        print("The " , self.tv ," has the channel " , self.Channel , "\n")
    
    def SetChannel(self):
        self.Channel = int(input("What channel do you want to set this TV?: "))
        print("The channel of this TV is now " , self.Channel)
    
    def GetVolume(self):
        print("The " , self.tv ," has the level of Volume of " , self.VolumeLevel , "\n")
    
    def SetVolume(self):
        self.VolumeLevel = int(input("What level of Volume do you want to set this TV?: "))
        print("The Level of Volume for this TV is now " , self.VolumeLevel)

    def ChannelUP(self):
        print("The Channel has gone up to: " , self.Channel + 1)
    
    def ChannelDown(self):
        print("The Channel has gone down to: " , self.Channel - 1)
    