import pulumi
import pulumi_digitalocean as do

config = pulumi.Config()

## Define a digital ocean cluster
#cluster = do.KubernetesCluster(
#    "brice-live-demo-cluster",
#    node_pool={
#        "name": "worker-pool",
#        "node_count": 2,
#        "size": "s-1vcpu-2gb",
#    },
#    region="lon1",
#    version="1.19.3-do.2"
#)
#
## Expose the kubeconfig
#pulumi.export("pulumi-kubeconfig", cluster.kube_configs[0]["rawConfig"])
