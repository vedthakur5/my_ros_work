#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def callback(msg):
   print(msg.pose.pose.position)

rospy.init_node('topic_subscriber')
sub=rospy.Subscriber('/odom',Odometry,callback)
rospy.spin()
