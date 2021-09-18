#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
import time

def automate():

    rospy.init_node('automatic_controller')

    pub = rospy.Publisher('cmd_vel', Twist , queue_size=1)

    mov_cmd = Twist()

    mov_cmd.linear.x = 0.0
    mov_cmd.angular.z = 0.0
    pub.publish(mov_cmd)
    time.sleep(1)

    i = 0

    for i in range(4):

        mov_cmd.linear.x = 1.0
        mov_cmd.angular.z = 0.0
        pub.publish(mov_cmd)
        time.sleep(2)

        mov_cmd.linear.x = 0.0
        mov_cmd.angular.z = 0.0
        time.sleep(1)

        mov_cmd.linear.x = 0.0
        mov_cmd.angular.z = 5.0
        pub.publish(mov_cmd)
        time.sleep(1)

        mov_cmd.linear.x = 0.0
        mov_cmd.angular.z = 0.0
        time.sleep(1)

        i = i + 1


if __name__ == '__main__':
    try:
        automate()
    except rospy.ROSInterruptException:
        pass