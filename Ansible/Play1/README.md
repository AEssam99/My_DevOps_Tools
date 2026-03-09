# Ansible Playbook 1 – Apache Installation

## Overview

This project is the **first lab in my Ansible automation practice series**.

The goal of this playbook is to automate the **installation and management of the Apache web server** across multiple Linux hosts using Ansible.

The playbook performs two main tasks:

* Install the Apache HTTP server package
* Start and enable the Apache service

This demonstrates basic **Ansible playbook structure**, including:

* Inventory usage
* Variables
* Package management
* Service management

---

# Repository Structure

```
Play1/
│
├── ansible.cfg
├── inventory
└── playbook1.yaml
```

### Description

| File               | Purpose                                   |
| ------------------ | ----------------------------------------- |
| **ansible.cfg**    | Custom Ansible configuration              |
| **inventory**      | Defines managed hosts                     |
| **playbook1.yaml** | Playbook that installs and manages Apache |

---

# Playbook Explanation

## Playbook: `playbook1.yaml`

The playbook runs on **all hosts defined in the inventory**.

### Variables

A variable is used to define the package name:

```yaml
vars:
  pkg:
    - httpd
```

### Tasks

#### 1. Install Apache Package

Uses the `package` module to install the Apache web server.

```yaml
ansible.builtin.package:
  name: "{{ pkg }}"
  state: present
```

This ensures the package is installed on the target hosts.

---

#### 2. Start and Enable Apache Service

The service module ensures the Apache service is:

* **Started**
* **Enabled at system boot**

```yaml
ansible.builtin.service:
  name: httpd
  state: started
  enabled: yes
```

---

# Example Inventory

Example `inventory` file:

```
[web]
client1
client2
```

---

# Running the Playbook

### 1. Verify connectivity

```
ansible all -m ping
```

### 2. Execute the playbook

```
ansible-playbook -i inventory playbook1.yaml
```

---

# Expected Result

After the playbook runs successfully:

* Apache (`httpd`) will be installed on all hosts
* The service will start immediately
* The service will be enabled to start automatically at boot

You can verify this with:

```
systemctl status httpd
```

---

# Skills Practiced

This lab demonstrates fundamental **Ansible automation concepts**:

* Writing basic playbooks
* Managing packages
* Managing services
* Using variables
* Working with inventories

---

# Author

DevOps Engineer in training focused on:

* Linux Administration
* Infrastructure Automation
* DevOps Engineering
