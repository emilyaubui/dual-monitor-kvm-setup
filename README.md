# KVM Setup Dual Displays with 1 PC + 1 Laptop
## A solution for home office users with two devices and way too many peripherals to manage

### The Problem

When I started WFH, I had a problem. I was constantly swapping cables from my home PC to my work laptop trying to use the personally curated selection of peripherals I already had. Instead of buying another keyboard, mouse, etc. and creating a separate workspace, I needed a solution that would make this switch between my PC and laptop frictionless. I had a few requirements going into my research. 

### Requirements
* Support Dual DisplayPort 1.4
* Simultaneously handle 1440p@240Hz & 1080p@165Hz
* EDID emulation (more on that later)
* Enough ports for at least 4 USB devices (keyboard, mouse, microphone, webcam)
* Support TB4 connection to laptop

### Research
My final setup was heavily inspired by [ConnectPRO's Guide](https://www.connectpro.com/blogs/news/the-ultimate-kvm-switch-setup-for-dual-monitor-sharing-with-one-mac-and-one-pc-system). 

### Setup
Here's a diagram I whipped up with Python Diagrams as Code: 
<picture>
  <source srcset="./kvm_setup.png" width=50%>
  <img src="./kvm_setup.png">
</picture>
