# GOST RA Client

`gost-ra-client` is an offline-first Python client and GUI toolkit for interacting with GOST-enabled Registration Authority (RA) REST APIs in enterprise environments.

The project is designed for infrastructures where:

- mutual TLS authentication is mandatory
- CryptoPro CSP is used for certificate/key operations
- client certificates are stored in CryptoPro containers
- direct OpenSSL integration is undesirable or unsupported
- operational hosts may have no internet access
- Python applications must run in isolated enterprise Linux environments

The project intentionally separates:

- transport execution
- REST API bindings
- business/service logic
- GUI presentation

to support maintainable deployment in secured environments.

The reference runtime model is:

```text
PySide6 GUI
    ↓
Python service layer
    ↓
CryptoPro curl wrapper
    ↓
GOST mutual TLS
    ↓
RA REST API
```

The project does **not** attempt to implement custom cryptography bindings or OpenSSL engine integrations.

Instead, the recommended approach is:

- use vendor-supported CryptoPro tooling
- execute authenticated requests through CryptoPro curl
- isolate runtime dependencies from system Python
- deploy application runtimes in self-contained directories

---

# Runtime Deployment Strategy

## Overview

Enterprise target environments may:

- prohibit internet access
- restrict package manager usage
- contain outdated system Python versions
- require strict runtime isolation
- forbid modification of system packages

For these reasons, the recommended deployment model is:

- deploy an isolated Python runtime into `/opt/...`
- avoid modifying system Python
- install all dependencies offline
- keep application/runtime self-contained

Recommended target layout:

```text
/opt/gost-ra-client/
├── python/
├── venv/
├── app/
├── wheels/
├── logs/
├── exports/
└── cache/
```

---

# Recommended Python Runtime Strategy

## Do NOT replace system Python

System Python should remain untouched.

Avoid:

```bash
sudo apt remove python
sudo update-alternatives
```

The application should use its own dedicated runtime.

---

# Recommended Runtime Location

Example:

```text
/opt/gost-ra-client/python/
```

This runtime is fully independent from the OS Python installation.

---

# Offline Python Deployment

## Step 1 — Prepare Runtime on Internet-Connected Machine

Build or download a compatible Python runtime.

Recommended versions:

- Python 3.11
- Python 3.12

Example build target:

```text
python-3.11.x-linux-x86_64/
```

Transfer archive to the target environment.

---

## Step 2 — Extract Runtime on Target Machine

Example:

```bash
sudo mkdir -p /opt/gost-ra-client
sudo tar -xf python-runtime.tar.gz -C /opt/gost-ra-client/
```

Result:

```text
/opt/gost-ra-client/python/bin/python3
```

---

# Virtual Environment

Create isolated virtual environment:

```bash
/opt/gost-ra-client/python/bin/python3 -m venv \
    /opt/gost-ra-client/venv
```

Activate:

```bash
source /opt/gost-ra-client/venv/bin/activate
```

---

# Offline Dependency Installation

## Prepare Wheels on Connected Machine

Example:

```bash
pip download -r requirements.txt -d wheels/
```

Transfer:

```text
wheels/
```

to target host.

---

## Install Offline

Example:

```bash
pip install \
    --no-index \
    --find-links=/opt/gost-ra-client/wheels \
    -r requirements.txt
```

---

# CryptoPro Integration Strategy

The project intentionally avoids direct OpenSSL/CSP integration inside Python.

Recommended transport model:

```text
Python
    ↓
subprocess
    ↓
CryptoPro curl
    ↓
mTLS authentication
```

Example transport executable:

```text
/opt/cprocsp/bin/amd64/curl
```

Client certificate selection is expected to use CryptoPro-supported mechanisms such as certificate thumbprints.

---

# Runtime Separation

Recommended host roles:

| Host | Responsibility |
|---|---|
| MONITOR | RDP / operator access only |
| JUMP | application runtime + CryptoPro + GUI |
| SERVER | nginx + RA API backend |

The full application stack is expected to run on the JUMP host.

---

# Project Architecture

```text
gostra_gui
    ↓
gostra_services
    ↓
gostra_api
    ↓
gostra_transport
    ↓
CryptoPro curl
```

Layer responsibilities are intentionally isolated to simplify:

- offline deployment
- debugging
- testing
- future GUI changes
- transport replacement
- mock/testing environments

---

# Design Goals

- offline-first operation
- deterministic deployment
- isolated runtime environment
- enterprise maintainability
- minimal system modification
- compatibility with secured infrastructures
- support for GOST-enabled mutual TLS environments

---

# Non-Goals

The project does not aim to:

- replace CryptoPro CSP
- implement custom GOST cryptography
- bypass enterprise PKI policy
- expose private infrastructure details
- depend on internet-hosted runtime services
