
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
                    sh 'source myenv/bin/activate'
                    sh 'pip install -r requirements.txt' // You can include this line to install required dependencies
                    sh 'xvfb-run -a myenv/bin/python -m unittest test_website_loading.py --verbose'
                    sh 'deactivate' // Deactivate the virtual environment
                }
            }
        }
    }

    post {
        always {
            sh 'true' // Do nothing, this is just to avoid the error on the following line
            sh 'myenv/bin/deactivate' // Deactivate the virtual environment
        }
    }
}

               

               
          
