# Assignment Bonus: Deep Q Learning

With a simple Q Learning algorithm, we can allow the robot to continually improve from both rewards and punshments. 
Use only the robot sensors to develop your algorithm.

Use the following framework to aid you in your assignment.

```python
from robots.alice import Robot, ALICE_MAX_SPEED
from math import pi

#Parameters

#End Parameters

def learn(prev_state, action, reward, current_state):
  # using Bellman Optimality Equation to update q function
  
# get action for the state according to the q function table
# agent pick action of epsilon-greedy policy
def get_action(current_state):

    return action
        
def arg_max(state_action):

    return random.choice(max_index_list)
    
def process_sensor_data(sensor, data):
    #Use sensors as state
    
def g(lat, lon):
    # TODO implement
    return 0.0

def f(angle_to_north, desired_direction):
    # TODO implement
    return 0.0

def on_global_position(lat, lon, angle_to_north):
    desired_direction = g(lat, lon)
    robot.set_turn(f(angle_to_north, desired_direction))

robot = Robot()
robot.on_sensor_reading = process_sensor_data
robot.on_global_position = on_global_position
robot.set_speed(ALICE_MAX_SPEED)  # move with max speed

robot.wait()
robot.shutdown()

```

Helpful Link: https://github.com/keon/deep-q-learning
