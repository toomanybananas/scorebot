#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import random,sys,os,time
# A simple, CP-finals-like scoring bot that checks for the status of critical services
# Can change ips and what not

# Config options
changeip = 0
# Whether or not to randomly change the ip of the scoring bot every check

changeip_address = ['192.168.1.200']
# Ip addresses that the score bot can use

check_content = 1
# Whether to verify the content of the service
# To do this, create a script running in host/service that returns 0 if the content is alright

# For more configuration options, search for HOST_CONFIG and TEAM_CONFIG

class host:
    def __init__(self, ip, services, hostname = ""):
        # Intialize some crap
        self.ip = ip
        self.services = services
        # Hostname is used for content checking. If we don't need that, don't even bother intializing
        if check_content == 1 and hostname != "":
            # Do some stuff relating to content checking here
            self.hostname = hostname

    def check(self):
        # Check the service. In this case we just run the associated script file
        score = {}
        for i in self.services:
            # Check if the service file exsists
            if not os.path.isfile("services/" + i):
                print("Error: handler for service " + i + " not found.")
                continue
            retval = os.system("services/" + i + " " + self.ip)
            if retval == 0:
                # The service is running, do some scoring stuff here
                #print("The service is up!")
                score[i] = 1
            else:
                # Oh no! The service is down. Do some scoring stuff here
                #print("The service is down!")
                score[i] = 0
        return score

    def checkcontent(self):
        # Execute a script to check the content
        for i in self.services:
            if not os.path.isfile(self.hostname + "/" + i):
                print("Error: content handler for service " + i + " on host " + self.hostname + " not found.")
                continue
            retval = os.system(self.hostname + "/" + i + " " + self.ip)
            if retval == 0:
                print("Content check succeded!")
            else:
                print("Content check failed.")

hosts = []
# HOST_CONFIG
# Configure your hosts here
# To add a host, do this:
# hosts.append(host("192.168.1.X", ["http","ssh"], "hostname")
#hosts.append(host("192.168.1.15", ["pop3", "ssh"], "strange"))

# Helper function to get the date and time
def getdate():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# Team class
class team:
    def __init__(self, teamid, hosts):
        self.teamid = teamid
        self.hosts = hosts # Array of hosts

        # Check if the team log directory exsists, if not create it
        if not os.path.isdir('team/' + str(self.teamid)):
            os.system('mkdir team/' + str(self.teamid))

    def check(self):
        # Open a log file for scoring
        log = open('team/' + str(self.teamid) + '/' + getdate() + '.txt', 'w') 
        # Check all of the hosts
        for h in self.hosts:
            log.write('HOST:' + h.hostname + '\n')
            score = h.check()
            #contentscore = h.checkcontent()
            for service, status in score.items():
                if status == 1:
                    log.write(service + ':up\n')
                else:
                    log.write(service + ':down\n')
            log.write('\n')


currentip = '192.168.1.200'

def changeipaddr():
    newaddr = changeip_address[random.randint(0, len(changeip_address))]
    if newaddr == currentip:
        changeipaddr()
        return
    os.system("ifconfig eth0 " + newaddr)

def main():
    # Do any host or team setup here
    strange = host('192.168.1.125', ['http', 'ssh'], 'strange')
    winter = host('192.168.1.126', ['http', 'ssh'], 'winter')
    #strange.check()
    #winter.check()
    
    #team1 = team(1, [strange, winter])
    #team1.check()

    # Actual, non testing team setup goes here
    teams = [
            team(2, [ 
                host('192.168.1.25', ['pop3', 'ssh'], 'strange'),
                host('192.168.1.26', ['http', 'ssh'], 'winter'),
                host('192.168.1.10', ['dns', 'dhcp'], '2008'),
                host('192.168.1.11', ['rdp', 'print'], '2012')
                ]),
            team(3, [ 
                host('192.168.1.35', ['pop3', 'ssh'], 'strange'),
                host('192.168.1.36', ['http', 'ssh'], 'winter'),
                host('192.168.1.30', ['dns', 'dhcp'], '2008'),
                host('192.168.1.31', ['rdp', 'print'], '2012')
                ]),
            team(4, [ 
                host('192.168.1.45', ['pop3', 'ssh'], 'strange'),
                host('192.168.1.46', ['http', 'ssh'], 'winter'),
                host('192.168.1.40', ['dns', 'dhcp'], '2008'),
                host('192.168.1.41', ['rdp', 'print'], '2012')
                ]),
            team(5, [ 
                host('192.168.1.55', ['pop3', 'ssh'], 'strange'),
                host('192.168.1.56', ['http', 'ssh'], 'winter'),
                host('192.168.1.50', ['dns', 'dhcp'], '2008'),
                host('192.168.1.51', ['rdp', 'print'], '2012')
                ]),
            team(6, [ 
                host('192.168.1.65', ['pop3', 'ssh'], 'strange'),
                host('192.168.1.66', ['http', 'ssh'], 'winter'),
                host('192.168.1.60', ['dns', 'dhcp'], '2008'),
                host('192.168.1.61', ['rdp', 'print'], '2012')
                ]),
            team(7, [ 
                host('192.168.1.75', ['pop3', 'ssh'], 'strange'),
                host('192.168.1.76', ['http', 'ssh'], 'winter'),
                host('192.168.1.70', ['dns', 'dhcp'], '2008'),
                host('192.168.1.71', ['rdp', 'print'], '2012')
                ]),
            team(8, [ 
                host('192.168.1.85', ['pop3', 'ssh'], 'strange'),
                host('192.168.1.86', ['http', 'ssh'], 'winter'),
                host('192.168.1.80', ['dns', 'dhcp'], '2008'),
                host('192.168.1.81', ['rdp', 'print'], '2012')
                ]),
            team(9, [ 
                host('192.168.1.95', ['pop3', 'ssh'], 'strange'),
                host('192.168.1.96', ['http', 'ssh'], 'winter'),
                host('192.168.1.90', ['dns', 'dhcp'], '2008'),
                host('192.168.1.91', ['rdp', 'print'], '2012')
                ]),
            team(10, [ 
                host('192.168.1.105', ['pop3', 'ssh'], 'strange'),
                host('192.168.1.106', ['http', 'ssh'], 'winter'),
                host('192.168.1.100', ['dns', 'dhcp'], '2008'),
                host('192.168.1.101', ['rdp', 'print'], '2012')
                ]),
            team(11, [ 
                host('192.168.1.115', ['pop3', 'ssh'], 'strange'),
                host('192.168.1.116', ['http', 'ssh'], 'winter'),
                host('192.168.1.110', ['dns', 'dhcp'], '2008'),
                host('192.168.1.111', ['rdp', 'print'], '2012')
                ]),
            team(12, [ 
                host('192.168.1.125', ['pop3', 'ssh'], 'strange'),
                host('192.168.1.126', ['http', 'ssh'], 'winter'),
                host('192.168.1.120', ['dns', 'dhcp'], '2008'),
                host('192.168.1.121', ['rdp', 'print'], '2012')
                ])
            ]
    while True:
        time.sleep(random.randint(3, 5) * 60)
        print("Scoring the teams at " + getdate())
        for i in teams:
            i.check()
main()
