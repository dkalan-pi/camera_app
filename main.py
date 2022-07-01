#from tkinter import Button
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
import time
from client import *
#import client
Builder.load_file('camera.kv')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        #save captured pic. in phone internal storage (e.g SD card..)
        #camera.export_to_png("/sdcard/selfiedk/IMG.png")
        #when run the application in the local host for testing, then better to use the below code to save the pic(taken by the computer webcam) in the current directory.
        camera.export_to_png("IMG.png")
        img = "IMG.png"
        #img = camera.export_to_png("IMG_{}.png".format(timestr))
        #camera.export_to_png("/sdcard/selfiedk/IMG_{}.png".format(timestr))
        #camera.export_to_png("/sdcard/selfiedk/IMG.png")
        print("Captured-DK")
        client.main1(img)
        #print(server.main1.host)
        #server.CameraClick.Button.text(server.host)
        

class TestCamera(App):

    def build(self):
        # set necessary permission for Android
        if platform == "android":
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.CAMERA, Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        return CameraClick()


if __name__ == '__main__':
    TestCamera().run()
