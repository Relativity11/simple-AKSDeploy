variable "subscription_id" {
  description = "The subscription ID to be used for this deployment."
  type        = string
}

variable "location" {
  description = "The location/region where the resources will be created."
  type        = string
  default     = "East US"
}

variable "resource_group_name" {
  description = "The name of the Resource Group."
  type        = string
  default     = "aks-resource-group"
}

variable "vnet_name" {
  description = "The name of the Virtual Network."
  type        = string
  default     = "aks-vnet"
}

variable "subnet_name" {
  description = "The name of the Subnet."
  type        = string
  default     = "aks-subnet"
}

variable "aks_cluster_name" {
  description = "The name of the AKS cluster."
  type        = string
  default     = "aks-cluster"
}

variable "node_vm_size" {
  description = "The size of the Virtual Machines in the AKS cluster."
  type        = string
  default     = "Standard_B4ms"
}

variable "node_count" {
  description = "The number of nodes in the default node pool."
  type        = number
  default     = 1
}