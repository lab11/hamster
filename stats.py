import sys, sched, time, hue, threading
from threading import Timer

#Globals
window = 3 #num in avg
times = [] #times to be averages
timeout_val = 1 #seconds before timeout
max_brightness = 254 #max value of lamp given by phue
last_time = 0 

bulb_name = sys.argv[1]

# Connect to hue
# TODO: make this not hardcoded
lights = hue.hue_connect()
light = [l for l in lights if l.name == bulb_name][0]


def set_brightness(brightness):
  light.brightness = brightness

def get_weighted_brightness():
  avg_speed = sum(times)/len(times)
  avg_speed_map = int(((avg_speed / timeout_val) * max_brightness)) 
  brightness = max_brightness - avg_speed_map
  if (brightness < 0): 
    brightness = 0 
  return brightness

def append_time():
  global last_time
  cur_time = time.time()
  delta_time = cur_time-last_time  
  times.append(delta_time)
  if (len(times) == window):
    times.pop(0)
  last_time = cur_time

def timeout():
  if (time.time() - last_time > timeout_val):
    light.brightness = 0
   
def process_event():
  append_time()
  set_brightness(get_weighted_brightness()) 

while (1):
  if (len(raw_input()) != 0):
    t = threading.Thread(target=process_event) 
    t.daemon = True
    t.start()    
    t.join()
  Timer(int(timeout_val), timeout, ()).start()
