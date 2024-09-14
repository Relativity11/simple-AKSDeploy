resource "null_resource" "run_cost_estimation" {
  provisioner "local-exec" {
    command = "python3 estimate_cost.py"
  }

  # This will trigger the provisioner after terraform apply
  depends_on = [azurerm_kubernetes_cluster.aks]
}