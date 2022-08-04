## Review

## Management & Government

John Savill (Azure cloud youtuber)

nobody knows exactly what things will cost

- services in resource group take money
  - Disk (always paying for egress)
  - VM
  - public IP
- **Blueprints** are groups of policies, to export into another environment
- **Locks**, allow for resources to be locked from being modified or deleted
  - even if you delete Resource Group, if there is even ***one*** resource with lock, it cannot be deleted
  - you can put a lock on anything (including resource groups)
- get into making good naming conventions as ***YOU CANNOT RENAME THINGS***

You can verify service health, and MS reports on issues in zones. This feeds into the SLA.

After creating a vertual machine you can **create a VM template** that can be used on or offline

## Monitoring Tools

- activity log
  - activity log is in any resource (giving log of what has happened, daulted to 6 hours in the past)
  - can set alerts based on activity log (attaching logic actions, or set to inform you)
- advisor
  - gives score of how secure and good your environment is
- monitor
  - includes activity logs
  - has metrics
  - can query logs in a read-only way (to ensure accurate logs)
- Sentinel 
  - AI that can take action to secure your environment 

**Enterprise agreement**: negotiate volume discount directly with Microsoft based on predicted spend

**Microsoft Partner Agreement**: Consultation and support with your cloud solution provider rather than Microsoft directly. Discount off RRP

**SIEM**: security information events management

**SOAR**: security automated response 