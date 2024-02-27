pipeline {
    agent any
    
    environment {
        AWS_DEFAULT_REGION = us-east-1
        ECR_REGISTRY = 862547479026.dkr.ecr.us-east-1.amazonaws.com/python:latest
        IMAGE_NAME = isana
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_KEY_ID')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Login to AWS ECR
                    sh "aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${ECR_REGISTRY}"

                    // Build Docker image
                    sh "docker build -t ${IMAGE_NAME} ."

                    // Tag Docker image
                    sh "docker tag ${IMAGE_NAME}:latest ${ECR_REGISTRY}/${IMAGE_NAME}:latest"

                    // Push Docker image to ECR
                    sh "docker push ${ECR_REGISTRY}/${IMAGE_NAME}:latest"
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image built and pushed successfully!'
        }
    }
}
