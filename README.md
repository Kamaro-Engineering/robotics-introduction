# Robotics Introduction
An introduction to robotics. The target is to get into robotics and ros with an easy (exponential) learning curve.

This is a tutorial on robotics.
The provided software can be used with for example an RC-Car with a PI attached like alice- and bob-hardware or with a full sized robot using ros.

If you do not have a robot yet look at the alice- or bob-hardware repositories to build your own robot.
* [Alice-Bot](https://github.com/penguinmenac3/alice-hardware) (scratch build, indoor, differential drive)
* [Bob-Bot [WIP]](https://github.com/penguinmenac3/bob-hardware) (modified rc car, outdoor, ackerman steering)
* Eve-Bot (like alice just smaller, hopefully released opensource someday)


If you want to adopt your ros robot to be compliant with this tutorial, look at [our implementation of the betelgeuse robot (ros)](https://github.com/penguinmenac3/robotics-introduction/blob/master/robots/betelgeuse.py). If you do not understand it, write us an email. 

## Overview

Assignment Name - What you learn. *(key skill name)*

0. Installing (section Setup) - Learn to setup a development environment. **(mandatory setup)**
1. [LEDs](https://github.com/penguinmenac3/robotics-introduction/tree/master/assignment1_leds) - Learn the basics of python and the framework.
2. [Buttons and LEDs](https://github.com/penguinmenac3/robotics-introduction/tree/master/assignment2_buttons_and_leds) - Learn the basics of event driven programming. *(can be skipped, since simulator and most hardware do not support buttons)*
3. [Steering a Robot](https://github.com/penguinmenac3/robotics-introduction/tree/master/assignment3_steering_a_robot) - Learn how to drive a robot in a rectangle. *(Steering)*
4. [Collision Avoidance](https://github.com/penguinmenac3/robotics-introduction/tree/master/assignment4_collision_avoidance) - Learn how to react to sensor values. *(Perception Basics)*
5. [Controll by Compass](https://github.com/penguinmenac3/robotics-introduction/tree/master/assignment5_controll_by_compass) - Learn to control the robots direction despite external factors. *(Control)*
6. [Drive to GPS Position](https://github.com/penguinmenac3/robotics-introduction/tree/master/assignment6_drive_to_gps_position) - Learn how to reach a gps destination. *(Simple Planning)*
7. [Advanced Navigation](https://github.com/penguinmenac3/robotics-introduction/tree/master/assignment7_advanced_navigation) - Learn how to put all pieces together to reach a gps target without colliding. *(Planning)*
8. [Porting to Betelgeuse](https://github.com/penguinmenac3/robotics-introduction/tree/master/assignment8_porting_to_betelgeuse) - (kamaro only) Port your code to a bigger robot. *(can be skipped)*
9. [ROS Programming](https://github.com/penguinmenac3/robotics-introduction/tree/master/assignment9_ros_programming) - Learn the fundamentals of ROS, a widely spread robotics framework. *(ROS, **the** framework)*

**BONUS/Advanced Stuff**

* [Localization and Mapping](https://github.com/penguinmenac3/robotics-introduction/tree/master/assignment_bonus_graph_slam) - Learn how a robot can localize itself.
* [Reinforcement Learning](https://github.com/penguinmenac3/robotics-introduction/tree/master/assignment_bonus_reinforcement_learning) - Learn how to teach a robot by reward and punishment.
* [Supervised Learning [TODO]](https://github.com/penguinmenac3/robotics-introduction/tree/master/assignment_bonus_supervised_learning) - Learn how robot perception works with deep neural networks.


# Setup

1. Install the simulator. When developing algorithms for a robot the first step is usually testing it in a simulator. There is a simulator for alice which can be found [here](https://github.com/penguinmenac3/alice-simulator).

2. Get yourself a compatible robot, if your instructor has not done so for you already.

    a) Build your own alice, bob or eve robot.
    
    b) Adopt a ros robot (like we did with betelgeuse).
    
    c) Use the alice simulator (it has all sensors except camera).
    
3. Install git and python on your system (see **install dependencies** instrucitons below)

4. Open a commandline in the folder where you want to work with your project.

5. Clone this repository
```bash
git clone https://github.com/penguinmenac3/robotics-introduction.git
```

6. If you did all steps correctly, you can start with the [first assignment](https://github.com/penguinmenac3/robotics-introduction/tree/master/assignment1_leds).

## Install Dependencies (Ubuntu)

Update and upgrade your system.

```bash
sudo apt-get update
sudo apt-get upgrade
```

Install git, python, pip and python-dev.

```bash
sudo apt-get install git python python-pip python-dev
```

## Install Dependencies (Windows)

Download and install the most recent version of anaconda python for windows. (Python2.7 and Python3.x should both be fine)

https://www.continuum.io/downloads#windows

Download and install git.

https://git-scm.com/
