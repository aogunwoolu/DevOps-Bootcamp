
## Questions

**Give 3 examples of special functions in python ?**
- Len
- Add 
- Main 
- Init

**Give 3 examples of agile principles**
  
**What does left shifting in terms of security and testing**

**Difference between scale horizontally and scale vertically**

**3 examples of estimation techniques**

## Gitlab
private git server, not hosted on github or bitbucket etc.
**no limit** to how much can be stored

now has updated to include CI server

### installing gitlab (EC2 instance)
https://about.gitlab.com/install/#amazonlinux-2

1. select EC2 page
2. select default AMI
	- **size**: t2.medium (can be bigger)
	- **storage**: 20 GiB (can be bigger/smaller)
	- **Tag**: name:GitLab
	- **Security group**: opening port 80/tcp (access from anywhere)
		- can open further
3. **signing into**:
	- download the ssh key
	- nativate to the location
	- ssh -i "github-ssh-key.pem" [user]@[ipv6/ipv4 address]
4. 
	**yum**: **Yellowdog Updater, Modified** (**YUM**)
		- free and open-source command-line package-management utility for computers running the Linux operating system using the RPM Package Manager.
	
	**curl**: 
		- curl (short for "Client URL") is a command line tool that enables data transfer over various network protocols. It communicates with a web or application server by specifying a relevant URL and the data that need to be sent or received.
	
	(-y flag means accept all)

	**postfix**: Postfix is **an open source mail-transfer agent** that was originally developed as an alternative to Sendmail and is usually set up as the default mail server.

	**chkconfig**: command is used to list all available services and view or update their run level settings. In simple words it is used to list current startup information of services or any particular service, updating _runlevel_ settings of service and adding or removing service from management.

	```bash
	sudo yum install postfix -y
	sudo service postfix start
	sudo chkconfig postfix on
¢	```
	
	**systemctl**: The systemctl command is a utility which is responsible for examining and controlling the systemd› system and service manager. It is a collection of system management libraries, utilities and daemons

	**|**: pipe, runs the next command with fed input from the previous
	**sudo**: gives elevates privileges 
	**bash**: returns to bash shell
	
	```bash
	curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash
	```

	**gitlab-ce**: community edition of the gitlab
	```bash
	sudo yum install gitlab-ce -y
	```
	**reconfigure**: 

	
	```bash
	# Check if opening the firewall is needed with: sudo systemctl status firewalld
	sudo firewall-cmd --permanent --add-service=http
	sudo firewall-cmd --permanent --add-service=https
	sudo systemctl reload firewalld
	```
