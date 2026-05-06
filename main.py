#import diagram, cluster, edge, node, and os functions
from diagrams import Diagram, Cluster, Edge, Node
from diagrams.custom import Custom

graph_attr = {
      "splines": "spline",
      "layout": "neato",
      "overlap": "false",
      "compound": "true",
      "bgcolor": "transparent",
}

import os

#diagram export settings
with Diagram("\nDual DP Monitors with 1 PC + 1 Laptop",
    show=False, #no xdg lib to open file, using os module to let windows choose method to open diagram
    outformat="png",
    filename="kvm_setup",
    direction="TB",
    graph_attr=graph_attr) as diag:

    with Cluster("Desk"):
        with Cluster("Monitors"):
            main_screen = Custom("Asus XG27UCG-W\n1440p@240Hz", "./icons/screen.png", pin="true", pos="0,5")
            second_screen = Custom("Sceptre E248B-FPT168\n1080p@165Hz", "./icons/screen.png", pin="true", pos="1,5")
        with Cluster("Devices"):
            computer = Custom("Custom PC", "./icons/pc.png", pin="true", pos="3,5")
            laptop = Custom("Thinkpad X13 Yoga G2", "./icons/laptop.png", pin="true", pos="4,5")

    with Cluster("Switch + Hubs", graph_attr={"rank": "same"}):
        kvm_switch = Custom("Steetek KVM\n80K@60Hz", "./icons/kvm.png", pin="true", pos="2,3")
        usb3_hub = Custom("USB3.0 4-Port Hub\nNo Charging Function", "./icons/usb3-hub.png", pin="true", pos="0.5,3,")
        tb4_dock = Custom("Cable Matters\nUSB4 Mini Dock w/ Dual DP", "./icons/tb4-dock.png", pin="true", pos="3.5,3")

    with Cluster("Peripherals"):
        headset = Custom("Logitech G733", "./icons/headphones.png", pin="true", pos="0.5,0")
        mouse = Custom("Pulsar 2XA", "./icons/mouse.png", pin="true", pos="1.5,0")
        webcam = Custom("Logitech C920S", "./icons/webcam.png", pin="true", pos="2.5,1")
        keyboard = Custom("Rainy75", "./icons/keyboard.png", pin="true", pos="3,0")
        mic = Custom("Fifine AM8 via USB-C", "./icons/mic.png", pin="true", pos="3.5,1")
        
        with Cluster("USB Dongles"):
            headset_usb = Custom("Logitech G733\nUSB Receiver", "./icons/usb.png", pin="true", pos="0.5,1")
            mouse_usb = Custom("Pulsar X2A\nUSB Receiver", "./icons/usb.png", pin="true", pos="1.5,1")

    laptop >> Edge(label="Thunderbolt 4 USB-C")>>tb4_dock
    kvm_switch << Edge(label="2xDP 1.4\n+ 1xUSB3.0") >> [
        main_screen,
        second_screen,
        computer, 
        tb4_dock
    ]
    kvm_switch << [
        mic,
        webcam,
    ]
    kvm_switch << usb3_hub << [
        headset_usb,
        mouse_usb,
        keyboard,
    ]
    headset_usb >> Edge(color="blue", style="dashed") >> headset
    mouse_usb >> Edge(color="blue", style="dashed") >> mouse
    
#open with window's file opener
os.system("explorer.exe kvm_setup.png")