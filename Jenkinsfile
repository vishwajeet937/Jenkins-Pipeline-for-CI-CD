pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                url: 'https://github.com/AJITH10000/Jenkins-Pipeline-for-CI-CD.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("my-flask-app:${env.BUILD_ID}")
                }
            }
        }

        stage('Test') {
            steps {
                sh 'python -m pytest test_app.py -v'
            }
        }

        stage('Deploy to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image("my-flask-app:${env.BUILD_ID}").push()
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}