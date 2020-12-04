pipeline {
    agent any
    stages {
        stage('setup') {
            steps {
                ansiblePlaybook credentialsId:'private-key', installation:'ansible', inventory:'assesment2/ansible/inventory', playbook:'assesment2/ansible/playbook.yaml', disableHostKeyChecking: true
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