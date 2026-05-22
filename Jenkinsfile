pipeline {

    agent any

    environment {
        IMAGE = "secure-app:${BUILD_NUMBER}"
    }

    stages {

        stage('Gitleaks Scan') {
            steps {
                bat 'gitleaks detect --source .'
            }
        }

        stage('Build Docker') {
            steps {
                bat 'docker build -t %IMAGE% .'
            }
        }

        stage('Trivy Scan') {
            steps {
                bat '''
                trivy image ^
                --severity HIGH,CRITICAL ^
                --exit-code 1 ^
                %IMAGE%
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy to Kubernetes'
            }
        }
    }
}