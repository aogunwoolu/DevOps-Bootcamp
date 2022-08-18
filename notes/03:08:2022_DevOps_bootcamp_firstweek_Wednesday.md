## Instrutor: Rob

Rob.Blincoe@QA.com

## AWS introduction

### architecting fundamentals

**Durability**: the servers will always be there

**Region**: an area with 2 or more availability zones

**VPC**: Virtual private cloud, your own area in the region (across availability zones). _cannot connect across regions natively_

- can build relationships between these called **peers**
- these peers are _non-transative_
  - ![Screenshot 2022-08-03 at 1.32.06 pm](https://imgur.com/MjLHudM.png)
  - QAC has relationship with QAHE but not QAA
- advised not to use the default VPC

**subnet**: inside VPCs (but in their own availability zones)

​	**public subnet**: you can access resources publically

​	**private subnet**: you have to access via an *IGW* (internet gateway)

you can connect a subnet to via a routing table (how the subnet can route traffic)

_if you connect a private subnet to the IGW via its routing table it becomes **public**_

**virtual machine**: these are refered to as EC2 instances

 - every EC2 instance has both a **public** and **private** address
   - just because you put a resource in a public subnet doesn't mean the resource can be connected to publically (you must give it a public address _or_ an elastic address)
   - public address: publically resolvable IP that is **dynamic**
   - _elastic IP_: publically resolvable IP that is **static**
     - limit of 5
     - can be moved between resources (detatched from one resource to another)

![Screenshot 2022-08-03 at 10.39.27 am](https://imgur.com/lYgO46x.png)

every subnet has a **firewall**, called a NACL (Network Access Control)

- default security group allows everything out, and everything in
- Stateless (does not remember that if you allow something in, it's allowed out)

every instance is has a **security group**, another firewall

- default security group allows everything out, but nothing in
- stateful (remembers that if you allow something in, it's allowed out)

you can communicate with any private machine within the same network, but you must satisfy security requirements, only if:

- Firewall of NACL allows communication 
- security group allows communication 

**elastic load balancer**: distributes traffic between resources

 - you can attatch an elastic IP to resources (EC2 instances) directly, but load balancer is a managed protected service ( which can distribute, if paired with *auto scaler* can relaunch instances)

   ![Screenshot 2022-08-03 at 10.45.09 am](https://imgur.com/odWPiPI.png)

**NAT Resource **: public resource that allows access to the internet (to allow for things like communication to internet update services)

- Network Address Translation
- NAT instance (unmanaged) - user managed
- NAT gateway (managed) 
  - **must** start within private network, ***NOT*** outside

![Screenshot 2022-08-03 at 11.03.24 am](https://imgur.com/S2Nt9RH.png)

**AMI**: Amazon Mahine Image

- images of OSs provided by Amazon
- Updates *image* not instance. to update instances, NAT may be required

**Account**: what subscriptions are in AWS

**Organisation**: a grouping of OUs (Organisational Unit) or a collection of accounts tht are treated as 1 entity 

- you can have up to 5 levels of OUs

 - Can apply ***policies***, ***reports*** and ***services***
   - these can be done on an OU level as opposed to the individual account
   - this is the best practice for policies

**IAM user**: user with permission that have jurisdiction over accounts

- a role can be used to extend the permissions of an IAM user
- can give jurisdiction in another account

![Screenshot 2022-08-03 at 1.50.09 pm](https://imgur.com/eOHivlf.png)

With perissions:

***explicit deny*** > ***implicit deny*** > ***permission grant***

**implicit**: picking permissions and leaving out things

**explicit**: picking denials

![Screenshot 2022-08-03 at 2.23.45 pm](https://imgur.com/mdk3LKc.png)

**Security/Service Control Policies (SCP)**: a policy linked to an OU, a _filter_ of permission

- gives global filter of permission. anyone who is an external IAM user is restricted by this rule
- it can be done by making another role, but this is can get out of hand

**Control Tower**: a managed service for creating organisation structure, this builds the hierarchy itself. Comes with guardrails: common practices 

_policy simulator_ is good tool for showing the permissions given to users with specific roles etc.

_policy generator_ is another good tool

AWS reserves the addresses:

- xxxx.xxxx.xxxx.0 - network
- xxxx.xxxx.xxxx.255 - broadcast
- xxxx.xxxx.xxxx.1
- xxxx.xxxx.xxxx.2
- xxxx.xxxx.xxxx.3

CIDR recap:

![Screenshot 2022-08-04 at 9.05.19 am](https://imgur.com/6aoH5hT.png)

front with a managed service: having managed service like load balance