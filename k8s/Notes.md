# Container Orchestration

Automates deployment, management, scaling, and networking of containers

## Challenges without orchestration:
- Manual scaling required
- Lack of fault tolerance
- Manual container management

## Solutions provided:
- Automatic scaling based on traffic
- Failed containers automatically restarted
- Provisioning and deployment automation
- Resource allocation and load balancing
- Container health monitoring

**Tools:** Kubernetes, Docker Swarm, Amazon ECS
# Kubernetes Introduction

Open-source container orchestration engine developed by Google  
Maintained by Cloud Native Computing Foundation

## Architecture:
- **Control Plane:** Manages cluster
- **Nodes:** Worker machines running containerized applications

## Features:
- Pod Auto-Scaling
- Service discovery and load balancing
- Self-Healing of Containers
- Secret management
- Automated rollouts and rollbacks
# Installation Options

- **Managed Kubernetes Service:** AWS EKS, GCP, Digital Ocean
- **Development Tools:** Minikube, K3d, Kubeadm
- **Setup from Scratch:** Install/configure each component individually
# Connectivity Options

- **API:** Direct requests using curl
- **CLI:** kubectl command-line tool
- **GUI:** Web-based Dashboard
# kubectl

Kubernetes command-line tool

## Requirements:
- DNS/IP address of Control Plane
- Authentication credentials

**Default kubeconfig path:** `~/.kube/config`  
**Custom config:** Use `--kubeconfig` flag
# Pods

Smallest deployable unit in Kubernetes  
Can contain one or more containers  
Containers share network namespace and storage  
Always runs on a Node

**Command:** `kubectl run nginx --image=nginx`
# Docker vs Kubernetes Commands

| Purpose | Docker | Kubernetes |
|---------|--------|------------|
| Create and run | `docker run nginx` | `kubectl run nginx --image=nginx` |
| List running | `docker ps` | `kubectl get pods` |
| View logs | `docker logs` | `kubectl logs` |
| Get detailed info | `docker inspect` | `kubectl describe pod` |
| Execute shell | `docker exec -it bash` | `kubectl exec -it -- bash` |
| Remove | `docker rm` | `kubectl delete pod` |

# Manifest Files

YAML or JSON files defining desired state

## Benefits:
- Version control
- Multiple resources in single file

## Structure:
- **apiVersion:** API version to use
- **kind:** Resource type
- **metadata:** Resource information
- **spec:** Resource details
# Generating Manifest Files

- `--dry-run=client`: Validates without applying
- `-o yaml`: Outputs YAML format
- **Combined:** Generates manifest without deploying
# Multi-Container Pods

Define multiple containers in `spec.containers`  
`kubectl run` supports single container only  
Use manifest file for multi-container

**Access specific container:** `kubectl exec -it <pod> -c <container-name> -- bash`
# Commands and Arguments

- **command field:** Overrides ENTRYPOINT
- **args field:** Overrides CMD

**Syntax:** `kubectl run nginx --image=nginx --command -- <command> <args>`

- **Array notation:** For short commands
- **Multi-line YAML list:** For long commands
# kubectl explain

Describe fields for API resources  
Alternative to API documentation
# Labels and Selectors

- **Labels:** Key/value pairs attached to objects
- **Selectors:** Filter objects based on labels

**Example:** `env: production`, `env: dev`
# ReplicaSet

Maintains stable set of replica Pods

## Issues:
- No automatic updates when template changes
- No built-in rollback
- Label collision issues
# Deployments

Higher-level abstraction built on ReplicaSets

## Features:
- Rolling updates
- Rollbacks
- Versioning

## Commands:
```bash
kubectl rollout history deployment/my-dep
kubectl rollout undo deployment/my-dep
kubectl rollout restart deployment/my-dep
```
# Multiple Worker Nodes

Distributes workload across nodes  
High availability  
Different hardware specifications allowed

