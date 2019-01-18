

from pynodered import node_red, NodeProperty


@node_red(category="pyfuncs")
def lower_case(node, msg):

    msg['payload'] = msg['payload'].lower()
    return msg


@node_red(category="pyfuncs",
          properties=dict(number = NodeProperty("Number", value="1")))
def repeat(node, msg):

    msg['payload'] = msg['payload'] * int(node.number.value)
    return msg
