# Program to record video in segements using a Raspberry Pi V2
# Camera over a given period of time, with given segement length
import picamera
import datetime as dt

#removed use of checking if PID was running, script will fail
#for lack of resources if camera is currently in use by same script


time_r = 300
    #time in seconds for each segment
time_tot = 72000 
    #total time in seconds you wish to record, value in parentheses
    #is time in minutes
num_files = time_tot/time_r
    #the number of files which will be created

with open("/home/pi/Documents/RasPiCamera/VidNum.txt" , "r") as myfile: 
    VidNum = myfile.read()
    #find number of the last video recorded
    #on first run make sure text file has a value of zero

with picamera.PiCamera() as camera:
    camera.resolution = (1640, 922) #resolution setting
    camera.framerate = 30 #frame rate setting
            
    for x in range(int(VidNum),(int(num_files)+int(VidNum))):
        f = open("/home/pi/Documents/RasPiCamera/VidNum.txt" , "w")
        f.write(str(x))
        f.close()
        #store number of last video for unique filename creation
        filename = "/media/pi/Samsung_T3/Videos/video_" +str(x)+".h264"
        #save location
        camera.annotate_background = picamera.Color('black')
        camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #place a timestamp at the beggining of the video
        camera.start_recording(filename) 
        camera.wait_recording(time_r) 
        camera.stop_recording()
        
                
camera.close()
#destroy camera object 
