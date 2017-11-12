# Shutdown-Timer

## How to use:

Run the script, and tell it how many minutes you want it to wait before 
shutting down your system.

### Background:

This was the first Python script I wrote that was actually of any use.
I had the problem where my computer was doing some video encoding but I was 
going to be leaving the house. Rather than leave my computer running I knew 
how much time the encoding needed before it was finished so I needed a simple
 timer to tell my PC when to shut down. There was no simple applications 
 online or built into windows which did this so I decided to build my own!
 
### What it does

Runs the shutdown executable called when you press the shut down button.

### Future work

It is untested as to what this script does when you have applications which 
restrict shutdown (i.e. you have to force shut down).
There are a few ways of handling this:
* Override and force the system to shut down.
* Give the user a choice when the script is ran.
* Detect if a force shutdown is required and just try again after an 
interval of time.