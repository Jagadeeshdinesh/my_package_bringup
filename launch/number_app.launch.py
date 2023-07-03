from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    publisher_node = Node(
        package="my_package",
        executable="publisher",
        name="publisher_python",
        remappings=[
            ("robot_news", "publisher_message_python")
        ],
        parameters=[
            {"frequency": 10},
            {"robot_namespace":"minion"}
        ]
    )

    publisher_cpp_node = Node(
        package="my_package_cpp",
        executable="publisher",
        name="publisher_cpp",
        remappings=[
            ("publisher_message", "publisher_message_cpp")
        ],
        parameters=[
            {"frequency": 20}
        ]
    )

    ld.add_action(publisher_node)
    ld.add_action(publisher_cpp_node)

    return ld