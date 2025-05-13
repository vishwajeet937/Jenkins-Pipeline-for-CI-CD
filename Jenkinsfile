pipeline {
    agent any

    environment {
        IMAGE_NAME = "ajith10000/my-flask-app"
        TAG = "${BUILD_ID}"
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
                    sh "docker build -t $IMAGE_NAME:$TAG ."
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run the container and test with pytest inside it
                    sh "docker run --rm $IMAGE_NAME:$TAG pytest test_app.py -v"
                }
            }
        }

        stage('Deploy to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                        sh "docker push $IMAGE_NAME:$TAG"
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
