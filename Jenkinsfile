pipeline{
    agent any
    stages{
        stage('Build Docker Image'){
            steps{
                echo 'Building Docker Image...'
                bat 'docker build -t mypythonflaskapp .'
            }
        }
        stage('Run Docker Container'){
            steps{
                echo 'Running Docker Container...'
                bat 'docker run mypythonflaskapp'
            }
        }
    }
    post{
        success{
                echo 'Deployment Successful!'
            }
            failure{
                echo 'Deployment Failed!'
            }
        }
    }
