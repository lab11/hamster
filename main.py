import os
import sys

usage = "\n   Usage:\n     sudo python main.py <name of bulb/your name>\n" + \
"\n   Example:\n     sudo python main.py Meghan\n"

def main():
  if len(sys.argv) != 2:
  	print(usage)
  	sys.exit()
  print("Starting type-brite")
  os.system("sudo ./key_press | python stats.py " + str(sys.argv[1]))

if __name__ == "__main__":
   main()
