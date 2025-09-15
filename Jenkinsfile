pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
            git branch: 'main', url: 'https://github.com/akilagrepo/hello-flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t hello-flask-app:latest .'
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
