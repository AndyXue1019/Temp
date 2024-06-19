#!/usr/bin/env python3

import rospy
from mdog_walk.msg import servos_angle
import time
from itertools import chain
from std_msgs.msg import Float64MultiArray


_servos_angle = servos_angle()
servos_signal = []
    
top_foot = 1


foot_stand = [
              [70.0, -70.0, 0.0], [66.7, -69.2, 0.0], [63.3, -68.3, 0.0], 
              [60.0, -67.5, 0.0], [56.7, -66.7, 0.0], [53.3, -65.8, 0.0], 
              [50.0, -65.0, 0.0], [46.7, -64.2, 0.0], [43.3, -63.3, 0.0], 
              [40.0, -62.5, 0.0], [36.7, -61.7, 0.0], [33.3, -60.8, 0.0], 
              [30.0, -60.0, 0.0], [26.7, -59.2, 0.0], [23.3, -58.3, 0.0], 
              [20.0, -57.5, 0.0], [16.7, -56.7, 0.0], [13.3, -55.8, 0.0], 
              [10.0, -55.0, 0.0], [6.7, -54.2, 0.0], [3.3, -53.3, 0.0], 
              [0.0, -52.5, 0.0], [-3.3, -51.7, 0.0], [-6.7, -50.8, 0.0], 
              [-10.0, -50.0, 0.0], [-13.3, -49.2, 0.0], [-16.7, -48.3, 0.0], 
              [-20.0, -47.5, 0.0], [-23.3, -46.7, 0.0], [-26.7, -45.8, 0.0], 
              [-30.0, -45.0, 0.0]
]


foot_raise = [ - 0.0, -55.0, 0.0] 
foot_step  = [ -20.0, -35.0, 0.0]



def callback():

    pub = rospy.Publisher('servos_angle', servos_angle, queue_size = 10)
    
    time.sleep(2.0)
    
    # let the dog stand up first   
    for i in range(31):
        
        if i == 30:
            stand_singal = foot_stand[i] + foot_stand[i] + foot_stand[i] + foot_stand[i]
        else:
            stand_singal = foot_stand[i] + foot_stand[i+1] + foot_stand[i+1] + foot_stand[i]
        _servos_angle.angles = stand_singal
        pub.publish(_servos_angle)
        time.sleep(0.1)



def listener():
    rospy.Subscriber("/direction_msg", Float64MultiArray, callback, queue_size = 1)
    rate = rospy.Rate(10)
    rospy.spin()


if __name__ == '__main__':
    rospy.init_node('servos_angle_publisher', anonymous=True)
    callback()
    
