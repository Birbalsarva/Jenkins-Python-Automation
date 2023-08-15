pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        
        stage('Build and Test') {
            steps {
                script {
                    sh 'python3.10 -m venv myenv'
                    sh './myenv/bin/activate' // Activate virtual environment using relative path
                    sh 'pip install -r requirements.txt' // You can include this line to install required dependencies
                    sh 'xvfb-run -a ./myenv/bin/python -m unittest test_website_loading.py --verbose' // Use relative path for python executable
                    sh './myenv/bin/deactivate' // Deactivate the virtual environment
                }
            }
        }
    }
}
