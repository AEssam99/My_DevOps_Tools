# Ansible Playbook – Multi-Tier Server Configuration (Play4)

This project demonstrates a **production-style Ansible automation setup** using **roles** to configure a multi-tier infrastructure environment.

The playbook automates configuration for three server categories:

* **Base Server Configuration**
* **Web Server Deployment**
* **Database Server Deployment**

The environment supports **multiple Linux distributions (Rocky Linux, CentOS, Ubuntu)** and applies **security hardening, package management, web hosting, and database provisioning** using reusable Ansible roles.

---

# Project Architecture

This project follows the **recommended Ansible roles structure** to ensure modularity and scalability.

```
Play4
│
├── ansible.cfg
├── inventory
├── playbook4.yaml
├── README.md
│
├── servers
│   ├── defaults
│   │   └── main.yml
│   ├── handlers
│   │   └── main.yml
│   └── tasks
│       └── main.yml
│
├── web
│   ├── defaults
│   │   └── main.yml
│   ├── tasks
│   │   └── main.yml
│   └── templates
│       └── temp.j2
│
└── db
    ├── defaults
    │   └── main.yml
    └── tasks
        └── main.yml
```

Each role is responsible for configuring a specific layer of the infrastructure.

---

# Infrastructure Roles

## 1️⃣ Servers Role (Base System Configuration)

The **servers role** prepares all hosts with common system configuration and security hardening.

This role ensures that all servers:

* Have required packages installed (vim, curl)
* Have standardized user accounts (devops, auditor)
* Use SSH key authentication
* Disable insecure SSH access methods

### Package Installation

Packages defined in the defaults file are installed using a loop.

```yaml
- name: Install packages {{pkg}}
  ansible.builtin.package:
    name: "{{ item }}"
    state: present
  loop: "{{ pkg }}"
```

---

### User Provisioning

Multiple system users are created automatically.

```yaml
- name: Create multiple users
  ansible.builtin.user:
    name: "{{ item }}"
    shell: /bin/bash
    create_home: true
    groups: wheel
    append: yes
  loop: "{{ users }}"
```

Users are granted **sudo privileges** by adding them to the **wheel group**.

---

### SSH Key Authentication

Each user receives the controller node's SSH public key to allow secure login.

```yaml
- name: Add SSH public key to each user
  ansible.posix.authorized_key:
    user: "{{item}}"
    state: present
    key: "{{ lookup('file', '/home/aessam/.ssh/id_rsa.pub') }}"
  loop: "{{users}}"
```

This ensures:

* Passwordless SSH login
* Secure automation access

---

### SSH Hardening

Root login is disabled to prevent direct administrative access.

```yaml
- name: Disable direct root SSH login
  ansible.builtin.lineinfile:
    path: /etc/ssh/sshd_config
    regexp: ^(#\s*)?PermitRootLogin
    line: PermitRootLogin no
    validate: '/usr/sbin/sshd -t -f %s'
  notify: Restart_SSH
```

Password authentication is also disabled.

```yaml
- name: Disable Password Auth
  ansible.builtin.lineinfile:
    path: /etc/ssh/sshd_config
    regexp: ^(#\s*)?PasswordAuthentication
    line: PasswordAuthentication no
    validate: '/usr/sbin/sshd -t -f %s'
  notify: Restart_SSH
```

Any SSH configuration change triggers the handler:

```yaml
Restart_SSH
```

which restarts the SSH service safely.

---

# 2️⃣ Web Role (Web Server Deployment)

The **web role** installs and configures a web server depending on the operating system.

Supported distributions:

* Rocky Linux
* CentOS
* Ubuntu

---

## Web Server Installation

For **Rocky Linux / CentOS**, Apache HTTPD is installed:

```yaml
- name: Install httpd service for Centos/Rocky
  ansible.builtin.package:
    name: httpd
    state: present
  when: ansible_distribution == "CentOS" or ansible_distribution == "Rocky"
```

For **Ubuntu**, Apache2 is installed:

