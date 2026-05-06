#import diagrams & custom nodes
from diagrams import Diagram, Cluster
from diagrams.custom import Custom

with Diagram("Dual DP Monitors with 1 PC + 1 Laptop", show=False, outformat="png", filename="kvm_setup", direction="TB"):

    computer = Custom("Custom PC", "./icons/pc.png")
    laptop = Custom("Thinkpad X13 Yoga Gen 2", "./icons/laptop.png")
    kvm_switch = Custom("Steetek\n80K@60Hz Dual DP KVM Switch", "./icons/kvm.png")
    tb4_dock = Custom("Cable Matters\nUSB4 Mini Dock w/ Dual DP", "./icons/tb4-dock.png")
    usb3_hub = Custom("Generic USB3.0 4-Port Hub\nNo Charging Function", "./icons/usb3-hub.png")

    with Cluster("Monitors"):
        main_screen = Custom("Asus XG27UCG-W\n1440p@240Hz", "./icons/screen.png")
        second_screen = Custom("Sceptre E248B-FPT168\n1080p@165Hz", "./icons/screen.png")

    with Cluster("Peripherals"):
        headset_usb = Custom("Logitech G733\nUSB Receiver", "./icons/usb.png")
        headset = Custom("Logitech G733", "./icons/headphones.png")
        mouse_usb = Custom("Pulsar X2A\nUSB Receiver", "./icons/usb.png")
        mouse = Custom("Pulsar 2XA", "./icons/mouse.png")
        keyboard = Custom("Rainy75", "./icons/keyboard.png")
        mic = Custom("Fifine AM8 via USB-C", "./icons/mic.png")
        webcam = Custom("Logitech C920S", "./icons/webcam.png")

        peripherals = [headset_usb, mouse_usb, keyboard, mic, webcam]

    kvm_switch - [
        main_screen,
        second_screen,
        tb4_dock,
        *peripherals
        ]
    
