# simple-AKSDeploy
A simple testing Azure AKS

In order to use this script to create a basic AKS installation:
1. Create a terraform.tfvars file
Include:
subscription_id       = "<subscription-id>"
location              = "East US"
resource_group_name   = "aks-resource-group"
vnet_name             = "aks-vnet"
subnet_name           = "aks-subnet"
aks_cluster_name      = "aks-cluster"
node_vm_size          = "Standard_D4ps_v5"
node_count            = 1

2.Run terraform plan and apply.