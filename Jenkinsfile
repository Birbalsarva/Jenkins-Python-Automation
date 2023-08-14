
pipeline {
    agent any
    environment {
        PATH = "/usr/local/bin:${env.PATH}"  // Include the directory containing chromedriver
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Birbalsarva/Bano_Devops_Task_2.git', branch: 'main'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Unit Test') {
            steps {
                sh 'google-chrome --no-sandbox --disable-gpu --headless --remote-debugging-address=0.0.0.0 --remote-debugging-port=9222 &'
                sh 'python3 test_website_loading.py'
            }
        }
    }
}
