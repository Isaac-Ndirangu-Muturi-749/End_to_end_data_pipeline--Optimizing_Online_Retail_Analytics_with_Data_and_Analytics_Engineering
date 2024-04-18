# mage-ai-terraform-templates
Terraform templates for deploying mage-ai to GCP(Google Cloud Platform)

## Infrastructure as Code (IaC)

#### Terraform
[Terraform](https://www.terraform.io/) is an open-source infrastructure as code software tool created by HashiCorp. It allows users to define and provision data center infrastructure using a high-level configuration language known as HashiCorp Configuration Language (HCL).

#### Project Structure
```
├── mage-ai-Terraform-Infrastructure-As-Code
│   ├── README.md
│   ├── db.tf
│   ├── direct-disk-412820-2333e42872f1.json
│   ├── fs.tf
│   ├── load_balancer.tf
│   ├── main.tf
│   ├── terraform.tfstate
│   ├── terraform.tfstate.backup
│   └── variables.tf
```

#### Files and Directories
- `README.md`: This file contains documentation for the infrastructure setup, including how to deploy and manage the infrastructure using Terraform.
- `db.tf`: Defines resources related to the database setup, including instance type, storage, and access permissions.
- `fs.tf`: Defines resources related to file storage, such as buckets and access controls.
- `load_balancer.tf`: Defines resources related to load balancers and networking configurations.
- `main.tf`: The main Terraform configuration file that orchestrates the provisioning of various resources.
- `terraform.tfstate` and `terraform.tfstate.backup`: These files contain the state of the infrastructure managed by Terraform. They should not be modified manually.
- `variables.tf`: Defines input variables used in the Terraform configuration files.

#### Usage
1. **Installation**: Ensure Terraform is installed on your local machine.
2. **Configuration**: Modify the `.tf` files to match your desired infrastructure configuration.
3. **Initialization**: Run `terraform init` to initialize the working directory containing Terraform configuration files.
4. **Planning**: Run `terraform plan` to create an execution plan. This step is optional but recommended to verify changes before applying them.
5. **Execution**: Run `terraform apply` to apply the changes required to reach the desired state of the configuration.
6. **Verification**: After applying changes, verify that the infrastructure has been provisioned correctly.
7. **Cleanup**: When done, run `terraform destroy` to destroy all the resources defined in the Terraform configuration.
