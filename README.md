# My Secure AWS DevOps Project

---

## About This Project

This project is about setting up a cloud server, installing all the tools needed, running a web app using Docker, and then check it for security problems using Trivy.  
I did this completely from scratch on an AWS EC2 server running Amazon Linux 2023.

---

## Why I Made This

I wanted to practice DevOps and cloud security skills in a real environment instead of just watching tutorials.  
This project helped me learn:
- How to work on AWS EC2 servers.
- How to install Python, Docker, and other tools.
- How to run an app inside a Docker container.
- How to scan that app for vulnerabilities.

---

## What I Used

- **AWS EC2** (Amazon Linux 2023)
- **Python 3**
- **Docker**
- **Trivy** (for security scanning)
- **Git**
- **AWS CLI**

---

## Steps I Followed

Here’s exactly what I did from start to finish.

### 1. Launching the EC2 server

- I logged into my AWS account.
- I launched a new EC2 instance with **Amazon Linux 2023**.
- I selected a **t2.micro** instance type (free tier).
- I added my `.pem` key so I could SSH into it.

### 2. Connecting to the server

On my computer, I opened the terminal and went to where my PEM file was:

```bash
cd ~/Downloads
chmod 400 my-key.pem
ssh -i "my-key.pem" ec2-user@<my-ec2-public-ip>

```
## Security Scanning
This project includes a Trivy vulnerability scan for educational purposes. The scan detected Debian 12 base image vulnerabilities and outdated Python dependencies (Werkzeug, Gunicorn, Setuptools). Work is ongoing to address these issues.
