# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

*Cost*
- VM: Since you have total control over the underlying operating system, custom configurations, and custom software, you need infrastructure engineers to concentrate on maintaining
- App Service: Cost efficiency - A single App Service plan can contain multiple applications as long as the plan has enough resources to handle the increasing load. The disadvantage: If you need to upgrade a portion of your App tier, you much upgrade to the next plan tier => higher cost

*Scalability*
- In VMs, horizontal scaling is achieved via Scale Sets
    - require separate load balancer
    - if existing VM does not belong to Scale Set, it might need a bit of configuration work to enable
- App Service provides an Integrated load balancer and can easily increase instances

In conclusion, we would like to use App Service for deploying this web app.

