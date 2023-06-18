#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move_line():
    rospy.init_node('twist_publisher')
    twist = Twist()
    twist.angular.z = 0 #0.5
    twist.linear.x = 0.5
    pub = rospy.Publisher('/cmd_vel',Twist , queue_size=1)
    r = rospy.Rate(2)
    while not rospy.is_shutdown(): 
        pub.publish(twist)
        r.sleep()


def move_circle():
    rospy.init_node('move_circle')
    twist = Twist()
    twist.angular.z = 1 #0.5
    twist.linear.x = 1
    pub = rospy.Publisher('/cmd_vel',Twist , queue_size=1)
    r = rospy.Rate(2)
    while not rospy.is_shutdown(): 
        pub.publish(twist)
        # r.sleep()
    
def move_straight():
    rospy.init_node('move_straight')
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    distance = 10
    vel_msg.linear.x = 1

    while not rospy.is_shutdown():
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while current_distance < distance:
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_distance = t1 - t0
        
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)

def move_square():
        rospy.init_node('twist_publisher')
    stop = Twist()
    
    straight = Twist()
    straight.linear.x = 0.1

    turn_right = Twist()
    turn_right.linear.x = 0
    turn_right.linear.y = 0
    turn_right.linear.z = 0
    turn_right.angular.z = -0.37
    pub = rospy.Publisher('/cmd_vel',Twist , queue_size=4)
    r = rospy.Rate(0.2)

    time.sleep(1)
    for i in range(4):
        pub.publish(straight)
        time.sleep(4)
        pub.publish(stop)
        time.sleep(1.5)
        pub.publish(turn_right)
        time.sleep(4.37)
        pub.publish(stop)
        time.sleep(1)
        r.sleep()
    pub.publish(stop)

if __name__ == "__main__":
    # move_straight()
    move_circle()
    # move_square()
    # move_line()
