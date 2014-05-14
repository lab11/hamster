type-brite
==========

A system that changes the brightness of a hue light depending on how fast you type

What you need:
* mac osx 
* a hue light
* python
* phue
  - https://github.com/studioimaginaire/phue
* the ability to compile c
* the ability to be super user

To run:
* Compile key_press.c 
   - gcc -Wall -o key_press key_press.c -framework ApplicationServices
* Because of os-x security restrictions, the key_press script will only work as super user. Read key_press.c if you don't trust it before running. 
   - sudo python main.py

TODO:
* The hue light is hard coded as light 2. Should be changed to allow user to choose.
* Pretty much no error handling is included.  

Keypress credit to:
Daniel Beard
 - http://danielbeard.wordpress.com/2010/10/29/listening-for-global-keypresses-in-osx/
