# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

*Cost*

I use [Azure Pricing Calculator](https://azure.microsoft.com/en-in/pricing/calculator/) to estimate the cost when using VM or App Service with almost same configuration. 
- VM: Region (East US), Operating system (Linux - Ubuntu), Tier (Basic), 1 instance (A1: 1 Cores, 1.75 GB RAM) - 730 Hours: $16.79 Average per month
- App Service: Region (East US), Operating system (Linux - Ubuntu), Tier (Basic), 1 instance (B1: 1 Cores, 1.75 GB RAM) - 730 Hours: $12.41 Average per month

=> App Serive is cheaper than VM

*Scalability*

- In VMs, horizontal scaling is achieved via Scale Sets
    - require separate load balancer
    - if existing VM does not belong to Scale Set, it might need a bit of configuration work to enable
- App Service provides an Integrated load balancer and can easily increase instances

*Availability*

Follow Microsoft service level agreement (SLA), we have: 
- VM: The availability for VMs depends on the number and configuration of the instances. Azure offers the following SLAs for VMs (99.9% for a single instance VM, 99.95% for two or more instances in the same availability set, 99.99% for two or more instances across two or more availability zones)
- App Service: Microsoft guarantees that Azure App Service will be available 99.95% of the time when running on either a single instance or on multiple instances.

*Workflow*

- VM is a Infrastructure as a Service (IaaS). The workflow of VMs can be divided into 2 main stages: deployment and management. During the deployment stage, users can create a new VM by selecting an image of their preferred operating system and specifying the desired hardware configuration. In the management stage, users can monitor and manage their VMs using Azure portal or command-line interface. This includes tasks such as starting and stopping VMs, resizing VMs, and configuring network settings.
- App Service is a Platform as a service (PaaS). The workflow for deploying an app to App Service involves configuring continuous deployment from a source code repository such as GitHub, Bitbucket, or Azure Repos. This will enable automatic deployment of updates to your app whenever changes are pushed to the selected branch of your repository.

Since my web app is a simple website, I consider:
- a low cost
- easy to deploy and manage
- scalability and availability (optional)

I decide to use App Service in my project.
