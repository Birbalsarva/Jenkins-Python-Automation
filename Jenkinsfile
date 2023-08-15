pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build and Test') {
            steps {
                script {
                    sh 'python3.10 -m venv myenv'
                    sh 'bash -c "source myenv/bin/activate"'  // Activate the virtual environment using Bash
                    sh 'xvfb-run bash -c "myenv/bin/python -m unittest test_website_loading.py"'  // Run tests using Bash
                }
            }
        }
    }
    
    post {
        always {
            sh 'bash -c "myenv/bin/deactivate || true"'  // Deactivate the virtual environment using Bash
        }
    }
}
