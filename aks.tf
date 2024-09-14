resource "azurerm_kubernetes_cluster" "aks" {
  name                = var.aks_cluster_name
  location            = azurerm_resource_group.aks_rg.location
  resource_group_name = azurerm_resource_group.aks_rg.name
  dns_prefix          = "akscluster"

  default_node_pool {
    name       = "default"
    node_count = var.node_count
    vm_size    = var.node_vm_size
  }

  network_profile {
    network_plugin = "azure"
    load_balancer_sku = "basic"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    environment = "testing"
  }
}