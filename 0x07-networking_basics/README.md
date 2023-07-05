# Networking basics #0

## Learning Objectives
### OSI Model
- What it is
- How many layers it has
- How it is organized

### What is a LAN
- Typical usage
- Typical geographical size

### What is a WAN
- Typical usage
- Typical geographical size

### What is the Internet
- What is an IP address
- What are the 2 types of IP address
- What is localhost
- What is a subnet
- Why IPv6 was created

### TCP/UDP
- What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
- What is the main difference between TCP and UDP
- What is a port
- Memorize SSH, HTTP and HTTPS port numbers
- What tool/protocol is often used to check if a device is connected to a network

## Resources
- [OSI model](https://en.wikipedia.org/wiki/OSI_model)
- [Different types of network](https://www.lifewire.com/lans-wans-and-other-area-networks-817376)
- [LAN network](https://en.wikipedia.org/wiki/Local_area_network)
- [WAN network](https://en.wikipedia.org/wiki/Wide_area_network)
- [Internet](https://en.wikipedia.org/wiki/Internet)
- [MAC address](https://whatismyipaddress.com/mac-address)
- [What is an IP address](https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/)
- [Private and public address](https://www.iplocation.net/public-vs-private-ip-address)
- [IPv4 and IPv6](https://www.webopedia.com/insights/ipv6-ipv4-difference/)
- [Localhost](https://whatismyipaddress.com/localhost)
- [TCP and UDP](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
- [TCP/UDP ports List](https://en.wikipedia.org/wiki/Main_Page)
- [What is ping /ICMP](https://en.wikipedia.org/wiki/Ping_%28networking_utility%29)
- [Positional parameters](https://wiki.bash-hackers.org/scripting/posparams)

##### man or help:
- netstat
- ping

### Requirements
- Allowed editors: vi, vim, emacs
- All your Bash script files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass shellcheck without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing

### More Info
- The second line of all your Bash scripts should be a comment explaining what is the script doing

- For multiple choice question type tasks, just type the number of the correct answer in your answer file, add a new line for every new answer, example:

- What is the most important position in a software company?
1. Project manager
2. Backend developer
3. System administrator


## Tasks
- [x] 0-OSI_model - OSI model
OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

It is organized from the lowest level to the highest level:

- The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
- The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc
Keep in mind that the OSI model is a concept, it’s not even tangible. The OSI model doesn’t perform any functions in the networking process. It is a conceptual framework so we can better understand complex interactions that are happening. Most of the functionality in the OSI model exists in all communications systems.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/4e6a0ad87a65d7054248.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230705T052253Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e3dacc9baf4c13439f88182f304bcbeb8bb05962783494965510cde19ab7cf35)

In this project we will mainly focus on:

- The Transport layer and especially TCP/UDP
- On the Network layer with IP and ICMP
The image bellow describes more concretely how you can relate to every level.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/0fc96bd99faa7941b18bcae4c5f90c6acd11791d.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230705T052253Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=21906240d4b69234df118043d60530a9334f8ac468f8a43045cc8a29ca6be1cb)

Questions:

What is the OSI model?

1. Set of specifications that network hardware manufacturers must respect
2. The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
3. The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology
How is the OSI model organized?

1. Alphabetically
2. From the lowest to the highest level
3. Randomly

- [x] 1-types_of_network - Types of network
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/4b995d4f8078b44afa968d68a98035d2bd7e8fac.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230705T052253Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f316733e197e7db5273b6dfc256097a024f14101018b742fb448be638631f0d0)
 
LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

Questions:

What type of network a computer in local is connected to?

- Internet
- WAN
- LAN
What type of network could connect an office in one building to another office in a building a few streets away?

- Internet
- WAN
- LAN
What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?

- Internet
- WAN
- LAN


- [x] 2-MAC_and_IP_address - MAC and IP address
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/1e348ba3bcbb094b02922f821ffeb3d8c5438b7b.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230705T052253Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9f8ea41bef4d739ff53ee54dbdceab33d203586bac4a98ee41194d6362a7dbdd)
Questions:

What is a MAC address?

- The name of a network interface
- The unique identifier of a network interface
- A network interface
What is an IP address?

- Is to devices connected to a network what postal address is to houses
- The unique identifier of a network interface
- Is a number that network devices use to connect to networks


- [x] 3-UDP_and_TCP -  UDP and TCP
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/3d92e3c4a470f8ecf4c73db511fcbbadaa002e1c.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230705T052253Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7ea86ce6852707f45fbe6deb2968dd32dfc458238cc7d8665e4740e50581881a)
Let’s fill the empty parts in the drawing above.

Questions:

Which statement is correct for the TCP box:
1. It is a protocol that is transferring data in a slow way but surely
2. It is a protocol that is transferring data in a fast way and might loss data along in the process

Which statement is correct for the UDP box:
1. It is a protocol that is transferring data in a slow way but surely
2. It is a protocol that is transferring data in a fast way and might loss data along in the process

Which statement is correct for the TCP worker:
1. Have you received boxes x, y, z?
2. May I increase the rate at which I am sending you boxes?


- [x] 4-TCP_and_UDP_ports - TCP and UDP ports
Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.

If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.

While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:

- 22 for SSH
- 80 for HTTP
- 443 for HTTPS
Note that a specific IP + port = socket.

Write a Bash script that displays listening ports:

- That only shows listening sockets
- That shows the PID and name of the program to which each socket belongs


- [x] 5-is_the_host_on_the_network - Is the host on the network
![](https://media.giphy.com/media/uDxkJAVSU7GY8/giphy.gif)

The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command ping uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.

Write a Bash script that pings an IP address passed as an argument.

Requirements:

- Accepts a string as an argument
- Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
- Ping the IP 5 times

## endif
