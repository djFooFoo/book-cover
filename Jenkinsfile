pipeline {
  agent {
    docker {
        image 'python:3.8-alpine'
    }
  }
  stages {
    stage('Build') {
      steps {
        sh 'pip install -r requirements.txt'
        }
    }

    stage('Test') {
      steps {
        sh 'python -m unittest'
      }
    }
  }
}
