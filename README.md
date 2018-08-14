#3D Renderer

This is a cool 3D renderer that I made for fun after reading [this tutorial](http://www.petercollingridge.co.uk/tutorials/3d/pygame/) by Peter Collingridge. 

It is a simple program to render two cubes that can be independently rotated, moved around, and scaled.

![Application window is shown with two cubes, one red and one green, sitting side-by-side.](https://github.com/jasonmgru/3d-renderer/blob/master/github_preview.png)

## Installation and Running

This program requires Python3, numpy, and pygame. If you already have these dependencies, skip to step 5.

1. Install Python3 from [https://www.python.org/downloads/] 
2. From the command line, verify that python3 was successfully installed by typing `python3 --version` This should display the python version.
3. Install numpy by typing `pip3 install numpy`
4. Install pygame by typing `pip3 install pygame`
5. Clone this repository by typing `git clone https://github.com/jasonmgru/3d-renderer.git`
6. Navigate into the folder by typing `cd 3d-renderer`
7. Now you can run the program! Type `python3 driver.py` and wait for a window to pop up.

## Usage

In the main window of the program, you should see two cubes. You can select a cube by clicking on it, which will highlight the edges of the cube with yellow lines. 

From here, you can manipulate the cube in several ways:
- Use the arrow keys <kbd>left</kbd> <kbd>up</kbd> <kbd>right</kbd> <kbd>down</kbd> to move the cube around the screen.
- Use <kbd>+=</kbd> and <kbd>_-</kbd> to scale the selected cube.
- Use <kbd>a</kbd> and <kbd>d</kbd> to rotate the cube around the z-axis
- Use <kbd>q</kbd> and <kbd>e</kbd> to rotate the cube around the y-axis
- Use <kbd>s</kbd> and <kbd>w</kbd> to rotate the cube around the x-axis
