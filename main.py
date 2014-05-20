import os
import sys
import stats

def main():
  print("Starting type-brite")
  [hub_addr, light_name] = stats.get_configuration()
  os.system("sudo ./key_press | python stats.py " + str(hub_addr) + " " + str(light_name))

if __name__ == "__main__":
   main()
