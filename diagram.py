#import diagram, cluster, edge, node, and os functions
from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
import os

edge_font = "10"

with Diagram(
    "KVM Setup",
    filename="kvm_setup",
    show=False, #no xdg lib installed; instead use os module to open window's file opener
    direction="TB",
    curvestyle="ortho",
    outformat="png",
    node_attr={
        "fontsize": "12",
        "fontname": "Helvetica",
        "labelloc": "t",
        "labeljust": "c",
    },
    edge_attr={
        "color": "black",
        "style": "solid",
        "fontname": "Helvetica",
        "arrowsize": "1",
        "penwidth": "2",
    },
):        
    outlet = Custom("Power","./icons/outlet.png")

    with Cluster("Switch & Hubs"):  
        kvm = Custom("Steetek KVM\n8k@60Hz", "./icons/kvm.png")  
        switch = Custom("Switch","./icons/switch.png")
        tb4_dock = Custom("TB4 Dock","./icons/tb4-dock.png")
        hub = Custom("USB3.0 hub\n(no PD)", "./icons/usb3-hub.png")

    with Cluster("Devices"):
        computer = Custom("PC","./icons/pc.png")
        laptop = Custom("Thinkpad Yoga\nX13 G2","./icons/pc.png") 

    with Cluster("Monitors"):
        main = Custom("1440p@240Hz","./icons/screen.png")
        secondary = Custom("1080p@165Hz","./icons/screen.png") 
    
    with Cluster("Peripherals"):
        headset = Custom("Logitech G733", "./icons/headphones.png")
        mouse = Custom("Pulsar 2XA", "./icons/mouse.png")
        webcam = Custom("Logitech C920S", "./icons/webcam.png")
        keyboard = Custom("Rainy75", "./icons/keyboard.png")
        mic = Custom("Fifine AM8", "./icons/mic.png")
        
        with Cluster("USB Dongles"):
            headset_usb = Custom("Logitech G733\nUSB Receiver", "./icons/usb.png")
            mouse_usb = Custom("Pulsar X2A\nUSB Receiver", "./icons/usb.png")

    laptop << Edge(label="TB4", fontsize=edge_font, decorate="true") >> tb4_dock 
    kvm << Edge(label="2xDP1.4+1xUSB2", fontsize=edge_font, decorate="true") >> [
        computer,
        tb4_dock,
        ]
    kvm << Edge(fontsize=edge_font, decorate="true") >> [
        mic,
        webcam,
        hub
        ]
    kvm >> Edge(label="2xDP1.4", fontsize=edge_font, decorate="true") >> [
        main,
        secondary
        ]
    kvm << Edge(label="CTRL", fontsize=edge_font, decorate="true") << switch
    kvm << Edge(label="DC12V/1A", fontsize=edge_font, decorate="true") << outlet
    hub << Edge(fontsize=edge_font, decorate="true") >> [
        headset_usb,
        mouse_usb,
        keyboard,
    ]
    headset_usb >> \
        Edge(label="Wireless", fontsize=edge_font, style="dashed", color="grey") >> \
        headset
    mouse_usb >> \
        Edge(label="Wireless", fontsize=edge_font, style="dashed", color="grey") >> \
        mouse
    switch - Edge(penwidth="0") - outlet

            
        











#open with window's file opener
os.system("explorer.exe kvm_setup.png")