**Command:** `kubectl get nodes`
# Node Selector

Controls pod placement on specific nodes

## Steps:
1. Label nodes: `kubectl label nodes node1 size=large`
2. Use `nodeSelector` in pod spec
# DaemonSet

Ensures all Nodes run a copy of a Pod  
Automatically creates pods on new nodes

## Use cases:
- Anti-virus agents
- Log collection agents
- Monitoring agents
# Node Affinity

More flexible than Node Selector

## Operators:
- **In:** Matches specified values
- **NotIn:** Excludes specified values
- **Exists:** Matches key regardless of value
- **DoesNotExist:** Excludes specified key
- **Gt/Lt:** Greater/less than for numeric values

## Modes:
- `requiredDuringSchedulingIgnoredDuringExecution`: Hard requirement
- `preferredDuringSchedulingIgnoredDuringExecution`: Soft preference
# Requests and Limits

- **Requests:** Minimum resources guaranteed
- **Limits:** Maximum resources allowed

CPU throttled if limit exceeded  
Container killed if memory limit exceeded

## Example:

```yaml
resources:
  requests:
    memory: "128Mi"
    cpu: "500m"
  limits:
    memory: "500Mi"
    cpu: "1"
```
# PriorityClass

Indicates pod importance

## Influences:
- Scheduling order
- Preemption (evicting lower priority pods)

**Command:** `kubectl create priorityclass high-priority --value=1000`
# Multi-Container Pod Patterns

- **Sidecar:** Multiple containers in single pod
- **Ambassador:** Second container proxies requests
- **Adapter:** Transforms output to standardized format
# Init Containers

Run before app containers  
Always run to completion  
Each must complete before next starts  
If fails, kubelet restarts until success
# Services

Provides stable endpoint for accessing Pods  
Acts as gateway distributing traffic

## Problems solved:
- Dynamic pod IPs
- Traffic distribution across replicas
- Stable endpoint for external access
# Service Types

| Type | Features | Use Cases |
|------|----------|-----------|
| ClusterIP | Default, internal only | Internal microservices |
| NodePort | Port 30000-32767 on each node | Development testing |
| LoadBalancer | Cloud provider load balancer | Production external access |
| ExternalName | Maps to external DNS | External service integration |

# Service and Endpoints

**Endpoints:** Contain Pod IPs

- **Manual:** Create service and add endpoints manually
- **Automatic:** Use selectors to auto-add Pod IPs
# Ingress

Entry point routing traffic to services based on rules

## Components:
- **Ingress Controller:** Implements rules (running application)
- **Ingress Resource:** Defines routing rules

**Command:** `kubectl create ingress my-ingress --rule="example.com/=my-service:80"`

**Supported controllers:** nginx, AWS ALB, GCE
# Ingress with TLS

## Steps:
1. Create TLS certificate
2. Store in Kubernetes Secret
3. Reference Secret in Ingress resource
4. Access over HTTPS
# Helm

Package manager for Kubernetes

## Concepts:
- **Chart:** Helm package
- **Repository:** Where charts are stored
- **Release:** Instance of chart running in cluster

## Commands:

```bash
helm search repo nginx
helm repo add stable https://charts.helm.sh/stable
helm install my-release nginx
helm uninstall my-release
helm list
helm template my-release nginx
```

**Skip CRDs:** `--skip-crds` or `--set crds.install=false`
# Namespaces

Isolate groups of resources within cluster

## Default namespaces:
- **default:** Resources with no namespace
- **kube-system:** Kubernetes system objects
- **kube-public:** Publicly accessible data
- **kube-node-lease:** Node heartbeat leases

## Commands:

```bash
kubectl create namespace dev
kubectl get pods -n dev
```
# Service Accounts

## Two categories:
- **User Accounts:** For humans
- **Service Accounts:** For applications

**Default:** Every namespace has default ServiceAccount  
**Token location:** `/var/run/secrets/kubernetes.io/serviceaccount/token`

