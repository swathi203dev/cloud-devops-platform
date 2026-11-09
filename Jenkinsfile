pipeline {
    agent any

    environment {
        IMAGE_NAME = 'swathireddy203/cloud-devops-platform'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Tests') {
            steps {
                sh '''
                    python3 app/app.py > app.log 2>&1 &
                    APP_PID=$!
                    sleep 2

                    set +e
                    python3 -m unittest discover -s tests -v
                    TEST_STATUS=$?
                    set -e

                    kill "$APP_PID" 2>/dev/null || true
                    exit "$TEST_STATUS"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $IMAGE_NAME:latest
                        docker logout
                    '''
                }
            }
        }
    }
}
