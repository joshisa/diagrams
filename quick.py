# diagram.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.ibm.compute import Internet
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Web Service", show=False):
    Internet("WWW") >> EC2("web") >> RDS("userdb")
