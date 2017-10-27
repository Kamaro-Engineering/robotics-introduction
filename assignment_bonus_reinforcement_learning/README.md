# Assignment Bonus: Reinforcement Learning (RL)

*You picked the coolest task of them all. (see section "Bonus Knowledge")*

In this task you will learn the basics of reinforcement learning (RL).

## What is Reinforcement Learning (RL)?

RL is basically the principle of learning with reward and punishment.
The computer is not given a model how to behave but rather it gets a reward whenever it does something good, and a punishment when its behaviour is bad.
It then learns by itself which behaviour to repeat and which to avoid.

The most basic way of learning this is using so called **Q-Learning**.
One of the best articles around about q-learning is [this one](http://neuro.cs.ut.ee/demystifying-deep-reinforcement-learning/).
Read it to get a good in depth explanation of the topic, or just use it as a helpful reference to implement this assignment.

## Simple Q-Learning (with table)

(Resources that will help you with your task are listed at the bottom of the page.)

With a simple Q Learning algorithm, we can allow the robot to continually improve from both rewards and punishments.
Use only the robot sensors to develop your algorithm.
For a first implementation it is recommended to use a simple table as a q-function.
Once you have mastered the table you can proceed to the "cool Stuff" (neural networks) as q-function.

This article might be helpful: https://en.wikipedia.org/wiki/Q-learning

Use the following framework to aid you in your assignment.
It provides you some anchors, but you have to figure out how to use it yourself.

You will have to figure out where, when and how to call the lean, get_action and arg_max functions yourself.

```python
from robots.alice import Robot, MAX_SPEED
from math import pi

#Parameters

q_function_table = {}  # TODO initialize q
learning_rate = 1.0  # TODO adjust this value
discount = 1.0  # TODO adjust this value

# Add more if you need more!

#End Parameters

def learn(prev_state, action, reward, current_state):
  # using Bellman Optimality Equation to update q function table
  
# get action for the state according to the q function table
# agent pick action of epsilon-greedy policy
def get_action(current_state):

    return action
        
def arg_max(state_action):

    return random.choice(max_index_list)
    
def process_sensor_data(sensor, data):
    if sensor == "reward":
        # Do something with the reward
    if sensor == "distance/front":
        # Use distance sensor(s) as state

robot = Robot()
robot.on_sensor_reading = process_sensor_data
robot.set_speed(MAX_SPEED)  # move with max speed

robot.wait()
robot.shutdown()

```

## Deep Q-Learning (DQN)

Assuming you understood the basics using a "simple" table as a q-function, you are ready for the fancy stuff: Deep Q-Learning.

Deep Q-Learning basically works the same way as normal Q-Learning.
However, your q-function is now no longer a table, but one of the "best" general function approximators: a neural network.

Spoiler alert: You will probably **not** need a really deep neural network.

Simple sample implementation of a dqn agent: [dqn.py](https://github.com/keon/deep-q-learning/blob/master/dqn.py)

### Bonus Knowledge

The alice robot (on which this whole introduction is based) was invented as a cheap, robust, easy to repair platform for reinforcement learning.

See my private project, where I develop my [alice-ai](https://github.com/penguinmenac3/alice-ai) using deep learning.

## Resources

This [introductory blog](http://neuro.cs.ut.ee/demystifying-deep-reinforcement-learning/) is one of the best introductions to (deep) q-learning.

If you need some motivation, read this [motivation site](https://deepmind.com/blog/deep-reinforcement-learning/) by deepmind (google).

If you like Papers:
[DQN Nature Paper](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf)

If you are interested in the maths and the derivation of RL, read [this german page](https://martin-thoma.com/probabilistische-planung/)
or if you do not speak german and like videos, these are the [best videos on RL](https://www.youtube.com/watch?v=2pWv7GOvuf0&list=PL7-jPKtc4r78-wCZcQn5IqyuWhBZ8fOxT).
