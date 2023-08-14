pipeline {
    agent any
    environment {
        PATH = "/usr/local/bin/chromedriver" // Add the path to Chromedriver here
    }
    stages {
        stage('Checkout') {
            steps {
                git url: "https://github.com/Birbalsarva/Bano_Devops_Task_2.git", branch: "main"
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Unit Test') {
            steps {
                sh 'python3 test_website_loading.py'
            }
        }
    }
}
