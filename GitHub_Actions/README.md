# GitHub Actions – DevOps Notes

## 📌 Overview

This directory contains structured notes for learning **GitHub Actions** in a logical, step-by-step manner — starting from basic concepts and moving toward advanced workflow design.

GitHub Actions is used to automate **CI/CD pipelines**, enabling building, testing, and deployment directly from your repository.

---

## 🚀 CI vs CD (Foundation First)

### Continuous Integration (CI)

* Automates code integration
* Runs tests on every change
* Ensures code quality

### Continuous Delivery

* Prepares code for deployment
* Requires manual approval

### Continuous Deployment

* Fully automated deployment to production

---

## ⚙️ Workflow Structure (Core Concept)

Workflows are YAML files located at:

```bash id="d4n8qs"
.github/workflows/
```

### Structure:

* **name** → Workflow name
* **on** → When workflow runs
* **jobs** → مجموعة من المهام
* **steps** → Commands inside each job

---

## 🎯 Triggers (Events) – When Workflow Runs

### 1. Webhook Events

Triggered automatically:

* `push`
* `pull_request`
* `issues`
* `release`

---

### 2. Scheduled (Cron Jobs)

```yaml id="lgk7sf"
on:
  schedule:
    - cron: '0 0 * * *'
```

👉 Use for:

* Nightly builds
* Maintenance
* Backups

---

### 3. Manual Triggers (Important Section)

#### workflow_dispatch (Basic Manual Trigger)

```yaml id="83rfxs"
on:
  workflow_dispatch:
```

👉 Use when:

* You want to run workflow manually

---

#### workflow_dispatch with Inputs

```yaml id="m7ghk2"
on:
  workflow_dispatch:
    inputs:
      environment:
        description: "Select environment"
        required: true
```

👉 Use when:

* Choosing environment (dev / prod)
* Running controlled operations

---

#### repository_dispatch (External Trigger)

* Trigger via API

👉 Use when:

* External systems trigger workflows

---

#### workflow_call (Reusable Workflows)

* Call workflow from another workflow

👉 Use when:

* Standardizing pipelines
* Reusing logic across repos

---

## 🖥️ Runners – Where Jobs Run

### Types:

* **GitHub-hosted runners**
* **Self-hosted runners**

👉 Runners execute jobs and provide the environment.

---

## 🧩 Actions – What Runs Inside Steps

Actions are reusable units used inside steps.

### Types:

#### 1. Marketplace Actions

```yaml id="xmn12r"
- uses: actions/checkout@v3
```

👉 Ready-made solutions

---

#### 2. Docker Actions

```yaml id="e7v4gt"
- uses: docker://alpine:latest
```

👉 Isolated container execution

---

#### 3. Local Actions

```yaml id="yqz2t9"
- uses: ./.github/actions/my-action
```

👉 Custom reusable logic

---

#### 4. Composite Actions

👉 Combine multiple steps into one action

---

## ▶️ Running Commands in Steps

```yaml id="q4dj2h"
steps:
  - name: Run command
    run: echo "Hello World"
```

You can:

* Run scripts
* Execute bash commands
* Use shell conditions

---

## 🔗 Jobs – Parallel vs Sequence

👉 By default:

* Jobs run **in parallel**

To make them sequential:

```yaml id="0s6ptv"
jobs:
  job1:
  job2:
    needs: job1
```

👉 `needs` controls execution order.

---

## 🔐 Running Jobs in Containers

```yaml id="rbm5cz"
container:
  image: my-private-image
  credentials:
    username: ${{ secrets.USERNAME }}
    password: ${{ secrets.PASSWORD }}
```

👉 Use for:

* Private images
* Controlled environments

---

## 🔁 Strategy & Matrix – Scaling Jobs

```yaml id="j0c1gk"
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [16, 18]
```

### What happens:

* Creates multiple job combinations
* Runs all in parallel

---

### Advanced:

#### Fail Fast

```yaml id="d8m6yx"
fail-fast: false
```

#### Include Custom Cases

```yaml id="o7lq9k"
matrix:
  include:
    - os: ubuntu-latest
      node: 20
```

---

## 🧠 Expressions & Conditions

### Operators:

* `==`, `!=`
* `&&`, `||`

### Functions:

* `contains()`
* `startsWith()`

---

### Conditional Execution:

```yaml id="7h2jdp"
if: success()
if: failure()
if: always()
if: canceled()
```

---

### Shell Conditions:

```bash id="n2k8az"
if [[ condition ]]; then
  # commands
fi
```

---

## ⚠️ Logging & Debugging

```bash id="k1b5gs"
echo "::warning::message"
echo "::debug::message"
echo "::error::message"
```

---

## 🔄 Environment Variables

### Persist Between Steps:

```bash id="m8v2zn"
echo "NEW_VAR=222" >> $GITHUB_ENV
```

### Usage:

```bash id="a3k9xw"
echo $NEW_VAR
```

---

## 🔒 Masking Sensitive Data

```yaml id="u9f6qp"
run: |
  echo "::add-mask::$NEW_VAR"
  echo "Our Variable is $NEW_VAR"
```

---

## 📦 Built-in Variables (GitHub Context)

### Repository:

* `${{ github.repository }}`
* `${{ github.ref }}`

### Workflow:

* `${{ github.workflow }}`
* `${{ github.run_id }}`

### Actor:

* `${{ github.actor }}`

### Commit:

* `${{ github.sha }}`

### Runner:

* `${{ runner.os }}`
* `${{ runner.arch }}`

---

## 📌 Additional Notes

### Secrets:

```yaml
${{ secrets.MY_SECRET }}
```

Stored in:

```
Settings → Secrets and Variables
```

---

### Multiple Triggers

```yaml id="o5c3ye"
on: [push, pull_request]
```

👉 Works as **OR condition**

---

## 📌 Learning Flow Summary

1. CI/CD basics
2. Workflow structure
3. Triggers (when it runs)
4. Runners (where it runs)
5. Actions (what runs)
6. Steps (how commands run)
7. Jobs (parallel vs sequence)
8. Containers
9. Strategy & matrix
10. Conditions & expressions
11. Variables & secrets
12. Debugging

---

## 📚 Conclusion

This document is now organized as a **step-by-step learning path**, making it easier to understand GitHub Actions from beginner to advanced level.

Next step: implement real workflows 🔥

---
