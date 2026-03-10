# Ansible Automation Projects

This directory contains a collection of **Ansible automation labs and projects** developed as part of my DevOps learning journey.
Each project focuses on automating common infrastructure tasks using **Infrastructure as Code (IaC)** principles.

The goal of these projects is to demonstrate practical experience with:

* Configuration Management
* Server Provisioning
* Infrastructure Automation
* Security Hardening
* Service Deployment
* Role-based Architecture

All automation tasks are implemented using **Ansible playbooks, inventories, variables, and roles** to simulate real-world DevOps workflows.

---

# Repository Structure

```
Ansible
│
├── Play1
├── Play2
├── Play3
└── Play4
```

Each project introduces **new Ansible concepts** and builds on the knowledge gained in previous labs.

---

# Projects Overview

## Play1 – Ansible Fundamentals

This project introduces the **basic structure of Ansible automation**.

Key concepts covered:

* Inventory configuration
* Running ad-hoc commands
* Writing simple playbooks
* Package management automation

Example tasks:

* Install packages on remote servers
* Execute commands on multiple hosts
* Verify connectivity using Ansible modules

Skills gained:

* Understanding Ansible architecture
* Writing basic playbooks
* Managing remote hosts using Ansible

---

# Play2 – Linux User & Security Automation

This project focuses on **automating Linux user management and system configuration**.

Key tasks automated:

* Creating multiple Linux users
* Assigning user groups
* Managing login shells
* Configuring SSH authentication
* Managing system configuration files

Skills gained:

* User lifecycle automation
* Security configuration using Ansible
* Working with loops and variables

---

# Play3 – Service Deployment Automation

This project demonstrates **automated service installation and management** across different servers.

Main automation tasks:

* Installing services depending on OS distribution
* Managing system services
* Ensuring services are enabled and running
* Applying configuration changes across multiple hosts

Skills gained:

* Conditional task execution
* Cross-platform automation
* Service lifecycle management

---

# Play4 – Role-Based Infrastructure Deployment

This is the **most advanced project in this repository**, implementing a **multi-role infrastructure deployment using Ansible Roles**.

The project simulates a **multi-tier infrastructure environment** consisting of:

* Base server configuration
* Web server deployment
* Database server deployment

Roles used in this project:

```
servers
web
db
```

### Server Role

Handles **common server configuration and security hardening**:

* Install essential system packages
* Create system users
* Configure SSH key authentication
* Disable root SSH login
* Disable password-based authentication

### Web Role

Deploys and configures a **web server environment**:

* Install Apache (httpd or apache2 depending on OS)
* Deploy a dynamic web page
* Start and enable the web service
* Use Ansible facts to display server information

### Database Role

Automates **MariaDB database deployment**:

* Install MariaDB server
* Enable and start the database service
* Create databases
* Create database users
* Assign database privileges

---

# Ansible Features Used

Across the four projects, the following Ansible features are used:

* Playbooks
* Inventory management
* Variables
* Group variables
* Roles
* Loops
* Conditionals (`when`)
* Handlers
* Templates (Jinja2)
* Ansible Facts
* Ansible Vault
* Secure configuration management

---

# Technologies Used

* Ansible
* YAML
* Jinja2 Templates
* Apache HTTP Server
* MariaDB
* Linux (Rocky Linux, CentOS, Ubuntu)

---

# Skills Demonstrated

These projects demonstrate hands-on experience with:

* Infrastructure as Code (IaC)
* Configuration Management
* Linux System Administration
* Secure Server Configuration
* Automated Service Deployment
* Multi-host Infrastructure Automation
* Cross-platform Configuration Management
* Role-based Ansible Project Structure

---

# Purpose of This Repository

This repository serves as:

* A **DevOps learning journal**
* A **portfolio of automation projects**
* A **reference for Ansible best practices**

Each project progressively introduces more advanced automation concepts to simulate real-world DevOps environments.


---

# Author

Ahmed Essam-Eldin

DevOps & System Administration Enthusiast
