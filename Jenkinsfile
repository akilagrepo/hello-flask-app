pipeline {
    agent any

    environment {
        IMAGE_NAME = "hello-flask-app:latest"
        CONTAINER_NAME = "hello-flask"
        APP_PORT = "5000"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout your repo
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/akilagrepo/hello-flask-app.git']]])
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove existing container if running
                    sh "docker rm -f ${CONTAINER_NAME} || true"

                    // Run container in detached mode
                    sh "docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:${APP_PORT} ${IMAGE_NAME}"
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully! Access app at http://<EC2-PUBLIC-IP>:5000"
        }
        failure {
            echo "❌ Pipeline failed. Check console output for errors."
        }
    }
}
