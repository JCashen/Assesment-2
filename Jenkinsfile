pipeline {
    agent any
    stages {
        stage('setup') {
            steps {
                sh "./assesment2/scripts/setup.sh"
            }
        }
        stage('Test') {
            steps {
                sh "./assesment2/scripts/test.sh"
            }
        }
        stage('Build') {
            steps {
                sh "./assesment2/scripts/build.sh"
            }
        }
        stage('Push') {
            steps {
                sh "./assesment2/scripts/push.sh"
            }
        }
        stage('Deploy') {
            steps {
                sh "./assesment2/scripts/deploy.sh"
            }
        }
    }
}