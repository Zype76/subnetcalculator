# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 10:32:17 2017

@author: Paul Hansen
Version 2.0
"""
import tkinter as tk

#To calcuate the IP    
def privateip(): 
    ipA = ipaddres_label.get()
    ipaddrs = ipA.split('.')
    terrible = list(range(16,31))
    if len(ipaddrs) != 4: 
        ipCout["text"] = "You need to enter an ip address..."
    
    lame = int(ipaddrs[1])
    
    if ipaddrs[0] == "192" and ipaddrs[1] == "168":
        ipCout["text"] = "This is a private ip"
        
    elif ipaddrs[0] == "10":
        ipCout["text"] = "This is a private ip"
        
    elif ipaddrs[0] == "172" and  lame in terrible: 
        ipCout["text"] = "This is a private ip"

    elif ipaddrs[0] == "169" and  ipaddrs[1] == "254":
        ipCout["text"] = "This is a link local address!"
        
    else:
        ipCout["text"] = "This is a public ip address"

#Subnet calculator 
def subnetcalc():
     #still working on the subnet calculation
     snet_dictionary = {
      "31":"255.255.255.254",
      "30":"255.255.255.252",
      "29":"255.255.255.248",
      "28":"255.255.255.240",
      "27":"255.255.255.224",
      "26":"255.255.255.192",
      "25":"255.255.255.128",
      "24":"255.255.255.0",
      "23":"255.255.254.0",
      "22":"255.255.252.0",
      "21":"255.255.248.0",
      "20":"255.255.240.0",
      "19":"255.255.224.0",
      "18":"255.255.192.0",
      "17":"255.255.128.0",
      "16":"255.255.0.0",
      "15":"255.254.0.0",
      "14":"255.252.0.0",
      "13":"255.248.0.0",
      "12":"255.240.0.0",
      "11":"255.224.0.0",
      "10":"255.192.0.0",
      "9":"255.128.0.0",
      "8":"255.0.0.0",
      "7":"254.0.0.0",
      "6":"252.0.0.0",
      "5":"248.0.0.0",
      "4":"240.0.0.0",
      "3":"224.0.0.0",
      "2":"192.0.0.0",
      "1":"128.0.0.0",}
     snet_mask = subnet_label.get()
     subnet_host["text"] = (2 ** (32 - int(snet_mask)) -2)
     sbnetout["text"] = snet_dictionary[snet_mask]


#Run both functions when you click the button :^)
def runbothfunctions():
    privateip()
    subnetcalc()
    
# Make a top level Tk window
root = tk.Tk()
root.title("IP calculator")
root.resizable(width=False, height=False)

#Input prompts and stuff: 
tk.Label(root, text="Enter ip:").grid(row=0, column=0)
tk.Label(root, text="Subnet mask CIDR notation:").grid(row=1, column=0)
tk.Label(root, text = 'Public or private? ').grid(row=2, column=0)
tk.Label(root, text = 'Subnet mask: ').grid(row=3, column=0)
tk.Label(root, text = 'Usable hosts: ').grid(row=4, column=0)


#Dem inputs 
ipaddres_label = tk.Entry(root)
ipaddres_label.grid(row=0, column=1)

subnet_label = tk.Entry(root)
subnet_label.grid(row=1, column=1)

#Dem calculations
subnet_host = tk.Label(root, text = '')
subnet_host.grid(row=4, column=1)

#Dem outputs
ipCout = tk.Label(root, text = '')
ipCout.grid(row=2, column=1)

sbnetout = tk.Label(root, text = '')
sbnetout.grid(row=3, column=1)

#To calcuate the result 
dank_button = tk.Button(root, text="Calculate", command=runbothfunctions)
dank_button.grid(row=5,column=1)

#To exit: 
tk.Button(root, text="Quit", command=quit).grid(row=5,column=0)

#A function I created to exit the widget. 
def quit():
    root.destroy()
    
root.mainloop()
