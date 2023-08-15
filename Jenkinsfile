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
                sh 'myenv/bin/python -m unittest discover -s . -p "test_*.py" -v'
            }
        }

        stage('Create Test Reports Directory') {
            steps {
                sh 'mkdir -p test-reports'
                sh 'mv *.xml test-reports'  // Assuming the XML files are generated in the workspace
            }
        }
    }

    post {
        always {
            sh 'myenv/bin/deactivate || true'
        }

        success {
            junit '**/test-reports/test_results.xml'
        }
    }
}


