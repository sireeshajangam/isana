#!/bin/bash
set -e

# Authenticate Docker with ECR
/usr/bin/aws ecr get-login-password --region us-east-1 | /usr/bin/docker login --username AWS --password-stdin 571888835380.dkr.ecr.us-east-1.amazonaws.com

# Pull the Docker image from ECR
/usr/bin/docker pull 571888835380.dkr.ecr.us-east-1.amazonaws.com/python-repo:latest

# Run the Docker image as a container
/usr/bin/docker run -d -p 8000:8000 571888835380.dkr.ecr.us-east-1.amazonaws.com/python-repo:latest
