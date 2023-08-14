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
                sh '''
                    python3.10 -m venv myenv
                    source myenv/bin/activate
                    pip install -r requirements.txt
                    python test_website_loading.py
                '''
            }
        }
    }

    post {
        always {
            sh 'deactivate' // Deactivate virtual environment
        }
    }
}

                 

