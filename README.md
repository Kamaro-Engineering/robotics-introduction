# robotics-introduction
An introduction to robotics. The target is to get into robotics and ros with an easy (exponential) learning curve.

This is a tutorial on robotics.
The provided software can be used with for example an RC-Car with a PI attached like alice- and bob-hardware or with a full sized robot using ros.

If you do not have a robot yet look at the alice- or bob-hardware repositories to build your own robot. https://github.com/penguinmenac3/alice-hardware https://github.com/penguinmenac3/bob-hardware
If you want to adopt your ros robot to be compliant with this tutorial, write us an email.

# Setup

1. Get yourself a compatible robot, if your instructor has not done so for you already.
    a) Build your own alice or bob robot.
    b) Adopt a ros robot
    c) Use the alice simulator.
    
2. Install git and python on your system (see **install dependencies** instrucitons below)

3. Open a commandline in the folder where you want to work with your project.

4. Clone this repository
```bash
git clone https://github.com/penguinmenac3/robotics-introduction.git
```

5. Test if it runs by executing the test script: **test.sh** on linux and **test.bat** on windows.

6. If there is no error you can start with the first assignment.

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
