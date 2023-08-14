pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                  git url: "https://github.com/Birbalsarva/Bano_Devops_Task_2.git", branch: "main"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv myenv'
                sh 'source myenv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Unit Test') {
            steps {
                sh 'source myenv/bin/activate && python test_website_loading.py'
            }
        }
    }
}

