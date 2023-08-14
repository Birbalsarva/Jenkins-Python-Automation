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
                sh 'python3.10 -m venv myenv'
                sh 'source myenv/bin/activate' // Update this line
                sh 'myenv/bin/pip install -r requirements.txt'
            }
        }
        
        stage('Run Unit Test') {
            steps {
                sh '/var/lib/jenkins/workspace/unit_test/myenv/bin/python -m pytest test_website_loading.py' // Update this line
            }
        }
    }
}
