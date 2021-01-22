#!/usr/bin/env python
#encoding=utf-8

import sys
import rospy
import math
from geometry_msgs.msg import Twist
from amigobot_lib.bot import amigobot, amigobot_xyControl
from amigobot_lib.bot_ts import amigobot_TS

# uncomment the correspongding case to represent run by amigobot

# CASE 2
prefixes = [['u1', '4', '3', '4', '3', '4', '3', '4', '5'],
            ['u2', '10', '11', '23', '24'],
            ['11', '12', '1']]
suffix_cycles = [['5', '27', '28', 'g4', '28', '21', '22', '23', '9', '10', '10', 'u2', '10', '11', '23', '24', 'g2', '24', '25', '26', '27', '3', '4', 'u1', '4', '5', '27', '28', '28', '21', '22', 'g1', '22', '23', '23', '9', '10', 'u2', '10', '10', '10', '11', '23', '24', 'g2', '24', '25', '26', '27', '3', '4', 'u1', '4', '5', '27', '28', '28', '28', '28', '28', 'g4', '28', '21', '22', '23', '9', '10', 'u2', '10', '10', '11', '23', '24', 'g2', '24', '25', '26', '27', '3', '4', 'u1', '4', '4', '5', '27', '28', '28', 'g4', '28', '21', '22', '23', '9', '10', 'u2', '10', '11', '23', '23', '24', 'g2', '24', '25', '26', '27', '3', '4', '4', '3', '4', '3', '4', 'u1', '4', '5'],
                 ['24', '24', '24', '25', '26', 'g3', '26', '27', '3', '4', '4', '3', '4', '3', '4', 'u1', '4', '5', '27', '28', '21', '22', 'g1', '22', '23', '23', '9', '10', 'u2', '10', '11', '23', '24', '25', '26', 'g3', '26', '27', '3', '4', '3', '4', 'u1', '4', '4', '3', '4', '5', '27', '28', '28', '28', 'g4', '28', '21', '22', '23', '9', '10', 'u2', '10', '11', '23', '24', 'g2', '24', '25', '26', '27', '3', '4', 'u1', '4', '5', '27', '28', '21', '22', '22', 'g1', '22', '23', '23', '9', '10', 'u2', '10', '11', '23', '24', '24', 'g2', '24', '25', '26', '27', '3', '4', 'u1', '4', '5', '27', '28', '21', '22', '22', 'g1', '22', '23', '9', '10', '11', '10', 'u2', '10', '11', '23', '24', '24'],
                 ['2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1']]

'''
# CASE 3
prefixes = [['u1', '4', 'u1'],
            ['u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2'],
            ['11', '12', '1']]
suffix_cycles = [['u1', '4', '5', '27', '28', '28', '21', '22', 'g1', '22', '23', '23', '9', '10', 'u2', '10', '11', '23', '24', '24', '24', 'g2', '24', '25', '26', '27', '3', '4', 'u1', '4', '5', '27', '28', '28', '28', '28', '28', 'g4', '28', '21', '22', '23', '23', '9', '10', 'u2', '10', '11', '23', '24', 'g2', '24', '25', '26', '27', '3', '4', 'u1', '4', '4', '5', '27', '28', '28', 'g4', '28', '21', '22', '23', '9', '10', 'u2', '10', '11', '23', '24', '24', 'g2', '24', '24', '25', '26', '27', '3', '4', '4', '5', '4', '4', 'u1', '4', '5', '27', '28', 'g4', '28', '21', '22', '23', '23', '9', '10', 'u2', '10', '11', '23', '24', 'g2', '24', '25', '26', '27', '3', '4', 'u1'],
                 ['u2', '10', '10', '11', '23', '24', '25', '26', 'g3', '26', '27', '3', '4', '3', '4', 'u1', '4', '4', '3', '4', '3', '4', '5', '27', '28', 'g4', '28', '21', '22', '23', '9', '10', 'u2', '10', '11', '23', '24', 'g2', '24', '25', '26', '27', '3', '4', 'u1', '4', '5', '27', '28', '21', '22', '22', 'g1', '22', '23', '9', '10', 'u2', 'u2', '10', '11', '23', '24', '24', 'g2', '24', '25', '26', '27', '3', '4', 'u1', '4', '5', '27', '28', '21', '22', '22', 'g1', '22', '23', '9', '10', 'u2', '10', '11', '23', '24', '24', '25', '26', 'g3', '26', '27', '3', '4', '4', '3', '4', '3', '4', 'u1', '4', '5', '27', '28', '21', '22', 'g1', '22', '23', '9', '10', 'u2'],
                 ['2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1']]
'''
'''
# CASE 4
prefixes = [['u1', '4', 'u1'],
            ['u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2'],
            ['11', '12', '1']]

suffix_cycles = [['u1', '4', '5', '27', '28', '28', '21', '22', 'g1', '22', '23', '23', '9', '10', 'u2', '10', '11', '23', '24', '24', '24', 'g2', '24', '25', '26', '27', '3', '4', 'u1', '4', '5', '27', '28', '28', '28', '28', '28', 'g4', '28', '21', '22', '23', '23', '9', '10', 'u2', '10', '11', '23', '24', 'g2', '24', '25', '26', '27', '3', '4', 'u1', '4', '4', '5', '27', '28', '28', 'g4', '28', '21', '22', '23', '9', '10', 'u2', '10', '11', '23', '24', '24', 'g2', '24', '24', '25', '26', '27', '3', '4', '4', '5', '4', '4', 'u1', '4', '5', '27', '28', 'g4', '28', '21', '22', '23', '23', '9', '10', 'u2', '10', '11', '23', '24', 'g2', '24', '25', '26', '27', '3', '4', 'u1'],
                ['u2', '10', '10', '11', '23', '24', '25', '26', 'g3', '26', '27', '3', '4', '3', '4', 'u1', '4', '4', '3', '4', '3', '4', '5', '27', '28', 'g4', '28', '21', '22', '23', '9', '10', 'u2', '10', '11', '23', '24', 'g2', '24', '25', '26', '27', '3', '4', 'u1', '4', '5', '27', '28', '21', '22', '22', 'g1', '22', '23', '9', '10', 'u2', 'u2', '10', '11', '23', '24', '24', 'g2', '24', '25', '26', '27', '3', '4', 'u1', '4', '5', '27', '28', '21', '22', '22', 'g1', '22', '23', '9', '10', 'u2', '10', '11', '23', '24', '24', '25', '26', 'g3', '26', '27', '3', '4', '4', '3', '4', '3', '4', 'u1', '4', '5', '27', '28', '21', '22', 'g1', '22', '23', '9', '10', 'u2'],
                ['2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1', '2', '21', '22', '23', '9', '10', '11', '12', '1']]
'''