```yaml
- name: Install apache2 service for Ubunto
  ansible.builtin.package:
    name: apache2
    state: present
  when: ansible_distribution == "Ubuntu"
```

---

## Dynamic Web Page Deployment

The role uses **Jinja2 templates** to generate a dynamic web page that displays server information.

Template deployment:

```yaml
- name: Create index.html using template
  ansible.builtin.template:
    src: temp.j2
    dest: /var/www/html/index.html
```

Example template content:

```
Server: {{ ansible_hostname }}
OS: {{ ansible_distribution }}
IP: {{ ansible_default_ipv4.address }}
```

This allows each server to automatically generate its own web page with runtime system information.

---

## Web Service Management

The web server service is enabled and started automatically.

For **Rocky/CentOS**:

```yaml
- name: enable_httpd
  service:
    name: httpd
    state: started
    enabled: yes
```

For **Ubuntu**:

```yaml
- name: enable_apache
  service:
    name: apache2
    state: started
    enabled: yes
```

---

# 3️⃣ Database Role (MariaDB Deployment)

The **db role** automates installation and configuration of a MariaDB database server.

The role performs:

* MariaDB installation
* Database service management
* Python MySQL dependency installation
* Database creation
* Database user creation with privileges

---

## MariaDB Installation

```yaml
- name: Install mariadb package
  ansible.builtin.package:
    name:
      - mariadb
      - mariadb-server
    state: present
```

---

## Start and Enable Database Service

```yaml
- name: enable and start mariadb
  ansible.builtin.service:
    name: mariadb
    state: started
    enabled: yes
```

---

## Python Dependency Installation

Ansible's MySQL modules require **PyMySQL**.

```yaml
- name: Install PyMySQL for mysql module
  ansible.builtin.package:
    name:
      - python3-PyMySQL.noarch
    state: present
```

---

## Database Creation

The database name is defined in the role variables.

Rocky/CentOS socket path:

```yaml
login_unix_socket: /var/lib/mysql/mysql.sock
```

Ubuntu socket path:

```yaml
login_unix_socket: /run/mysqld/mysqld.sock
```

Example task:

```yaml
- name: Create new databases
  community.mysql.mysql_db:
    name: "{{ db_name }}"
    state: present
```

---

## Database User Creation

A dedicated database user is created and granted full privileges on the database.

```yaml
- name: Create database user
  community.mysql.mysql_user:
    name: "{{ db_user }}"
    password: "{{ db_password }}"
    priv: '{{ db_name }}.*:ALL'
    state: present
```

This allows application services to securely interact with the database.

---

### Database variables 

```yaml
---
# defaults file for db

db_user: appuser
db_password: SuperSecret123
db_name: appdb
```
Sensitive credentials can be protected using Ansible Vault.
```sh
ansible-vault encrypt db/defaults/main
```

--- 

# Playbook Execution

To run the full infrastructure configuration:

```sh
ansible-playbook playbook4.yaml --ask-vault-pass
```
`Note`
As we have an encrypted file at db role using Ansible-Vault so we used:
```sh
--ask-vault-pass
```

This will sequentially execute:

1. **servers role** on all hosts
2. **web role** on web servers
3. **db role** on database servers

---

# Skills Demonstrated

This project demonstrates several core **DevOps and Automation skills**:

* Infrastructure as Code (IaC)
* Ansible Role-Based Architecture
* Linux System Automation
* SSH Hardening
* Multi-distribution Package Management
* Apache Web Server Deployment
* MariaDB Database Provisioning
* Dynamic Configuration using Jinja2 Templates
* Idempotent Infrastructure Design

---

# Future Improvements

Potential enhancements for this project:

* Implement **Ansible Vault** for database credentials
* Add **firewall automation (firewalld / ufw)**
* Add **Nginx role**
* Add **Load Balancer role**
* Add **Dockerized services**
* Integrate with **CI/CD pipelines**

---

# Author

Ahmed Essam
DevOps / System Administration Enthusiast

