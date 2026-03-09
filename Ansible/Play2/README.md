# Ansible Playbook 2 – Dynamic Web Page with Jinja2 Template

## Overview

This project is the **second lab in my Ansible automation practice series**.

The goal of this playbook is to deploy a **dynamic web page using a Jinja2 template** and automatically **restart the Apache service when the template changes**.

This demonstrates two important Ansible concepts:

* **Jinja2 Templates**
* **Handlers for service management**

The playbook generates a dynamic `index.html` page containing system information gathered from **Ansible facts**.

---

# Repository Structure

```
Play2/
│
├── ansible.cfg
├── inventory
├── playbook2.yaml
│
└── templates
    └── index.html.j2
```

### Description

| File                        | Purpose                                              |
| --------------------------- | ---------------------------------------------------- |
| **ansible.cfg**             | Custom Ansible configuration                         |
| **inventory**               | Defines managed hosts                                |
| **playbook2.yaml**          | Playbook responsible for deploying the template      |
| **templates/index.html.j2** | Jinja2 template used to generate the dynamic webpage |

---

# Playbook Explanation

## Playbook: `playbook2.yaml`

This playbook runs on hosts in the **web** inventory group.

### Main Task

The `template` module copies a Jinja2 template from the control node to the managed host and renders the variables dynamically.

```
ansible.builtin.template:
  src: templates/index.html.j2
  dest: /var/www/html/index.html
```

If the template file changes, Ansible triggers a **handler**.

---

# Handler

Handlers run **only when notified by a task that caused a change**.

```
handlers:
  - name: temp_result
    ansible.builtin.service:
      name: httpd
      state: restarted
```

This ensures:

* Apache is **restarted only when the template changes**
* Prevents unnecessary service restarts
* Keeps the system **idempotent**

---

# Jinja2 Template

The template file:

```
templates/index.html.j2
```

Generates a dynamic webpage using **Ansible facts**.

Example variables used:

| Variable                       | Description                   |
| ------------------------------ | ----------------------------- |
| `inventory_hostname`           | Hostname defined in inventory |
| `ansible_hostname`             | Actual system hostname        |
| `ansible_default_ipv4.address` | Server IP address             |
| `ansible_distribution`         | Linux distribution            |
| `ansible_distribution_version` | OS version                    |

Example snippet:

```
<li><b>Hostname:</b> {{ ansible_hostname }}</li>
<li><b>IP Address:</b> {{ ansible_default_ipv4.address }}</li>
```

This allows each server to display its **own system information** on the web page.

---

# Running the Playbook

### 1. Test connectivity

```
ansible web -m ping
```

### 2. Execute the playbook

```
ansible-playbook -i inventory playbook2.yaml
```

---

# Expected Result

After running the playbook:

* The template is rendered and copied to:

```
/var/www/html/index.html
```

* Apache is restarted **only if the file changes**
* Opening the server in a browser will display **dynamic system information**

Example output page:

```
Server Info
Inventory name: client1
Hostname: web-server
IP Address: 192.168.1.101
OS: CentOS 9
```

---

# Skills Practiced

This lab demonstrates key **Ansible automation concepts**:

* Jinja2 templating
* Using Ansible facts
* File deployment using the `template` module
* Service management with handlers
* Idempotent automation practices

---

# Author

DevOps Engineer in training focused on:

* Linux System Administration
* Infrastructure Automation
* DevOps Engineering