## Commands:

```bash
kubectl create serviceaccount my-sa
```

Use `serviceAccountName` in pod spec
# Named Port

Associate name with port  
Name must be unique within pod  
Reference by name in service instead of port number
# Metrics Server

Collects CPU and memory from kubelet  
Makes available via Metrics API

## Commands:

```bash
kubectl top pods
kubectl top nodes
```
# Horizontal Pod Autoscaler (HPA)

Automatically adjusts number of pods  
Based on CPU, memory, or custom metrics  
Does not apply to DaemonSets

## Stabilization Window:
- **Scale Up:** 0 seconds (no delay)
- **Scale Down:** 300 seconds (5 minutes)

**Command:** `kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=3`
# Vertical Pod Autoscaler (VPA)

Automatically adjusts CPU and memory requests

## Update Modes:
- **Off:** Recommendations only
- **Initial:** Assigns on creation only
- **Auto:** Applies by evicting and restarting
# Gateway API

Successor to Ingress  
Supports L4 and L7 protocols (TCP, UDP, HTTP, gRPC)

## Components:
- **GatewayClass:** Specifies controller
- **Gateway:** Traffic handling infrastructure
- **HTTPRoute:** Routing behavior
- **Gateway Controller:** Implementation component

## TLS Modes:
- **Passthrough:** TLS decrypted at backend
- **Terminate:** TLS decrypted at Gateway
# Custom Resource Definitions (CRD)

Extend Kubernetes API  
Define custom resource types

## Steps:
1. Create CRD
2. Create custom objects

**Controller:** Tracks resource type, ensures desired state
# Authentication

Verifies user identity  
Kubernetes does not manage user accounts natively

## Methods:
- Client Certificates (X509)
- Static Token File
- Service Account Tokens

## User categories:
- **Normal Users:** For humans
- **Service Accounts:** For apps
# Authorization

Determines what authenticated user can do  
Takes place after authentication

## Modes:
- **AlwaysAllow:** All requests (testing only)
- **AlwaysDeny:** Blocks all (testing only)
- **RBAC:** Role-based (recommended for production)

**Default:** AlwaysAllow if not defined
# RBAC (Role-Based Access Control)

- **Role:** Defines permissions in namespace
- **RoleBinding:** Grants Role to subjects in namespace
- **ClusterRole:** Permissions across all namespaces
- **ClusterRoleBinding:** Grants ClusterRole cluster-wide

## API Groups:
- **"" (empty):** Core API (pods, services, configmaps)
- **apps:** Deployments, daemonsets, replicasets
- **batch:** Jobs, CronJobs
- **networking.k8s.io:** Ingress, Network Policies

## Verbs:
`get`, `list`, `create`, `update`, `delete`, `watch`
# Asymmetric Key Encryption

Uses public and private keys

- **Public key:** Shared with everyone
- **Private key:** Kept secret

Either key encrypts, opposite key decrypts

**Protocols:** PGP, SSH, Bitcoin, TLS, S/MIME
# HTTPS/TLS

**HTTPS:** Extension of HTTP  
Communication encrypted using TLS

Certificate like passport issued by trusted entity  
Browser verifies certificate issuer  
Asymmetric encryption generates temporary symmetric key
# Certificate Based Authentication

X509 client certificates

## Workflow:
1. Generate private key (openssl)
2. Create CSR (openssl)
3. Create K8s CSR object
4. K8s CA approves
5. Get certificate
6. Authenticate with kubectl/curl
# Kubeconfig

Contains cluster, user, authentication info

## Fields:
- **clusters:** Cluster URL and info
- **users:** Authentication info (tokens, certificates)
- **contexts:** Groups cluster, user, namespace

Can have details for multiple clusters
# Volumes

## Challenges:
- Container state not saved on crash
- Multi-container file sharing

