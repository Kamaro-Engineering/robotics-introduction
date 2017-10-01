# Assignment 6: Collision Avoidance

Until now, you only have steered the robot blindly. But a robot who does not interact or react with its
environment is barely a robot.

## Sensing our surroundings

In this assignment you will learn how to use your robot's sensors to navigate an environment full of obstacles
without prior knowledge about it. The goal is to drive through a room without colliding with any of its obstacles.

To use the sensor data, you have to define the callback `on_sensor_reading` of your robot like the following:

```python
def process_sensor_data(sensor, data):
  if sensor == "distance/front":
    print ("New sensor data:")
    for i in range(0, len(data)):
      print("  Sensor {} measured a distance of {}".format(i, data[i]))

robot.on_sensor_reading = process_sensor_data

robot.wait()
robot.shutdown()
```

`on_sensor_reading` is called everytime the robot gets new data from one of its sensors. We want to use its
frontfacing ultrasonic sensors (or later Betelgeuses front lidar) which will call the function with
`"distance/front"` as its first argument.
The second argument contains the actual data the sensors measured. In this case it is an array with the
distance in meters each sensor has measured. The sensors are sorted from left to right. Alice has four of them.

Try now to keep the robot moving through the room without collisions utilizing your robot's frontfacing sensors
and the stuff you learned in assignment 3.
Just standing still or driving in a small enough circle do not count. ;)

## Bonus

Make your code work for a robot with any number of frontfacing sensors. How do you distinguish between a left
facing or right facing sensor, assuming a symmetrical setup?

Depending on your solution, after a while your robot will probably keep following the same more or less complex
pattern through a room. Try to increase the amount of space covered by your robot and compare with your peers!

Try to follow a wall to the right side of your robot, without moving further away than 0.5m from the wall (and of
course without colliding with it either)!
