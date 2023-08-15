pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                 git url: "https://github.com/Birbalsarva/Bano_Devops_Task_2.git", branch: "main"
            }
        }
        
        stage('Build and Test') {
            steps {
                script {
                    sh 'python3.10 -m venv myenv'
                    sh 'source myenv/bin/activate'
                    sh 'xvfb-run -a myenv/bin/python -m unittest test_website_loading.py --verbose'
                }
            }
        }
    }

    post {
        always {
            sh 'bash -c myenv/bin/deactivate || true'
        }
    }
}

               

               
          
