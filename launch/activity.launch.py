from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    robot_name = ["jagu", "yavan", "abi", "stalin", "ravi", "jb"]
    publisher_ = []
    for name in robot_name:
        publisher_.append(Node(
        package="my_package",
        executable="publisher",
        name="publisher_python_" + name.lower(),
        # remappings=[
        #     ("robot_news", "publisher_message_python")
        # ],
        # parameters=[
        #     {"frequency": 10},
        #     {"robot_namespace":"minion"}
        # ]
    ))

    # publisher_cpp_node = Node(
    #     package="my_package_cpp",
    #     executable="publisher",
    #     name="publisher_cpp",
    #     remappings=[
    #         ("publisher_message", "publisher_message_cpp")
    #     ],
    #     parameters=[
    #         {"frequency": 20}
    #     ]
    # )

    for node in publisher_:
        ld.add_action(node)
    # ld.add_action(publisher_cpp_node)

    return ld