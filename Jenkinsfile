pipeline {
    agent any

    stages {
        stage('Set Up Virtual Environment') {
            steps {
                echo 'Setting up virtual environment...'
                // Create a virtual environment
                sh 'python3 -m venv venv'
                // Activate the virtual environment
                sh '. venv/bin/activate'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                // Install dependencies in the virtual environment
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Run tests inside the virtual environment
                sh '. venv/bin/activate && python -m unittest discover -s .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                mkdir -p /tmp/python-app-deploy
                cp app.py /tmp/python-app-deploy/
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for more details.'
        }
    }
}
