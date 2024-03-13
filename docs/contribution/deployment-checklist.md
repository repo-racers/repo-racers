# Production Environment Checklist (Azure)

1. [Server-side](#server-side)
1. [Client-side](#client-side)
1. [Data storage](#data-storage)
1. [Scalability and High Availability](#scalability-and-high-availability)
1. [Continuous Integration](#continuous-integration)
1. [Continuous Delivery](#continuous-delivery)
1. [Networking](#networking)
1. [Security](#security)
1. [Monitoring](#monitoring)
1. [Cost optimization](#cost-optimization)

## Server-side

### Build VM Images

If you want to run your apps directly on [Azure Virtual Machines](https://docs.microsoft.com/en-us/azure/virtual-machines/), you should package them as [Azure VM Images](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/capture-image-resource) using a tool such as Packer.
Although we recommend Docker for all stateless apps (see below), we recommend directly using VM Images and Azure Virtual Machines for all stateful apps, such as any data store (MySQL, MongoDB, Kafka), and app that writes to its local disk (e.g., WordPress, Jenkins).

### Deploy VM Images using Virtual Machine Scale Sets

The best way to deploy a VM Image is typically to run it as a [Virtual Machine Scale Set](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview).
This will allow you to spin up multiple Azure Virtual Machines that run your VM Image, scale the number of Virtual Machines up and down in response to load, and automatically replace failed Virtual Machines.

### Build Docker images

If you want to run your apps as containers, you should package your apps as Docker images and push those images to [Azure's Container Registry (ACR)](https://docs.microsoft.com/en-us/azure/container-registry/).
We recommend Docker for all stateless apps and for local development (along with Docker Compose).

### Deploy Docker images using Azure Kubernetes Service (AKS) or Azure Container Instances (ACI)

You have several options for running Docker containers in Azure. One is to use the [Azure Kubernetes Service (AKS)](https://docs.microsoft.com/en-us/azure/aks/), where you run a cluster of Azure Virtual Machines, and Azure takes care of scheduling containers across them. Another option is [Azure Container Instances (ACI)](https://docs.microsoft.com/en-us/azure/container-instances/), a service where Azure manages and scales the underlying Virtual Machines for you and you just hand it Docker containers to run.

### Deploy serverless apps using Azure Functions and API Management

If you want to build serverless apps, you should package them as deployment packages for [Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/). You can expose your Azure Functions as HTTP endpoints using [Azure API Management](https://docs.microsoft.com/en-us/azure/api-management/).

### Configure CPU, memory, and GC settings

Configure CPU settings (e.g., ensure your app uses all available CPU cores using tools such as Node Cluster), memory settings (e.g., -Xmx, -Xms settings for the JVM), and GC settings (if applicable) for your app. If you're deploying directly on Azure Virtual Machines, these should be configured based on the available CPU and memory on your Virtual Machine (see [VM Sizes](https://docs.microsoft.com/en-us/azure/virtual-machines/sizes)). If you are deploying Docker containers, then tell the scheduler the resources your app needs (e.g., in the AKS Pod Definition), and it will automatically try to find a Virtual Machine that has those resources.

### Configure hard drives

Configure the OS disk on each Azure Virtual Machine with enough space for your app and log files. Note that OS disks are deleted when a Virtual Machine is deallocated, so if you are running stateful apps that need to persist data between redeploys (or between crashes), attach one or more [Managed Disks](https://docs.microsoft.com/en-us/azure/virtual-machines/disks-types).

## Client-side

### Pick a JavaScript framework

If you are building client-side applications in the browser, you may wish to use a JavaScript framework such as React, Angular, or Ember. You'll need to update your build system to build and package the code appropriately (see [continuous integration](#continuous-integration)).

### Pick a compile-to-JS language

JavaScript has a number of problems and limitations, so you may wish to use a compile-to-JS language, such as TypeScript, Scala.js, PureScript, Elm, or ClojureScript. You'll need to update your build system to build and package the code appropriately (see [continuous integration](#continuous-integration)).

### Pick a compile-to-CSS language

CSS has a number of problems and limitations, so you may wish to use a compile-to-CSS language, such as SASS, less, cssnext, or postcss. You'll need to update your build system to build and package the code appropriately (see [continuous integration](#continuous-integration)).

### Optimize your assets

All CSS and JavaScript should be minified and all images should be compressed. You may wish to concatenate your CSS and JavaScript files and sprite images to reduce the number of requests the browser has to make. Make sure to enable gzip compression. Much of this can be done using a build system such as Grunt, Gulp, Broccoli, or webpack.

### Use a static content server

You should serve all your static content (CSS, JS, images, fonts) from a static content server so that your dynamic web framework (e.g., from Rails, Node.js, or Django) can focus solely on processing dynamic requests. The best static content host to use with Azure is [Azure Blob Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/).

### Use a CDN

Use [Azure Content Delivery Network (CDN)](https://docs.microsoft.com/en-us/azure/cdn/) to cache and distribute your content across servers all over the world. This significantly reduces latency for users and is especially effective for static content.

### Configure caching

Think carefully about versioning, caching, and cache-busting for your static content. One option is to put the version number of each release directly in the URL (e.g., /static/v3/foo.js), which is easy to implement, but means 100% of your content is "cache busted" each release. Another option is "asset fingerprinting," where the build system renames each static content file with a hash of that file's contents (e.g., foo.js becomes 908e25f4bf641868d8683022a5b62f54.js), which is more complicated to implement (note: many build systems have built-in support), but ensures that only content that has changed is ever cache busted. [Azure CDN](https://docs.microsoft.com/en-us/azure/cdn/) can be used to cache your static content across servers all over the world.

## Data storage

### Deploy relational databases

Use [Azure's SQL Database service](https://docs.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview) to run SQL Server, or [Azure Database for MySQL and PostgreSQL](https://docs.microsoft.com/en-us/azure/postgresql/) for running MySQL or PostgreSQL. Consider [Azure SQL Managed Instance](https://docs.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview) for a scalable, cloud-native, SQL Server compatible database. Azure SQL Database and Azure Database for MySQL and PostgreSQL support automatic failover, read replicas, and automated backup.

### Deploy NoSQL databases

Use [Azure Cache for Redis](https://docs.microsoft.com/en-us/azure/azure-cache-for-redis/cache-overview) if you want to use Redis for in-memory key-value storage (Redis provides persistence too, but it's typically only recommended for ephemeral data). Use [Azure Table Storage](https://docs.microsoft.com/en-us/azure/storage/tables/table-storage-overview) if you need a managed, eventually consistent, persistent key-value store. Use [Azure Cosmos DB](https://docs.microsoft.com/en-us/azure/cosmos-db/introduction) if you need a managed, scalable document store that is compatible with MongoDB (albeit, with a number of limitations and differences). If you need other NoSQL databases, such as MongoDB, Couchbase, or InfluxDB, you'll need to look to other managed services or you can run them yourself on [Azure Virtual Machines](https://docs.microsoft.com/en-us/azure/virtual-machines/).

### Deploy queues

Use [Azure Queue Storage](https://docs.microsoft.com/en-us/azure/storage/queues/storage-queues-introduction) as a managed, distributed queue.

### Deploy search tools

Use [Azure Cognitive Search](https://docs.microsoft.com/en-us/azure/search/search-what-is-azure-search) for log analysis and full text search.

### Deploy log analysis tools

For log analysis, consider using [Azure Monitor](https://docs.microsoft.com/en-us/azure/azure-monitor/overview) and [Log Analytics](https://docs.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview). Azure Monitor collects, analyzes, and acts on telemetry data from your Azure and on-premises environments. It helps you understand how your applications are performing and proactively identifies issues affecting them and the resources they depend on. Azure Log Analytics is a service within Azure Monitor that collects telemetry and other data from a variety of sources and provides a query language for advanced analytics. It can help you to understand patterns, trends, and potential issues within your complex systems.

### Deploy stream processing tools

Use [Azure Event Hubs](https://docs.microsoft.com/en-us/azure/event-hubs/) or [Azure Stream Analytics](https://docs.microsoft.com/en-us/azure/stream-analytics/) to process streaming data. Note that Event Hubs and Stream Analytics have some significant limitations, so if you need to work around those, you can look to other managed services or you can run Kafka yourself on [Azure HDInsight](https://docs.microsoft.com/en-us/azure/hdinsight/kafka/apache-kafka-introduction) which supports Apache Kafka.

### Deploy a data warehouse

Use [Azure Synapse Analytics](https://docs.microsoft.com/en-us/azure/synapse-analytics/overview-what-is) for data warehousing.

### Deploy big data systems

Use [Azure HDInsight](https://docs.microsoft.com/en-us/azure/hdinsight/hadoop/apache-hadoop-introduction) to run Hadoop, Spark, HBase, and Hive. For Presto, consider using [Azure Data Explorer](https://docs.microsoft.com/en-us/azure/data-explorer/).

### Set up cron jobs

Use [Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/) with Timer Triggers or [Azure Logic Apps](https://docs.microsoft.com/en-us/azure/logic-apps/) to reliably run background jobs on a schedule (cron jobs). Look into Azure Logic Apps or [Azure Durable Functions](https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview) to build reliable, multi-step, distributed workflows.

### Configure disk space

Configure enough disk space on your system for all the data you plan to store. If you are running a data storage system yourself, you'll probably want to store the data on one or more [Azure Managed Disks](https://docs.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview) that can be attached and detached as Virtual Machines are replaced. Note: using Managed Disks with [Virtual Machine Scale Sets (VMSS)](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview) can be tricky, as VMSS can launch a Virtual Machine in any Availability Zone, but a Managed Disk can only be attached from the same Availability Zone.

### Configure backup

Configure backup for all of your data stores. Most Azure-managed data stores, such as [Azure SQL Database](https://docs.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview) and [Azure Cache for Redis](https://docs.microsoft.com/en-us/azure/azure-cache-for-redis/cache-overview), support automated backups. For backing up Virtual Machines and Managed Disks, consider using [Azure Backup service](https://docs.microsoft.com/en-us/azure/backup/backup-overview) on a scheduled basis.

### Configure cross-subscription backup

Copy all of your backups to a separate Azure subscription for extra redundancy. This ensures that if a disaster happens in one Azure subscription—e.g., an attacker gets in or someone accidentally deletes all the backups—you still have a copy of your data available elsewhere.

### Test your backups

If you never test your backups, they probably don't work. Create automated tests that periodically restore from your backups to check they are actually working. [Azure Backup service](https://docs.microsoft.com/en-us/azure/backup/backup-overview) provides features to test your backups without impacting production workloads.

### Set up schema management

For data stores that use a schema, such as [Azure SQL Database](https://docs.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview), define the schema in schema migration files, check those files into version control, and apply the migrations as part of the deployment process. See [Flyway](https://flywaydb.org/) and [Liquibase](https://www.liquibase.org/). [Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/user-guide/about-azure-devops) can be used to automate the deployment process.

## Scalability and high availability

### Choose between a Monolith and Microservices

Ignore the hype and stick with a monolithic architecture as long as you possibly can. Microservices have massive costs (operational overhead, performance overhead, more failure modes, loss of transactions/atomicity/consistency, difficulty in making global changes, backwards compatibility requirements), so only use them when your company grows large enough that you can't live without one of the benefits they provide (support for different technologies, support for teams working more independently from each other). If you decide to go with microservices, consider using [Azure Service Fabric](https://docs.microsoft.com/en-us/azure/service-fabric/) or [Azure Kubernetes Service (AKS)](https://docs.microsoft.com/en-us/azure/aks/) for orchestrating your microservices. See [Microservice trade-offs](https://martinfowler.com/articles/microservice-trade-offs.html) for more info.

### Configure service discovery

If you do go with microservices, one of the problems you'll need to solve is how services can discover the IPs and ports of other services they depend on. Some of the solutions you can use include [Azure Load Balancer](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview), [Azure Service Fabric](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-overview) for service discovery, and Consul. If you're using Kubernetes, [Azure Kubernetes Service (AKS)](https://docs.microsoft.com/en-us/azure/aks/) provides its own service discovery mechanism.

### Use multiple Instances

Always run more than one copy (i.e., more than one EC2 Instance or Docker container) of each stateless application. This allows you to tolerate the app crashing, allows you to scale the number of copies up and down in response to load, and makes it possible to do zero-downtime deployments.

### Use multiple Availability Zones

Configure your [Azure Scale Sets](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview) and [Load Balancers](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview) to make use of multiple Availability Zones (AZs) (3 is recommended) in your Azure region so you can tolerate the failure of an entire AZ. Azure Availability Zones are physically separate locations within an Azure region that are tolerant to local failures within a zone.

### Set up load balancing

Distribute load across your apps and Availability Zones using Azure's managed [Load Balancer](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview), which is designed for high availability and scalability. Use the Azure Load Balancer for all network traffic. For HTTP/HTTPS traffic specifically, consider using [Azure Application Gateway](https://docs.microsoft.com/en-us/azure/application-gateway/overview), which is a dedicated HTTP/HTTPS load balancer.

### Use Auto Scaling

Use auto scaling to automatically scale the number of resources you're using up to handle higher load and down to save money when load is lower.

### Configure Auto Recovery

Configure a process supervisor such as systemd or supervisord to automatically restart failed processes. Configure your [Azure Virtual Machine Scale Sets](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview) to use a Load Balancer for health checks and to automatically replace failed VM instances. If you're using [Azure Kubernetes Service (AKS)](https://docs.microsoft.com/en-us/azure/aks/) or [Azure Service Fabric](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-overview), they provide built-in health checks to monitor the health of your containers and automatically restart failed ones.

### Configure graceful degradation

Handle failures in your dependencies (e.g., a service not responding) by using graceful degradation patterns, such as retries (with exponential backoff and jitter), circuit breaking, timeouts, deadlines, and rate limiting.

### Perform load tests and use chaos engineering

Run load tests against your infrastructure to figure out when it falls over and what the bottlenecks are. Use chaos engineering to continuously test the resilience of your infrastructure. Azure provides tools like [Azure Load Testing](https://docs.microsoft.com/en-us/azure/architecture/framework/scalability/load-testing) and [Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/migrate/chaos-engineering?view=azure-devops) for chaos engineering to help with these tasks. For chaos engineering, you can also consider open-source tools like [Chaos Toolkit](https://chaostoolkit.org/), which is cloud-agnostic and can be used with Azure.

## Continuous integration

### Pick a Version Control System

Check all code into a Version Control System (VCS). The most popular choice these days is Git. You can use GitHub, GitLab, or BitBucket to host your Git repo. For us that's GitHub!

### Do code reviews

Set up a code review process in your team to ensure all commits are reviewed. Pull requests are an easy way to do this. See [contribution guidelines](./contribution-guidelines.md).

### Configure a build system

Set up a build system for your project, such as Gradle (for Java), Rake (for Ruby), or Yarn (for Node.js). The build system is responsible for compiling your app, as well as many other tasks described below.

### Use dependency management

Your build systems should allow you to explicitly define all the of the dependencies for your apps. Each dependency should be versioned, and ideally, the versions of all dependencies, including transitive dependencies, are captured in a lock file (e.g., read about Yarn's lock file and Go's dep lock file.

### Configure static analysis

Configure your build system so it can run static analysis tools on your code, such as linters and code coverage.

### Set up automatic code formatting

Configure your build system to automatically format the code according to a well-defined style (e.g., with Go, you can run go fmt; with Terraform, you can run terraform fmt). This way, all your code has a consistent style, and your team doesn't have to spend any time arguing about tabs vs spaces or curly brace placement.

### Set up automated tests

Configure your build system so it can run automated tests on your code, with tools such as JUnit (for Java), RSpec (for Ruby), or Mocha (for Node.js).

### Publish versioned artifacts

Configure your build system so it can package your app into a deployable "artifact," such as a VM image or Docker image. Each artifact should be immutable and have a unique version number that makes it easy to figure out where it came from (e.g., tag Docker images with the Git commit ID). Push the artifact to an artifact repository (e.g., [Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/) for Docker images) from which it can be deployed.

### Set up a build server

Set up a server to automatically run builds, static analysis, automated tests, etc. after every commit. You can use a hosted system such as [Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines) or [GitHub Actions](https://docs.github.com/en/actions), which integrate well with Azure services. Alternatively, you can run your own build server with a tool such as Jenkins.

## Continuous delivery

### Create deployment environments

Define separate "environments" such as dev, stage, and prod. Each environment can either be a separate Azure subscription (recommended for larger teams and security-sensitive and compliance use cases) or a separate Virtual Network (VNet) within a single Azure subscription (recommended only for smaller teams).

### Set up per-environment configuration

Your apps may need different configuration settings in each environment: e.g., different memory settings, different features on or off. Define these in config files that get checked into version control (e.g., dev-config.yml, stage-config.yml, prod-config.yml) and packaged with your app artifact (i.e., packaged directly into the Docker image for your app), and have your app boot up code pick the proper config file for the current environment during boot. In Azure, you can also use [Azure App Configuration](https://docs.microsoft.com/en-us/azure/azure-app-configuration/) or [Azure Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/) for managing application settings and secrets respectively.

### Define your infrastructure as code

Do not deploy anything by hand, by using the Azure portal, or the Azure CLI. Instead, define all of your infrastructure as code using tools such as Terraform, Packer, and Docker. Azure also provides its own native infrastructure as code solution, [Azure Resource Manager (ARM) templates](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/overview), for defining and deploying resources.

### Test your infrastructure code

If all of your infrastructure is defined as code, you can create automated tests for it. The goal is to verify your infrastructure works as expected after every single commit, long before those infrastructure changes affect prod. You can use testing frameworks like [Terratest](https://terratest.gruntwork.io/) for Terraform or [Pester](https://pester.dev/) for PowerShell used in ARM templates. For more complex testing scenarios, consider using Azure's native testing service, [Azure Test Plans](https://docs.microsoft.com/en-us/azure/devops/test/overview).

### Set up immutable infrastructure

Don't update Azure Virtual Machines or Docker containers in place. Instead, launch completely new Azure Virtual Machines and new Docker containers and, once those are up and healthy, remove the old Virtual Machines and Docker images. Since we never "modify" anything, but simply replace, this is known as [immutable infrastructure](https://www.oreilly.com/radar/an-introduction-to-immutable-infrastructure/), and it makes it easier to reason about what's deployed and to manage that infrastructure.

### Promote artifacts

Deploy immutable artifacts to one environment at a time, and promote it to the next environment after testing. For example, you might deploy v0.3.2 to dev, and test it there. If it works well, you promote the exact same artifact, v0.3.2, to stage, and test it there. If all goes well, you finally promote v0.3.2 to prod. Since it's the exact same code in every environment, there's a good chance that if it works in one environment, it'll also work in the others. In Azure, you can use [Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/kubernetes/deploy?view=azure-devops) or [GitHub Actions](https://docs.github.com/en/actions) to automate the promotion process across environments.

### Roll back in case of failure

If you use immutable, versioned artifacts as your unit of deployment, then any time something goes wrong, you have the option to roll back to a known-good state by deploying a previous version. If your infrastructure is defined as code using tools like Terraform or Azure Resource Manager (ARM) templates, you can also see what changed between versions by looking at the diffs in version control. Azure also provides features like [Azure Backup](https://docs.microsoft.com/en-us/azure/backup/) and [Azure Site Recovery](https://docs.microsoft.com/en-us/azure/site-recovery/) for more comprehensive disaster recovery strategies.

### Automate your deployments

One of the advantages of defining your entire infrastructure as code using tools like Terraform, Azure Resource Manager (ARM) templates, or Bicep is that you can fully automate the deployment process, making deployments faster, more reliable, and less stressful. Azure provides several services for this purpose, such as [Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines) and [GitHub Actions](https://docs.github.com/en/actions) that integrate well with Azure services for continuous integration and continuous deployment (CI/CD).

### Do zero-downtime deployments

There are several strategies you can use for Zero-downtime deployments in Azure, such as [blue-green deployment](https://martinfowler.com/bliki/BlueGreenDeployment.html) (works best for stateless apps) or [rolling deployment](https://hintcafe.net/post/56948449558/rolling-deployment-with-no-downtime) (works best for stateful apps). Azure provides built-in support for these strategies with services like [Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/deploy-staging-slots) for blue-green deployments and [Azure Service Fabric](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-deploy-remove-applications) or [Azure Kubernetes Service](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough-portal) for rolling deployments.

### Use canary deployments

Instead of deploying the new version of your code to all servers, and risking a bug affecting all users at once, you limit the possible damage by first deploying the new code to a single "canary" server. You then compare the canary to a "control" server running the old code and make sure there are no unexpected errors, performance issues, or other problems. If the canary looks healthy, roll out the new version of your code to the rest of the servers. If not, roll back the canary. Azure provides built-in support for canary deployments with services like [Azure App Service Deployment Slots](https://docs.microsoft.com/en-us/azure/app-service/deploy-staging-slots) and [Azure Kubernetes Service](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough-portal) with Kubernetes' native rollout controls.

### Use feature toggles

Wrap all new functionality in an if-statement that only evaluates to true if the feature toggle is enabled. By default, all feature toggles are disabled, so you can safely check in and even deploy code that isn't completely finished (as long as it compiles!), and it won't affect any user. When the feature is done, you can use a UI to gradually enable the feature toggle for specific users: e.g., initially just for your company's employees, then for 1% of all users, then 10% of all users, and so on. At any stage, if anything goes wrong, you can turn the feature toggle off again. Feature toggles allow you to separate deployment of new code from the release of new features in that code. They also allow you to do bucket testing. Azure provides a feature management service in [Azure App Configuration](https://docs.microsoft.com/en-us/azure/azure-app-configuration/overview) that can be used for this purpose. For more advanced feature management, consider using third-party services like LaunchDarkly, Split, or Optimizely.

## Networking

### Set up Virtual Networks

Don't use the default network, as everything in it is publicly accessible by default. Instead, create one or more custom [Virtual Networks (VNet)](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview), each with their own IP address range (see [VNet and subnet sizing](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-faq)), and deploy all of your apps into those VNets.

### Set up subnets

Create three "tiers" of subnets in each Virtual Network (VNet): public, private-app, private-persistence. The public subnets are directly accessible from the public Internet and should only be used for a small number of highly locked down, user-facing services, such as load balancers and [Azure Bastion](https://docs.microsoft.com/en-us/azure/bastion/bastion-overview). The private-apps subnets are only accessible from within the VNet from the public subnets and should be used to run your apps ([Virtual Machine Scale Sets](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview), [Azure Kubernetes Service](https://docs.microsoft.com/en-us/azure/aks/intro-kubernetes), etc.). The private-persistence subnets are also only accessible from within the VNet from the private-app subnets (but NOT the public subnets) and should be used to run all your data stores ([Azure SQL Database](https://docs.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview), [Azure Cache for Redis](https://docs.microsoft.com/en-us/azure/azure-cache-for-redis/cache-overview), etc.).

### Configure Network Security Groups

Create [Network Security Groups (NSGs)](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview) to control what traffic can go between different subnets. We recommend allowing the public subnets to receive traffic from anywhere, the private-app subnets to only receive traffic from the public subnets, and the private-persistence subnets to only receive traffic from the private-app subnets.

Every Azure resource (e.g., [Virtual Machines](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/overview), [Load Balancers](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview), [Azure SQL Databases](https://docs.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview), etc.) can be associated with a Network Security Group (NSG) that acts as a firewall, controlling what traffic is allowed in and out of that resource. By default, no inbound traffic is allowed and all outbound traffic is allowed. Follow the Principle of Least Privilege and open up the absolute minimum number of ports you can for each resource. When opening up a port, you can also specify either the CIDR block (IP address range) or the name of another NSG that is allowed to access that port. Reduce these to solely trusted servers where possible. For example, Virtual Machines should only allow SSH access (port 22) from the NSG of a single, locked-down, trusted server (the Azure Bastion).

### Configure Static IPs

By default, all Azure resources (e.g., [Virtual Machines](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/overview), [Load Balancers](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview), [Azure SQL Databases](https://docs.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview), etc.) have dynamic IP addresses that could change over time (e.g., after a redeploy). When possible, use Service Discovery to find the IPs of services you depend on. If that's not possible, you can create static IP addresses that can be attached and detached from resources using [Public IP addresses](https://docs.microsoft.com/en-us/azure/virtual-network/public-ip-addresses) for public IPs or [Private IP addresses](https://docs.microsoft.com/en-us/azure/virtual-network/private-ip-address) for private IPs.

### Configure DNS using Azure DNS

Manage DNS entries using [Azure DNS](https://docs.microsoft.com/en-us/azure/dns/dns-overview). You can buy public domain names using third-party domain registrars and manage them in Azure DNS, or create custom private domain names, accessible only from within your Virtual Network, using [Azure Private DNS Zones](https://docs.microsoft.com/en-us/azure/dns/private-dns-overview).

## Security

### Configure encryption in transit

Encrypt all network connections using TLS. Many [Azure services](https://docs.microsoft.com/en-us/azure/?product=featured) support TLS connections by default (e.g., [Azure SQL Database](https://docs.microsoft.com/en-us/azure/azure-sql/database/security-overview)) or if you enable them (e.g., [Azure Cache for Redis](https://docs.microsoft.com/en-us/azure/azure-cache-for-redis/cache-overview)). You can get free, auto-renewing TLS certificates for your public domain names from [Azure App Service Managed Certificates](https://docs.microsoft.com/en-us/azure/app-service/configure-ssl-certificate#create-a-free-certificate-preview). For private domain names within your [Virtual Network](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview), you can use [Azure Private Link](https://docs.microsoft.com/en-us/azure/private-link/private-link-overview) service along with your own private certificates.

### Configure encryption at rest

Encrypt the OS disk of each Virtual Machine by using [Azure Disk Encryption](https://docs.microsoft.com/en-us/azure/security/fundamentals/azure-disk-encryption). Enable encryption for each managed disk too. Many Azure services optionally support disk encryption: e.g., see [Azure SQL Database Transparent Data Encryption (TDE)](https://docs.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-tde-overview) and [Azure Cache for Redis disk persistence](https://docs.microsoft.com/en-us/azure/azure-cache-for-redis/cache-how-to-persistence).

### Set up SSH access

Do NOT share SSH keys with your team! Otherwise, everyone will be using the same username and key for server access (so there's no audit trail), the key may easily be compromised, and if it is, or someone leaves the company, you'll have to redeploy ALL your Virtual Machines to change the SSH key. Instead, configure your Virtual Machines so that each developer can use their own username and SSH key, and if that developer leaves the company, the key can be invalidated immediately (see [Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/) for solutions).

### Deploy a Bastion Host

Just about all your Virtual Machines should be in private subnets and NOT accessible directly from the public Internet. Only a single, locked-down Virtual Machine, known as the [Azure Bastion](https://docs.microsoft.com/en-us/azure/bastion/bastion-overview), should run in the public subnets. You must first connect to the Azure Bastion, which gets you "in" to the network, and then you can use it as a "jump host" to connect to the other Virtual Machines. The only other Virtual Machines you might want to run in public subnets are those that must be accessible directly from the public Internet, such as load balancers (though in most cases, we recommend using [Azure-managed Load Balancers](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview)).

### Deploy a VPN Gateway

We typically recommend running a VPN Gateway as the entry point to your network (as the Bastion Host). [Azure VPN Gateway](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways) is a popular option for setting up a VPN server.

### Set up a secrets management solution

NEVER store secrets in plaintext. Developers should store their secrets in a secure secrets manager, such as pass, 1Password, or LastPass. Applications should store all their secrets (such as DB passwords and API keys) either in files encrypted with [Azure Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/general/overview) or in a secret store such as [Azure Key Vault Secrets](https://docs.microsoft.com/en-us/azure/key-vault/secrets/about-secrets).

### Use server hardening practices

Every server should be hardened to protect against attackers. This may include: running [Azure Security Center's Just-In-Time VM Access](https://docs.microsoft.com/en-us/azure/security-center/just-in-time-explained), [Azure DDoS Protection](https://docs.microsoft.com/en-us/azure/ddos-protection/ddos-protection-overview) to protect against malicious access, [Azure Update Management](https://docs.microsoft.com/en-us/azure/automation/update-management/update-mgmt-overview) to automatically install critical security patches, [Azure Firewall](https://docs.microsoft.com/en-us/azure/firewall/overview), [Azure Security Center's Antimalware for Virtual Machines](https://docs.microsoft.com/en-us/azure/security/fundamentals/antimalware), and [Azure File Integrity Monitoring](https://docs.microsoft.com/en-us/azure/security-center/file-integrity-monitoring). See also [Azure Security Best Practices](https://docs.microsoft.com/en-us/azure/security/fundamentals/best-practices-and-patterns) and [Azure Virtual Machine Security Guide](https://docs.microsoft.com/en-us/azure/security/fundamentals/vm-best-practices).

### Go through the OWASP Top 10

Browse through the Top 10 Application Security Risks list from the [Open Web Application Security Project (OWASP)](https://owasp.org/) and check your app for vulnerabilities such as injection attacks, CSRF, and XSS. Use [Azure Security Center's Web Application Firewall (WAF) on Azure Application Gateway](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview) to help protect your applications from these vulnerabilities.

### Go through a security audit

Have a third party security service perform a security audit and do penetration testing on your services. Fix any issues they uncover.

### Sign up for security advisories

Join the security advisory mailing lists for any software you use and monitor those lists for announcements of critical security vulnerabilities.

### Create Azure Active Directory Users

Create an [Azure Active Directory User](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/add-users-azure-active-directory) for each developer, then you will have a portal login for accessing Azure from a web browser and a set of API keys for accessing Azure from the CLI.

### Create Azure Roles

Give your Azure resources (e.g., [Virtual Machines](https://docs.microsoft.com/en-us/azure/virtual-machines/), [Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/)) access to other resources by assigning [Azure Roles](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview). All Azure SDK and CLI tools automatically know how to use Azure Roles, so you should never have to copy Azure access keys to a server.

### Create cross-subscription Azure Roles

If you are using multiple Azure subscriptions (e.g., one for dev and one for prod), you should define all of the [Azure Active Directory Users](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/add-users-azure-active-directory) in one subscription, and use [Azure Roles](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) to provide access to the other Azure subscriptions. This way, developers have only one set of credentials to manage, and you can have very fine-grained permissions control over what users can do in any given subscription.

### Create a password policy and enforce MFA

Set a password policy that requires a long password for all [Azure Active Directory users](https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-sspr-policy) and require every user to enable Multi-Factor Authentication (MFA) using [Azure AD Multi-Factor Authentication](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa).

### Record audit Logs

Enable [Azure Activity Log](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/activity-log) to maintain an audit log of all changes happening in your Azure account.

## Monitoring

### Track availability metrics

The most basic set of metrics: can a user access your product or not? Useful tools: [Azure Monitor](https://docs.microsoft.com/en-us/azure/azure-monitor/overview) and [Azure Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview).

### Track business metrics

Metrics around what users are doing with your product, such as what pages they are viewing, what items they are buying, and so on. Useful tools: [Azure Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview), Google Analytics, and Mixpanel.

### Track application metrics

Metrics around what your application is doing, such as QPS, latency, and throughput. Useful tools: [Azure Monitor](https://docs.microsoft.com/en-us/azure/azure-monitor/overview), [Azure Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview), and New Relic.

### Track server metrics

Metrics around what your hardware is doing, such as CPU, memory, and disk usage. Useful tools: [Azure Monitor](https://docs.microsoft.com/en-us/azure/azure-monitor/overview), [Azure Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview), New Relic, Nagios, Icinga, and collectd.

### Configure services for observability

Record events and stream data from all services. Slice and dice it using tools such as [Azure Event Hubs](https://docs.microsoft.com/en-us/azure/event-hubs/) and [Azure Stream Analytics](https://docs.microsoft.com/en-us/azure/stream-analytics/), [Azure Monitor](https://docs.microsoft.com/en-us/azure/azure-monitor/overview), and [Azure Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview).

### Store logs

To prevent log files from taking up too much disk space, configure log rotation on every server using a tool such as logrotate. To be able to view and search all log data from a central location (i.e., a web UI), set up log aggregation using tools such as [Azure Monitor Logs](https://docs.microsoft.com/en-us/azure/azure-monitor/logs/overview), Filebeat, Logstash, Loggly, and Papertrail.

### Set up alerts

Configure alerts when critical metrics cross pre-defined thresholds, such as CPU usage getting too high or available disk space getting too low. Most of the metrics and log tools listed earlier in this section support alerting. Set up an on-call rotation using tools such as [Azure Monitor Alerts](https://docs.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview) and [Azure Logic Apps](https://docs.microsoft.com/en-us/azure/logic-apps/) for incident management.

## Cost optimization

### Pick proper Azure Virtual Machine sizes and types

[Azure](https://azure.microsoft.com/en-us/) offers a number of different [Virtual Machine sizes](https://docs.microsoft.com/en-us/azure/virtual-machines/sizes), each optimized for different purposes: compute, memory, storage, GPU, etc. Use [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/) to slice and dice the different VM sizes across a variety of parameters. Try out a variety of VM sizes by load testing your app on each type and picking the best balance of performance and cost. In general, running a larger number of smaller VMs ("horizontal scaling") is going to be cheaper, more performant, and more reliable than a smaller number of larger VMs ("vertical scaling"). See also Azure's documentation on how to [Choose the right virtual machine size](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes).

### Use Azure Spot Virtual Machines for background jobs

[Azure Spot Virtual Machines](https://docs.microsoft.com/en-us/azure/virtual-machines/spot-vms) allow you to use Azure's unused capacity at a significant cost savings. Note that if Azure needs to reclaim that capacity, it may deallocate the VM at any time. This makes Spot VMs a great way to save money on any workload that is non-urgent (e.g., all background jobs, machine learning, image processing) and pre-production environments. Just be sure to handle the potential for interruptions in your application design.

### Use Azure Reserved Virtual Machine Instances for dedicated work

[Azure Reserved Virtual Machine Instances](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/prepay-reserved-vm-instances) allow you to reserve capacity ahead of time in exchange for a significant discount (up to 72%) over pay-as-you-go pricing. This makes Reserved Instances a great way to save money when you know for sure that you are going to be using a certain number of VMs consistently for a long time period. For example, if you knew you were going to run a 3-node ZooKeeper cluster all year long, you could reserve three `D2s v3` VMs for one year, at a discount of 72%. Reserved Instances are a billing optimization, so no code changes are required: just reserve the VM size, and next time you use it, Azure will charge you less for it.

### Shut down Virtual Machines and Azure SQL Databases when not using them

You can shut down (but not delete!) [Virtual Machines](https://docs.microsoft.com/en-us/azure/virtual-machines/) and [Azure SQL Databases](https://docs.microsoft.com/en-us/azure/azure-sql/database/) when you're not using them, such as in your pre-prod environments at night and on weekends. You could even create an [Azure Function](https://docs.microsoft.com/en-us/azure/azure-functions/) that does this on a regular schedule. For more info, see [Azure Automation to schedule VM start/stop](https://docs.microsoft.com/en-us/azure/automation/automation-solution-vm-management).

### Use Auto Scaling for cost control

Use Azure's [Virtual Machine Scale Sets](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview) to increase the number of VMs when load is high and then to decrease it again—and thereby save money—when load is low.

### Use Docker when possible

If you deploy everything as a VM directly on your [Azure Virtual Machines](https://docs.microsoft.com/en-us/azure/virtual-machines/), then you will typically run exactly one type of app per VM. If you use a Docker orchestration tool (e.g., [Azure Kubernetes Service](https://docs.microsoft.com/en-us/azure/aks/)), you can give it a cluster of VMs to manage, and it will deploy Docker containers across the cluster as efficiently as possible, potentially running multiple apps on the same VMs when resources are available.

### Use Azure Functions when possible

For all short background jobs, cron jobs, ETL jobs, event processing jobs, and other glue code, use [Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/). You not only have no servers to manage, but Azure Functions pricing is incredibly cost-effective, with the first 1 million requests and 400,000 GB-seconds per month being completely free! After that, it's just $0.0000002 per request and $0.000016 for every GB-second.

### Clean up old data with Azure Blob Storage Lifecycle Management

If you have a lot of data in [Azure Blob Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/), make sure to take advantage of [Azure Blob Storage Lifecycle Management](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-lifecycle-management-concepts?tabs=azure-portal) to save money. You can configure the Blob Storage to move files older than a certain age either to cheaper storage tiers or to delete those files entirely.

### Clean up unused resources

Use tools such as [Azure Resource Graph](https://docs.microsoft.com/en-us/azure/governance/resource-graph/overview) and [Azure Advisor](https://docs.microsoft.com/en-us/azure/advisor/advisor-overview) to clean up unused Azure resources, such as old Virtual Machines or Load Balancers that no one is using any more. You can run these tools on a regular schedule by using [Azure Automation](https://docs.microsoft.com/en-us/azure/automation/automation-intro) or scheduled Azure Functions.

### Learn to analyze your Azure bill

Learn to use tools such as [Cost Management and Billing](https://docs.microsoft.com/en-us/azure/cost-management-billing/), [Azure Advisor](https://docs.microsoft.com/en-us/azure/advisor/advisor-overview), and [Azure Cost Management Power BI App](https://docs.microsoft.com/en-us/azure/cost-management-billing/costs/analyze-cost-data-azure-cost-management-power-bi-template-app) to understand where you're spending money. Make sure you understand what each category means (e.g., the delightfully vague "Other" often means Disk Storage, Managed Disks, and Load Balancers). If you find something you can't explain, reach out to [Azure Support](https://azure.microsoft.com/en-us/support/options/), and they will help you track it down. Using multiple Azure subscriptions with [Azure Management Groups](https://docs.microsoft.com/en-us/azure/governance/management-groups/) can make it easier to isolate certain types of costs from others (e.g., break down costs by environment or team).

### Create billing alerts

Create cost alerts in [Azure Cost Management](https://docs.microsoft.com/en-us/azure/cost-management-billing/manage/create-budget) to notify you when your Azure bill crosses important thresholds. Make sure to have several levels of alerts: e.g., at the very least, one when the cost is a little high, one when it's really high, and one when it is approaching bankruptcy levels.
