#!/usr/bin/env python
""" LIP control """

import rospy
import math
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Vector3, WrenchStamped
import numpy as np


class LIPController(object):
    """ LIP Control """
    def __init__(self, timestep):
        self.velocity = 0
        self.effort = 0
        self.position = 0
        self.kp = 150
        self.ki = 10
        self.kd = 150
        self.target_theta = 0
        self.smp_time = 0.01
        self.theta0 = 0
        self.thetai = 0
        self.error = 0
        self.duty_ratio = 0
        self.pubs = rospy.Publisher("/lip/joint_effort_controller_j_0/command/", Float64, queue_size=10)
        self.command_sub = rospy.Subscriber("/lip/joint_states", JointState , self.callback)

    def callback(self, data):
        """ Callback function for subscribing /lip/joint_states topic 
        Use this data in your control equation below """
        self.effort = data.effort
        self.velocity = data.velocity
        self.position = data.position
        """ Write your control equation in self.cmd 
        to publish the effort values to the Joint Effort Controller """
        self.error = self.target_theta - self.position[0]
       	self.dtheta = (self.error - self.theta0)/self.smp_time
        self.theta0 = self.error
        self.thetai += self.error*self.smp_time
        self.duty_ratio = (self.error*self.kp) + (self.thetai*self.ki) + (self.dtheta*self.kd)
        self.cmd = self.duty_ratio
        if self.cmd > 100:
        	self.cmd = 100
        elif self.cmd < -100:
        	self.cmd = -100
        self.pubs.publish(self.cmd)

def main():
    rospy.init_node('lip_control', anonymous=False)
    controller = LIPController(.01)
    rospy.spin()
    del controller
    return

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
