
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

**yum**: **Yellowdog Updater, Modified** (**YUM**)
	- free and open-source command-line package-management utility for computers running the Linux operating system using the RPM Package Manager.

**curl**: 
	- curl is a command-line tool to transfer data to or from a server, using any of the supported protocols (HTTP, FTP, IMAP, POP3, SCP, SFTP, SMTP, TFTP, TELNET, LDAP, or FILE)

(-y flag means accept all)

```bash
sudo yum install -y curl policycoreutils-python openssh-server openssh-clients perl
```

**systemctl**: The systemctl command is a utility which is responsible for examining and controlling the systemd system and service manager. It is a collection of system management libraries, utilities and daemons

Enable OpenSSH server daemon if not enabled: sudo systemctl status sshd
```bash
sudo systemctl enable sshd
sudo systemctl start sshd
```

```bash
# Check if opening the firewall is needed with: sudo systemctl status firewalld
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo systemctl reload firewalld
```
