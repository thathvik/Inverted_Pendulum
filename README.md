# Linear Inverted Pendulum
This is the final assignment for MTE 4007: Robot Dynamics and Control, Department of Mechatronics Engineering, Manipal Institute of Technology

The inverted pendulum is controlled successfully using a PID.


## Instructions

In order to run this package, add it to your catkin workspace.
You can the use the following commands, each in a new terminal window:

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


