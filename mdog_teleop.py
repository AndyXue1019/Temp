#!/usr/bin/env python
# -*- coding: utf-8 -*-

import select
import sys
import time
import termios
import tty
from itertools import chain

import rospy
from mdog_walk.msg import servos_angle

msg = """
Control Mdog
---------------------------
Moving around:
        w
   a    s    d
        x


W : walk forward
X : walk backward
A : walk left
D : walk right 

S, sapce key : stop and stand

CTRL-C or Q to quit
"""

e = """
Communications Failed
"""

_servos_angle = servos_angle()
servos_signal = []

foot_stay  = [   1.0,   1.0, 1.0]
foot_stand = [ -30.0, -45.0, 0.0] 
foot_raise = [  -0.0, -55.0, 0.0] 
foot_step  = [ -20.0, -35.0, 0.0]

foot_stand_back = [ -45.0, -45.0, 0.0]
foot_raise_back = [ -15.0, -55.0, 0.0]
foot_step_back  = [ -35.0, -35.0, 0.0]

foot_right_r = [ -30.0, -45.0, -10.0] #dog right
foot_right_l = [ -30.0, -45.0, -10.0] #dog left
foot_right_l_back = [-45.0, -35.0, 10.0] #dog right back
foot_right_r_back = [-45.0, -35.0, 10.0] #dog left back

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
        
    return key

def first_stand():
    stand_signal = [foot_stay,
                    foot_stand,
                    foot_stand,
                    foot_stay]
    _servos_angle.angles = list(chain.from_iterable(stand_signal))
    pub.publish(_servos_angle)
    time.sleep(0.5)

    stand_signal = [foot_stand,
                    foot_stay,
                    foot_stay,
                    foot_stand]
    _servos_angle.angles = list(chain.from_iterable(stand_signal))
    pub.publish(_servos_angle)
    time.sleep(0.5)

def stand():
    stand_signal = [foot_stand,
                    foot_stand,
                    foot_stand,
                    foot_stand]
    _servos_angle.angles = list(chain.from_iterable(stand_signal))
    pub.publish(_servos_angle)
    time.sleep(0.5)

def walk_forward():
    servos_signal = [foot_raise,
                     foot_stand_back,
                     foot_raise,
                     foot_stand]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.1)

    servos_signal = [foot_step ,
                     foot_stand_back,
                     foot_step_back ,
                     foot_stand]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.2)

    servos_signal = [foot_stand,
                     foot_raise,
                     foot_stand_back,
                     foot_raise]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.1)

    servos_signal = [foot_stand,
                     foot_step_back ,
                     foot_stand_back,
                     foot_step ]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.2)
    
def walk_backward(): # Not tested yet...
    servos_signal = [foot_raise,
                     foot_stand_back,
                     foot_raise,
                     foot_stand]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.1)

    servos_signal = [foot_step ,
                     foot_stand_back,
                     foot_step_back ,
                     foot_stand]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.2)

    servos_signal = [foot_stand,
                     foot_raise,
                     foot_stand_back,
                     foot_raise]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.1)

    servos_signal = [foot_stand,
                     foot_step_back ,
                     foot_stand_back,
                     foot_step ]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.2)

def walk_left():
    servos_signal = [foot_stand,
                     foot_raise_back,
                     foot_stand_back,
                     foot_raise]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.1)
    
    servos_signal = [foot_right_r,
                     foot_raise_back,
                     foot_right_l_back,
                     foot_raise]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.1)

    servos_signal = [foot_stand,
                     foot_step_back ,
                     foot_stand_back,
                     foot_step ]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.1)
    
    servos_signal = [foot_raise,
                     foot_stand_back,
                     foot_raise_back,
                     foot_stand]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.1)
    
    servos_signal = [foot_step ,
                     foot_stand_back,
                     foot_step_back ,
                     foot_stand]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.1)

def walk_right():
    servos_signal = [foot_raise,
                        foot_stand_back,
                        foot_raise_back,
                        foot_stand]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.1)
    
    servos_signal = [foot_raise,
                        foot_right_r_back,
                        foot_raise_back,
                        foot_right_l]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.1)

    servos_signal = [foot_step,
                        foot_stand_back ,
                        foot_step_back,
                        foot_stand ]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.1)
    
    servos_signal = [foot_stand,
                        foot_raise_back,
                        foot_stand_back,
                        foot_raise]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.1)
    
    servos_signal = [foot_stand,
                        foot_step_back,
                        foot_stand_back ,
                        foot_step]
    _servos_angle.angles = list(chain.from_iterable(servos_signal))
    pub.publish(_servos_angle)
    time.sleep(0.1)

if __name__=="__main__":
    old_setting = termios.tcgetattr(sys.stdin)
    new_settings = termios.tcgetattr(sys.stdin)
    new_settings[3] = new_settings[3] & ~termios.ECHO
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, new_settings)

    rospy.init_node('modg_teleop')
    pub = rospy.Publisher('servos_angle', servos_angle, queue_size = 10)
    try:
        first_stand()
        print(msg)
        while not rospy.is_shutdown():
            key = getKey()

            if key == 'w' :
                walk_forward()
            elif key == 'x' :
                walk_backward()
            elif key == 'a' :
                walk_left()
            elif key == 'd' :
                walk_right()
            elif key == ' ' or key == 's' :
                stand()
            else:
                if key == '\x03' or key == 'q':
                    rospy.signal_shutdown('Quit')

    except Exception as e:
        print(e)

    finally:
        stand()
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_setting)