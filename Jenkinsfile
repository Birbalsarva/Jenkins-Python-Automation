pipeline {
    agent any
    
    stages {
        stage('Checkout SCM') {
            steps {
                  git url: "https://github.com/Birbalsarva/Bano_Devops_Task_2.git", branch: "main"
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'python3.10 -m venv myenv'
                sh 'myenv/bin/pip install -r requirements.txt'
            }
        }
        
        stage('Run Unit Test') {
            steps {
                sh 'myenv/bin/python -m pytest test_website_loading.py'
            }
        }
    }
}
