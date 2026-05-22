pipeline {

    agent any

    environment {
        IMAGE = "secure-app:${BUILD_NUMBER}"
    }

    stages {

        stage('Gitleaks Scan') {
            steps {
                bat '"C:\\Users\\ASUS\\AppData\\Local\\Microsoft\\WinGet\\Packages\\Gitleaks.Gitleaks_Microsoft.Winget.Source_8wekyb3d8bbwe\\gitleaks.exe" detect --source .'
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
                "C:\\Users\\ASUS\\AppData\\Local\\Microsoft\\WinGet\\Packages\\AquaSecurity.Trivy_Microsoft.Winget.Source_8wekyb3d8bbwe\\trivy.exe" image ^
               --ignore-unfixed ^
                --severity CRITICAL ^
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