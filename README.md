# Linear Inverted Pendulum
Gazebo Simulation of Inverted Pendulum model and control using a PID controller, under normal gravity conditions.

The inverted pendulum is controlled successfully using a PID.


## Instructions

In order to run this package, add it to your catkin workspace, and name it inv_pend.

Then, you can the use the following commands, each in a new terminal window:

1. Start roscore
```bash
  $ roscore
```
2. Launch the model in Gazebo
```bash
  $ roslaunch inv_pend inv_pend.launch
```
3. Run the controller
```bash
  $ rosrun inv_pend control.py 
```

or 

To just simulate it on Rviz

1. Start roscore

```bash
  $ roscore

```
2. Launch the model in Rviz
```bash
  $ roslaunch inv_pend rviz.launch
```


