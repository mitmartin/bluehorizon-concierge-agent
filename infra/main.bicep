targetScope = 'subscription'

@minLength(1)
param environmentName string

@minLength(1)
param location string = deployment().location

param resourceGroupName string = ''
param serviceName string = 'concierge'

var tags = {
  'azd-env-name': environmentName
  application: 'bluehorizon-concierge-agent'
}
var resolvedResourceGroupName = empty(resourceGroupName) ? '${environmentName}-rg' : resourceGroupName

resource rg 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: resolvedResourceGroupName
  location: location
  tags: tags
}

module app 'resources.bicep' = {
  name: 'bluehorizon-concierge-resources'
  scope: rg
  params: {
    environmentName: environmentName
    location: location
    serviceName: serviceName
    tags: tags
  }
}

output AZURE_CONTAINER_REGISTRY_ENDPOINT string = app.outputs.containerRegistryEndpoint
output AZURE_CONTAINER_APP_NAME string = app.outputs.containerAppName
output SERVICE_CONCIERGE_URI string = app.outputs.containerAppUri
