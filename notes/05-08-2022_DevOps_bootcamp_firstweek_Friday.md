## Automation

cloudformation is automation product (for AWS specifcally)

Terraform is automation product for **any** cloud product

Elastic beastalk is managed automation



## Containerisation

**ECS**: elastic container service

- has cluster of EC2 instaces
- ECS creates area that machines can run (a cluster)
- ECS asks you things like:
  - what AMI you want
  - what ASG you want
  - the spec
  - what ELB you want
  - what monitoring you want

**ECR**: elastic container registry

- stores machine images
- containers in clusters then have instances based off ECR images

Alternatively, there is **fargate**: serverless containerisation which is managed.

**ECS** _vs_ **Fargate**

**kurbernetes**: orchestrator

- planes
- Pods

## Networking

**VPG**: virtual private gateway

instances can only communicate with things inside VPN

things like **dynamo DB** are outside of the VPC

Instead of routing through IGW, you can configure traffick specifically using an ***endpoint***

2 types of endpoint:

1. gateway endpoint
   - routing table entry.
   - can only be used for dynamo DB and 
2. dynamic endpoint
   1. NIC

privatelink is the link being create though the endpoint connection

***VPC peer*** connection is setting up routing table entry, but it is not transitive

**transit gateway (TGW)**: helps manage peer connections between VPCs and on premises.

	- routes different VPC peers, allowing for a sort of transitiveness 
	- these are region bound whereas peer connections can go across regions
	- can configure connections between TGWs
 - paying for each attachment to TGW (whether sending trsaffic or not)
   - gets pretty expensive, so in relation to VPC peers it may not be the best decision

**Direct Connect Gate Way (DCGW)**: helps connect to transit gateways

Route 53: DNS which directs traffic through region

**serverless**:

- Done on your behalf
- managed

API gateway can handle API requests

**message queue**:

- sending messages using polling



## edge computing

things can be done to help with latency.

- Outposts: on premise VPN (physical data rack)
- AWS wavelength: 5g providers can host resources in data center
- AWS edge locations: access backbone, cloufront etc
- Local zone: using resources closer to users (not preference but actual SLA)

**edge caching** the cloudfront already has the data from the origin, making fetching much easier

	- with dynamic content, cloudfront controls how the traffic gets there (making it faster)
	- can dictate protocol
	- Embargo countries/IP ranges

![Screenshot 2022-08-05 at 4.09.21 pm](https://imgur.com/PB6dek3.png)

when caching in **cloufront**, you give it a TTL (time to live)

- can remove unwanted information by renaming/changing TTL (free) or invalidating the object (paid)
- Security

**global accelerator**: redirecting traffic

	- sends the traffic to where it wants to be
	- instead of going to the content, using the AWS backbone (faster): gets user to the data
	- redirects to the closer location

at every layer of the ASI layer model, AWS can protect against DDoS

**outpost**: physically have AWS resources in your server (bring the cloud to you)

## backup & recovery

**Disaster Recovery (DR)**

**disaster planning**: testing, resources, planning

**FIS**: emulates failure, if this failed how would AWS config fair with huge breakages

**AWS backup**: backs up storage, instances etc.

**Recovery Strategies**:

1. backup and recovery
2. pilot light
   - switch AWS service off, while using production solution
   - keep backup of DB in AWS S3
   - in event of production failure, redirect to recovery
3. fully working low-capacity standby
   - keep both production + backup in use
   - in the event of production failure, switch fully to recovery & scale
4. Multi-site active-active
   - both production + recovery are active fully 
   - in the event of production failure, send to cloud and vice versa



online course supplement: https://www.aws.training/Details/eLearning?id=78882. 



Https://evaluation.qa.com

- zskydevopw1
- 4737222-5