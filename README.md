Toy Robot Simulator
===================

Description
-----------

- The application is a simulation of a toy robot moving on a square tabletop,
  of dimensions 5 units x 5 units.
- There are no other obstructions on the table surface.
- The robot is free to roam around the surface of the table, but must be
  prevented from falling to destruction. Any movement that would result in the
  robot falling from the table must be prevented, however further valid
  movement commands must still be allowed.

Getting Started
---------------

These instructions will get you a copy of the project up and running on your 
local machine for development and testing purposes.

### Prerequisites

  * Python 3.6 and up
  * Unittest package

### Installing

  - The simulator doesn't need to be installed. However, you should have installed
  	Python in your local machine. 

Running the code
----------------
   
  ### Running test file
   	
  * Open a new terminal window
  * Move into the project directory
  ```
  $ cd your/local/folder/RobotSimulator
  ```
  * Run TestRobotFunctions.py 
  ```
  $ python TestRobotFunctions.py
  ```

  ### Coding style tests

  - Testing code have been implemented following TDD techniques.

  ### Running the simulator

  * Open a terminal window
  * Move into the project directory
  ```
  $ cd your/local/folder/RobotSimulator
  ```
  * Run Game.py
  ```
  $ python Game.py
  ```
  * Enter your commands
  ```
  $ Please enter your commands then press ctrl+d:
  $ PLACE 0,0,WEST
  $ REPORT
  $ ctrl+d
  ```
  * The output should be similar to:
  ```
  $ 0,0,WEST
  ```
  - Notes:
  	* If you press 'ctrl+d' in the same line where the last command input is,
  	you should press 'ctrl+d' two time to create the EOF in the system.
  	* If you press 'ctrl+d' in the next line where the last command input is,
  	you should press 'ctrl+d' only one time to create the EOF in the system.
  	* This system has been tested in Mac, Linux, Ubuntu and Centos. If you
  	are using different OS, maybe 'ctrl+d' doesn't create EOF in the system.

	




