
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
	
![](https://i.imgur.com/khpvcrt.png)
	
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
	**reconfigure**: command to reconfigure gitlab (setup), reverts changes and restarts services

	**gitlab-ctl**: gitlab control

	```bash
	sudo gitlab-ctl reconfigure
	```
![](https://i.imgur.com/jy6j9PX.png)

**to find the initial root password (if it does not prompt for password input)**:

**cat**: concatenate files and print on the standard output
```bash
sudo cat /etc/gitlab/initial_root_password
```
![](https://i.imgur.com/sRhSL8O.png)

**main gitlab dashboard**

![](https://i.imgur.com/be3lbOa.png)

5. **create a project**
	- select new project
	- give information to it
	- ![](https://i.imgur.com/575CpUF.png)
	- you can now clone with SSH & HTTP
	![](https://i.imgur.com/gWP80Gx.png)
	- cloning can now be done in any machine using
	```bash
	sudo yum install -y git
	git clone [repo address]
	```

## automating
upon creating the instance, under the **user data** field input the following
```bash
	#!/bin/bash
	sudo yum install postfix -y
	sudo service postfix start
	sudo chkconfig postfix on
	curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash
	sudo yum install gitlab-ce -y
	sudo gitlab-ctl reconfigure	
```

## backup gitlab server
sources:
https://nira.com/how-to-back-up-your-gitlab-server/#:~:text=Method%201%3A%20The%20Manual%20Method%20to%20Back%20Up%20Your%20GitLab%20Server&text=Log%20into%20your%20GitLab%20server,creation%20of%20your%20GitLab%20backup.

https://docs.gitlab.com/ee/raketasks/backup_restore.html
	https://docs.gitlab.com/ee/raketasks/backup_gitlab.html
	

**requirement**: rsync
```bash
# Debian/Ubuntu 
sudo apt-get install rsync

# RHEL/CentOS
sudo yum install rsync
```

1. log into GitLab server using SSH
2. use command:

**GitLab 12.2 or later:**
<strong>commandline:</strong>
```bash
sudo gitlab-backup create
```
**GitLab 12.1 or earlier:**
```bash
sudo gitlab-rake gitlab:backup:create
```

***find GitLab version***
https://stackoverflow.com/questions/21068773/how-to-check-the-version-of-gitlab

