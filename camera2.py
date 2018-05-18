# Program to record video in segements using a Raspberry Pi V2
# Camera over a given period of time, with given segement length
import os 
import picamera
from time import sleep




time_r = 3
    #time in seconds for each segment
time_tot = 15
    #total time in seconds you wish to record, value in parentheses
    #is time in minutes
num_files = time_tot/time_r
    #the number of files which will be created

with open("/home/pi/Documents/RasPiCamera/VidNum.txt" , "r") as myfile: 
    VidNum = myfile.read()
    #find number of the last video recorded

with picamera.PiCamera() as camera:
    camera.resolution = (1640, 922) #resolution setting
    camera.framerate = 40 #frame rate setting
            
    for x in range(int(VidNum),(int(num_files)+int(VidNum))):
        f = open("/home/pi/Documents/RasPiCamera/VidNum.txt" , "w")
        filename = "/media/pi/Samsung_T3/Videos/video_" +str(x)+".h264" #save location
        camera.start_recording(filename) 
        camera.wait_recording(time_r) 
        camera.stop_recording()
        f.write(str(x))
        f.close()
        #update number of last video recorded and close filestream

        
camera.close()




           
        
            

        

