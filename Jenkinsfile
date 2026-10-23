pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is available in the workspace'
            }
        }

        stage('Install Pylint') {
            steps {
                sh 'python3 -m venv venv'
                sh 'venv/bin/python -m pip install pylint'
            }
        }

        stage('Static Code Analysis') {
            steps {
                sh 'venv/bin/pylint --rcfile=.pylintrc app/app.py'
            }
        }
    }
}
