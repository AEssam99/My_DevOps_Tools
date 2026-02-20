# Ansible Automation – Multi-Host Setup

- This directory contains Ansible configuration files, inventory definitions, and multiple playbooks used to automate tasks across different servers.

- The environment currently includes two managed nodes:

- `client1` → Web Server
- `client2` → Database Server

More playbooks will be added as the automation journey continues.

## 📁 Project Structure
```java
ansible/
├── ansible.cfg
├── inventory
├── playbook1.yml
├── playbook2.yml
├── playbook3.yml
└── (more plays coming soon...)
```

## 🖥 Inventory Configuration

The inventory file defines two host groups:
```yaml
[web]
client1

[db]
client2
```

- **web group** → Used for web server related tasks
- **db group** → Used for database server related tasks


## ⚙️ Ansible Configuration (ansible.cfg)
```yaml
[defaults]
inventory=./inventory
remote_user=aessam

[privilege_escalation]
become=true
```

### Explanation:

- `inventory=./inventory`  
  Uses the local inventory file in this directory.

- `remote_user=aessam`  
  All playbooks run using the `aessam` user.

- `become=true`  
  Enables privilege escalation (sudo) automatically for tasks requiring root access.



## 🚀 Running Playbooks

To run a playbook:

```bash
ansible-playbook playbook1.yml
```
To target a specific group:

```bash
ansible-playbook playbook1.yml -l web
```
🔍 Verify Connectivity
Check connection to all hosts:

```bash
ansible all -m ping
```
## 📌 Current Scope
- Multi-host inventory setup

- Privilege escalation enabled

- Multiple playbooks for automation tasks

## 🔮 Upcoming Additions
- More playbooks for advanced automation

- Role-based structure

- Variables and templates

- Conditional execution

- Handlers and notifications

- Production-ready structure

## 🛠 Technologies Used
- Ansible

- YAML

- Linux Servers

- SSH-based Automation
