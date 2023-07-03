from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    publisher_node = Node(
        package="my_package",
        executable="publisher"
    )

    publisher_cpp_node = Node(
        package="my_package_cpp",
        executable="publisher"
    )

    ld.add_action(publisher_node)
    ld.add_action(publisher_cpp_node)

    return ld