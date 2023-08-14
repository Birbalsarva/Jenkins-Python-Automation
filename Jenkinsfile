pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
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