## Types:
- **Ephemeral:** Lifetime linked to pod
- **Persistent:** Exists beyond pod lifetime

**Volume types:** configMap, emptyDir, hostPath, local, nfs

## Specification:
- `spec.volumes`: Volumes to provide
- `spec.containers[*].volumeMounts`: Where to mount
# emptyDir Volume

Temporary storage directory  
All containers can read/write  
Deleted when pod removed  
Can use memory instead of disk  
Data safe across container crashes
# hostPath Volume

Mounts file/directory from host node

## Use cases:
- Access node logs
- Access node configuration
- Write persistent data to node
# PersistentVolume (PV) and PersistentVolumeClaim (PVC)

- **PV:** Storage provisioned by admin or dynamically
- **PVC:** Request for storage by user

## Workflow:
1. Admin creates PVs
2. User creates PVC
3. Kubernetes binds PVC to PV
4. Pod references PVC
# Static vs Dynamic Provisioning

- **Static:** PV created before PVC
- **Dynamic:** PV automatically created with PVC using StorageClass
# StorageClass

Specifies provisioner for dynamic provisioning

## Fields:
- **provisioner:** Plugin/driver
- **parameters:** Provisioner config
- **reclaimPolicy:** What happens after PVC deletion
- **Default:** Mark as default for cluster

## volumeBindingMode:
- **Immediate:** Bind at PVC creation
- **WaitForFirstConsumer:** Delay until pod scheduled
# Reclaim Policy

- **Delete:** PV and storage deleted when PVC deleted
- **Retain:** PV remains, data preserved

Set at PV level or StorageClass level
# Access Modes

| Mode | Abbreviation | Description |
|------|--------------|-------------|
| ReadWriteOnce | RWO | Read-write by single node |
| ReadOnlyMany | ROX | Read-only by many nodes |
| ReadWriteMany | RWX | Read-write by many nodes |
| ReadWriteOncePod | RWOP | Read-write by single pod |

# ConfigMaps

Store non-sensitive configuration data  
Plain-text key-value pairs

## Create from:
- **Literal:** `--from-literal=key=value`
- **File:** `--from-file=file.txt`
- **Directory:** `--from-file=/path/to/dir`

## Use in Pods:
- Environment variables
- Volume mounts
# Security Context

Defines privilege and access control

## Fields:
- **runAsUser:** User ID container runs as
- **runAsGroup:** Primary group ID
- **fsGroup:** Group ID for volume files
# Secrets

Store sensitive data  
Not encrypted by default in ETCD (can configure)  
Displayed as base64 encoded  
Protect with RBAC

**Use:** Environment variables or volume mounts
# sysctl

Utility for kernel parameters

**Temporary:** `sysctl -w parameter=value`

**Permanent:**
- `/etc/sysctl.conf`
- `/etc/sysctl.d/*.conf`

**Apply:** `sysctl --system`
# Kubernetes from Scratch

## Common patterns:
- Certificates for each component
- Kubeconfig files for components
- Configuration flags
- Systemd unit files

## Component order:
1. Certificate Authority
2. ETCD
3. API Server
4. Controller Manager
5. Scheduler
6. Worker nodes (kubelet, kube-proxy, container runtime)
# Component Binaries

- **Server:** API Server, Controller Manager, Scheduler
- **Node:** kubelet, kube-proxy
- **Client:** kubectl
# Network Policies

Control network traffic flow  
**Default:** All traffic allowed

## Rule types:
- **Ingress:** Inbound
- **Egress:** Outbound

## Filtering:
- podSelector
- namespaceSelector
- ipBlock

**CNI support required:** Calico, Cilium (yes), Flannel (no)

## Structure:
- **podSelector:** Which pods policy applies to
- **policyTypes:** [Ingress, Egress, or both]
- **ingress/egress:** Rules
- **from/to:** Traffic sources/destinations
- **except:** Exceptions to rules
- **ports:** Port specifications
# Taints and Tolerations