def main():
    rospy.init_node('ijrr2013_ca_improv', anonymous=False)

    bot_1 = amigobot_TS(name='amigobot_1', yaml_file='/home/ghost/catkin_ws_ros/src/amigobot_LTL/model/ijrr_2013_improv/robot_1.yaml',
                                           map_file ='/home/ghost/catkin_ws_ros/src/amigobot_LTL/model/ijrr_2013_improv/map.yaml')
    bot_2 = amigobot_TS(name='amigobot_2', yaml_file='/home/ghost/catkin_ws_ros/src/amigobot_LTL/model/ijrr_2013_improv/robot_2.yaml',
                                           map_file ='/home/ghost/catkin_ws_ros/src/amigobot_LTL/model/ijrr_2013_improv/map.yaml')
    bot_3 = amigobot_TS(name='amigobot_3', yaml_file='/home/ghost/catkin_ws_ros/src/amigobot_LTL/model/ijrr_2013_improv/robot_3.yaml',
                                           map_file ='/home/ghost/catkin_ws_ros/src/amigobot_LTL/model/ijrr_2013_improv/map.yaml')
    rate = rospy.Rate(25)	# 5Hz

    rospy.sleep(3)

    for i in range(0, prefixes[0].__len__()):
        bot_1.add_waypoint_from_waypt_list(prefixes[0][i])
    for i in range(0, prefixes[1].__len__()):
        bot_2.add_waypoint_from_waypt_list(prefixes[1][i])
    for i in range(0, prefixes[2].__len__()):
        bot_3.add_waypoint_from_waypt_list(prefixes[2][i])

    for i in range(1, suffix_cycles[0].__len__()):
        bot_1.add_waypoint_from_waypt_list(suffix_cycles[0][i])
    for i in range(1, suffix_cycles[1].__len__()):
        bot_2.add_waypoint_from_waypt_list(suffix_cycles[1][i])
    for i in range(0, suffix_cycles[2].__len__()):                      # range(0, ...)
        bot_3.add_waypoint_from_waypt_list(suffix_cycles[2][i])

    while not rospy.is_shutdown():
        if bot_1.is_all_done == True:
            for i in range(1, suffix_cycles[0].__len__()):
                bot_1.add_waypoint_from_waypt_list(suffix_cycles[0][i])

        if bot_2.is_all_done == True:
            for i in range(1, suffix_cycles[1].__len__()):
                bot_2.add_waypoint_from_waypt_list(suffix_cycles[1][i])

        if bot_3.is_all_done == True:
            for i in range(0, suffix_cycles[2].__len__()):
                bot_3.add_waypoint_from_waypt_list(suffix_cycles[2][i])

        rate.sleep()

    print("Finished!")

if __name__ == '__main__':
     try:
         main()
     except rospy.ROSInterruptException:
         pass
