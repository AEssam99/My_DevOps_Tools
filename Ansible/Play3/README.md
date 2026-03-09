# Ansible Playbook 3 – Users & SSH Security Hardening

## Overview

This project is the **third lab in my Ansible automation practice series**.

The goal of this playbook is to automate **user management and SSH security hardening** on Linux servers using Ansible.

The playbook performs the following security tasks:

* Create an administrative user
* Configure SSH key-based authentication
* Disable direct root SSH login
* Disable password authentication
* Safely restart the SSH service when configuration changes

This lab demonstrates **secure server configuration using Infrastructure as Code (IaC).**

---

# Repository Structure

```
Play3/
│
├── ansible.cfg
├── inventory
└── playbook3.yaml
```

### Description

| File               | Purpose                                                  |
| ------------------ | -------------------------------------------------------- |
| **ansible.cfg**    | Custom Ansible configuration                             |
| **inventory**      | Defines the managed hosts                                |
| **playbook3.yaml** | Playbook responsible for SSH hardening and user creation |

---

# Playbook Objectives

This playbook implements the following **server hardening steps**:

1. Create a privileged administrative user
2. Configure SSH key authentication
3. Disable root login via SSH
4. Disable password authentication
5. Restart SSH safely after configuration changes

---

# Playbook Breakdown

## 1. Create Administrative User

A new user named **devops** is created with sudo privileges.

```yaml
ansible.builtin.user:
  name: devops
  shell: /bin/bash
  group: wheel
  append: true
  create_home: true
```

This ensures the user:

* Has a home directory
* Uses `/bin/bash`
* Belongs to the **wheel group** (sudo privileges)

---

# 2. Configure SSH Key Authentication

The playbook installs an SSH public key for the `devops` user.

```yaml
ansible.posix.authorized_key:
  user: devops
  state: present
  key: "{{ lookup('file', '/home/aessam/.ssh/id_rsa.pub') }}"
```

This allows the user to authenticate using **SSH key pairs instead of passwords**.

---

# 3. Disable Root SSH Login

Direct root access via SSH is disabled for better security.

```yaml
ansible.builtin.lineinfile:
  path: /etc/ssh/sshd_config
  regexp: ^(#\s*)?PermitRootLogin
  line: PermitRootLogin no
```

---

# 4. Disable Password Authentication

The playbook enforces **key-only SSH access**.

```yaml
ansible.builtin.lineinfile:
  path: /etc/ssh/sshd_config
  regexp: ^(#\s*)?PasswordAuthentication
  line: PasswordAuthentication no
```

This prevents password-based SSH attacks such as **brute force attempts**.

---

# Safe SSH Configuration Validation

Before applying the configuration change, Ansible validates the SSH configuration:

```
validate: '/usr/sbin/sshd -t -f %s'
```

This ensures:

* The configuration syntax is correct
* SSH will not break after the change
* Prevents accidental **server lockout**

---

# Handler – Restart SSH Service

If the SSH configuration changes, a handler restarts the SSH service.

```yaml
handlers:
  - name: Restart_SSH
    service:
      name: sshd
      state: restarted
```

Handlers ensure that the service is restarted **only when necessary**.

---

# Running the Playbook

### 1. Test connectivity

```
ansible web -m ping
```

### 2. Execute the playbook

```
ansible-playbook -i inventory playbook3.yaml
```

---

# Expected Result

After successful execution:

* A new **devops** user exists on the servers
* SSH login works using **key authentication**
* **Root SSH login is disabled**
* **Password authentication is disabled**
* SSH service restarts automatically if configuration changes

---

# Skills Practiced

This project demonstrates important **DevOps and Linux administration skills**:

* Linux user management
* SSH security hardening
* Infrastructure as Code (IaC)
* Idempotent configuration management
* Secure service configuration
* Safe automation practices

---

# Author

DevOps Engineer in training focused on:

* Linux System Administration
* Infrastructure Automation
* DevOps Engineering