- **Taint:** Property repelling pods from node
- **Toleration:** Special pass allowing scheduling

## Effects:
- **NoSchedule:** Prevent new pods
- **PreferNoSchedule:** Try to avoid
- **NoExecute:** Evict existing pods

**Add taint:** `kubectl taint nodes node1 key=value:NoSchedule`

**Toleration fields:** key, operator, value, effect
# Editing Resources

- **kubectl edit:** Opens in editor (interactive)
- **kubectl patch:** Non-interactive updates

## Mutable:
- `metadata.labels`
- `metadata.annotations`

## Immutable:
- `metadata.name`
- `spec.containers[*].name`

## Immutable edit workflow:
1. Export to YAML
2. Delete resource
3. Modify YAML
4. Recreate
# Node Capacity

- **Capacity:** Total physical resources
- **Allocatable:** Available after system reservation
- **Allocated:** Currently requested by pods

## Commands:

```bash
kubectl describe node <node-name>
kubectl top nodes
kubectl top pods
```
# JSONPath

Query language for JSON

## Syntax:
- **$:** Root
- **.:** Child operator
- **[index]:** Array element
- **\*:** Wildcard

## Examples:
- `$.items[*].metadata.name`: All pod names
- `$.items[*].spec.containers[*].image`: All images
- `$.items[0].metadata.namespace`: First pod namespace
# Container Runtime Interface (CRI)

Plugin interface for kubelet to communicate with runtimes

## Compatible runtimes:
- containerd
- CRI-O
- Docker Engine (using cri-dockerd)
- Mirantis Container Runtime

## crictl: Tool to interact with CRI runtimes

```bash
crictl pods
crictl ps -a
crictl logs <id>
crictl exec -i -t <id> ls
```
# cri-dockerd

Shim implementing CRI for Docker  
Translates CRI gRPC calls to Docker API

**Socket:** `/var/run/cri-dockerd.sock`
# Kubernetes Events

Created on state changes, errors, messages  
Stored in master server  
**Retention:** 1 hour after last occurrence  
Namespaced

## Commands:

```bash
kubectl get events
kubectl get events --all-namespaces
kubectl get events --field-selector type=Warning
```
# Field Selector

Select resources based on field values  
**Default:** No filters applied
# Monitoring

- **cAdvisor:** Collects metrics, exposes via Kubelet Summary API
- **Metrics Server:** Collects and aggregates from kubelet
- **kube-state-metrics:** Metrics about object state
# Logging

**Docker logging drivers:** json-file, syslog, journald, splunk, awslogs  
`docker logs` only for json-file and journald
# Troubleshooting

## Application:

```bash
kubectl get pods
kubectl describe pod <pod>
kubectl logs <pod>
kubectl get events
```

## Cluster components:

```bash
kubectl get nodes
kubectl cluster-info
kubectl cluster-info dump
systemctl status kubelet
journalctl -u kubelet
```

## Important paths:
- `/etc/kubernetes/manifests` (static pods)
- `/var/log/containers` (container logs)
# Version Skew Policy

**Format:** MAJOR.MINOR.PATCH (e.g., v1.32.2)

- **kube-apiserver (HA):** Within one minor version
- **kubelet:** Up to 3 minor versions older than apiserver
- **kube-proxy:** Up to 3 minor versions older than apiserver
- **Controller Manager/Scheduler:** Up to 1 minor version older than apiserver
- **kubectl:** Within 1 minor version (older or newer) of apiserver
# Taint Based Evictions

Automatic taints on node conditions:

- `node.kubernetes.io/not-ready`
- `node.kubernetes.io/unreachable`
- `node.kubernetes.io/out-of-disk`
- `node.kubernetes.io/memory-pressure`
- `node.kubernetes.io/disk-pressure`
- `node.kubernetes.io/network-unavailable`
- `node.kubernetes.io/unschedulable`
