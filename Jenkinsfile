pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/YOUR_GITHUB_USERNAME/hello-flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("hello-flask-app:latest")
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh 'docker rm -f hello-flask || true'
                    sh 'docker run -d --name hello-flask -p 5000:5000 hello-flask-app:latest'
                }
            }
        }
    }
}
