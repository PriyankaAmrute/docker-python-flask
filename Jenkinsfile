pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the GitHub repository
                git 'https://github.com/PriyankaAmrute/docker-python-flask.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build Docker image
                sh 'docker build -t docker-python-flask .'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Run Selenium tests
                script {
                    // Create and activate virtual environment
                    sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                    '''
                    // Install dependencies
                    sh 'pip install -r requirements.txt'

                    // Run Selenium test script
                    sh 'python selenium_tests.py'
                }
            }
        }

        stage('Deploy Application') {
            steps {
                // Deploy application (if applicable)
                // Example: deploy Docker container
                sh 'docker run -d -p 80:80 docker-python-flask'
            }
        }
    }
}
