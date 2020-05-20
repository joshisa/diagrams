"""
IBM provides a set of services for the IBM Cloud provider.
"""

from diagrams import Node


class _IBM(Node):
    _provider = "ibm"
    _icon_dir = "resources/ibm"

    fontcolor = "#2d3436"
