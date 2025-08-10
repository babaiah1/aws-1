# aws-1

````markdown
# Secure CI/CD Demo Project

---

## Table of Contents
- [Project Overview](#project-overview)  
- [Prerequisites](#prerequisites)  
- [Setup Steps](#setup-steps)  
- [How to Run the Project](#how-to-run-the-project)  
- [Testing](#testing)  
- [Security Scanning with Trivy](#security-scanning-with-trivy)  
- [Technologies Used](#technologies-used)  
- [What to Highlight on Your Resume](#what-to-highlight-on-your-resume)  
- [Contact](#contact)  

---

## Project Overview

This project demonstrates a simple web application deployed on an AWS EC2 instance, with a secure CI/CD pipeline focus.  
The project covers:

- Setting up an Amazon Linux 2023 EC2 instance from scratch.  
- Installing all required dependencies: Docker, Python 3, AWS CLI, Terraform, and Trivy.  
- Cloning and running a Python-based web application inside a Docker container.  
- Performing automated security scanning on the Docker image with Trivy.  

This project simulates real-world cloud and DevOps workflows, showing your ability to build, secure, and deploy applications in AWS environments.

---

## Prerequisites

- AWS account with permissions to launch EC2 instances.
- An EC2 instance running Amazon Linux 2023.
- PEM key file to SSH into your EC2 instance.
- Basic knowledge of terminal/command line (or follow instructions carefully).
- Windows PowerShell or any SSH client for remote login.

---

## Setup Steps

### 1. Connect to your EC2 instance

```powershell
cd ~/Downloads
ssh -i "aws-1.pem" ec2-user@<your-ec2-public-ip>
````

Make sure your `.pem` file has proper permissions:

```powershell
chmod 400 aws-1.pem
```

### 2. Update the system

```bash
sudo dnf update -y
```

### 3. Install essential tools

```bash
sudo dnf install -y git curl unzip wget jq make gcc gcc-c++ openssl-devel bzip2 libffi-devel
```

### 4. Install Docker

```bash
sudo dnf install -y docker
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
newgrp docker
docker --version
```

### 5. Install Python 3 and pip

```bash
sudo dnf install -y python3 python3-pip python3-devel
python3 --version
pip3 --version
```

### 6. Install AWS CLI v2

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
```

### 7. Install Terraform (optional for this project, skipped here)

### 8. Install Trivy (security vulnerability scanner)

```bash
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sudo sh -s -- -b /usr/local/bin
trivy --version
```

### 9. Clone the project repository

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 10. Setup Python virtual environment and install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## How to Run the Project

### Build the Docker image

```bash
docker build -t myapp .
```

### Run the Docker container

```bash
docker run -d -p 8000:8000 myapp
```

The application should now be accessible at `http://<your-ec2-public-ip>:8000`

---

## Testing

Inside your virtual environment, you can run:

```bash
pytest
```

This will run the automated tests included in the project.

---

## Security Scanning with Trivy

You ran:

```bash
trivy image myapp
```

Trivy scanned the Docker image for vulnerabilities and reported some findings (mostly in Python packages and dependencies). This is a critical DevSecOps skill demonstrating your awareness of security in the CI/CD pipeline.

---

## Technologies Used

* **AWS EC2:** Amazon Linux 2023 instance as deployment environment.
* **Docker:** Containerizing the Python web application.
* **Python 3:** Backend language with Flask framework.
* **AWS CLI:** Managing AWS resources and deployments.
* **Trivy:** Security vulnerability scanning of container images.
* **Git:** Version control and project cloning.
* **PowerShell:** Local Windows terminal for SSH connection.

---

## What to Highlight on Your Resume

* **Project Title:** Secure CI/CD Pipeline Demo on AWS
* **Description:** Developed and deployed a containerized Python web application on an Amazon Linux 2023 EC2 instance. Automated environment setup with Python virtual environments, Docker containerization, and security vulnerability scanning using Trivy.
* **Skills:** AWS EC2, Amazon Linux 2023, Docker, Python (Flask), AWS CLI, Linux command line, Trivy security scanning, Git, PowerShell SSH usage.
* **Achievements:**

  * Successfully automated the environment setup and application deployment.
  * Performed Docker image vulnerability analysis and mitigation awareness.
  * Demonstrated ability to work with cloud-native tools and CI/CD best practices.

---

## Contact

For any questions or further help, please reach out or check the project repo README.

---

*This README aims to help beginners understand the entire workflow from zero to deployment with security scanning included.*
*Follow the steps carefully and you will be able to replicate and explain the project confidently in interviews.*

---

**End of README.md**

```
If you want, I can help you generate a nicely formatted `README.md` file ready to commit to your repo!
```
