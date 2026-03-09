# Ansible Multi-Tier Infrastructure Automation Lab Overview
This project demonstrates infrastructure automation using Ansible roles to configure a small multi-tier environment consisting of:
- Common server role
- Web server role
- Database server role
The automation follows Ansible best practices by separating logic into roles and organizing configuration using variables, handlers, templates, and encrypted secrets.

The project simulates a simple production-style architecture where a web server connects to a database server, while all systems receive common security and system configuration.
# Project Architecture
Example topology used in the lab:
```sh
Ansible Control Node
        │
        ├── client1  →  Web Server
        │
        └── client2  →  Database Server
```
# Repository Structure
```sh
play4/
│
├── ansible.cfg
├── inventory
├── playbook4.yaml
│
├── db/
│   ├── defaults/
│   │   └── main.yml
│   └── tasks/
│       └── main.yml
│
├── servers/
│   ├── defaults/
│   │   └── main.yml
│   ├── handlers/
│   │   └── main.yml
│   └── tasks/
│       └── main.yml
│
├── web/
│   ├── defaults/
│   │   └── main.yml
│   ├── tasks/
│   │   └── main.yml
│   └── templates/
│       └── temp.j2
│
└── README.md
```
# Roles Description
## 1. Servers Role

This role applies common configuration to all managed hosts.

### Tasks

- Install common packages (vim, curl)

- Create system users (devops, auditor)

- Configure SSH public key authentication

- Disable root SSH login

- Disable password authentication

### Handlers

- Restart SSH service when SSH configuration changes.

### Variables
Defined in:
```sh
servers/dafaults/main.yml
```
## 2. Web Role

The web role installs and configures the web server depending on the operating system.

### Supported systems

- Ubuntu → apache2

- CentOS / Rocky Linux → httpd

### Tasks

- Install the appropriate web server package

- Start and enable the service

- Deploy a dynamic web page using a Jinja2 template

### Template
```sh
web/templates/temp.j2
```
The template dynamically displays:

- Hostname

- Operating System

- Server IP Address

This demonstrates the use of Ansible facts and templating.

## 3. DB Role

The db role installs and configures MariaDB database server.

### Tasks

- Install MariaDB server

- Start and enable MariaDB service

- Create a database

- Create a database user

- Assign privileges to the user

### Database variables are defined in:
```sh
db/defaults/main.yml
```
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
## Main Playbook

The main playbook:
```sh
playbook4.yaml
```
It orchestrates the deployment by applying roles to the appropriate host groups:
```sh
Host Group |	Role  |
───────────|──────────|
all	       | servers  |
───────────|──────────|
web	       | web      |
───────────|──────────|
db	       |db        |
───────────└──────────|
```
## Running the Project
1. Clone the repository
```sh
git clone https://github.com/AEssam99/My_DevOps_Tools.git
cd Ansible/Play4
```
2. Verify connectivity
```sh
ansible all -m ping
```
3. Run the playbook
```sh
ansible-playbook playbook4.yaml --ask-vault-pass
```
`Note`
As we have encrypted file at db role using Ansible-Vault so we used:
```sh
--ask-vault-pass
```
## Skills Demonstrated
This project demonstrates practical DevOps and Infrastructure Automation skills:

- Ansible Roles
- Infrastructure as Code (IaC)
- Configuration Management
- Secure secrets management with Ansible Vault
- Jinja2 templating
- Linux server automation
- Multi-tier architecture deployment

## Author
DevOps Engineer in training focusing on:
- Linux System Administration
- Infrastructure Automation
- SysAdmin & DevOps Engineering