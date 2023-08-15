pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git url: "https://github.com/Birbalsarva/Banao_Devops_Task_2.git", branch: "main"
            }
        }
        
        stage('Build and Test') {
            steps {
                sh 'python3.10 -m venv myenv'
                sh 'myenv/bin/pip install -r requirements.txt'
                sh 'myenv/bin/python -m unittest discover -s . -p "test_*.py" -v --resultxml=test-reports/test_results.xml'
            }
        }
    }
    
    post {
        always {
            sh 'myenv/bin/deactivate || true'
        }
        
        success {
            junit 'test-reports/test_results.xml'
        }
    }
}
