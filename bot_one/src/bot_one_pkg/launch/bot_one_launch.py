from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='bot_one_pkg',
            executable='py_pub.py',
            name='py_pub_node',
            parameters=[
                
            ]
        ),
        Node(
            package='bot_one_pkg',
            executable='py_sub.py',
            name='py_sub_node',
            parameters=[
                
            ]
        ),
        ExecuteProcess(
            cmd=['ros2', 'topic', 'list'],
            output='screen'
        )
    ])