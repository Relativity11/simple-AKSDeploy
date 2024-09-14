import requests
import json

# Read Terraform outputs
with open('terraform.tfstate') as f:
    tfstate = json.load(f)

# Extract relevant values from Terraform outputs
vm_size = tfstate['outputs']['aks_node_vm_size']['value']
node_count = tfstate['outputs']['aks_node_count']['value']
location = tfstate['outputs']['location']['value']
# Assumes Commercial Cloud
# Azure region pricing API sometimes uses different names, map to region names if needed
region_map = {
    'East US': 'eastus',
    # Add other region mappings if necessary
}

# API endpoint for Azure Pricing
azure_pricing_url = "https://prices.azure.com/api/retail/prices"

# Query the API for the VM size
def get_vm_price(vm_size, location):
    params = {
        'currencyCode': 'USD',
        'armRegionName': region_map.get(location, location),
        'serviceFamily': 'Compute',
        'skuName': vm_size
    }
    response = requests.get(azure_pricing_url, params=params)
    response.raise_for_status()
    prices = response.json()
    if prices['Items']:
        # Return the price per hour
        return float(prices['Items'][0]['retailPrice'])
    return None

# Get the price per hour for the VM size
vm_price_per_hour = get_vm_price(vm_size, location)
if vm_price_per_hour is None:
    print(f"Could not find price for VM size: {vm_size}")
else:
    # Estimate the monthly cost
    hours_per_month = 730  # Average number of hours in a month
    total_cost = vm_price_per_hour * node_count * hours_per_month
    cost_estimate = {
        'vm_size': vm_size,
        'node_count': node_count,
        'location': location,
        'cost_per_hour': vm_price_per_hour,
        'monthly_cost_estimate': total_cost
    }

    # Write the cost estimate to a file
    with open('cost_estimate.json', 'w') as f:
        json.dump(cost_estimate, f, indent=4)

    print("Cost estimate written to cost_estimate.json")