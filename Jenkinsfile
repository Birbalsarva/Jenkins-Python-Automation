pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: "https://github.com/Birbalsarva/Bano_Devops_Task_2.git", branch: "main"
                
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Unit Test') {
            steps {
                sh 'python3 test_website_loading.py'
            }
        }
    }
}
