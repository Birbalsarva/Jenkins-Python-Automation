pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                 git url: "https://github.com/Birbalsarva/Bano_Devops_Task_2.git", branch: "main"
            }
        }
        
        stage('Build and Test') {
            steps {
                sh 'python3.10 -m venv myenv'
                sh 'myenv/bin/pip install -r requirements.txt'
                sh 'myenv/bin/python -m unittest test_website_loading.py'
            }
        }
    }
    
    post {
        always {
            sh 'myenv/bin/deactivate || true'
         }
      }
  }
