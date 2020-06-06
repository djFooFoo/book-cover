pipeline {
  agent {
    docker {
        image 'python:3.8'
    }
  }
  stages {
    stage('Build') {
      steps {
        sh 'pip3 install --user -r requirements.txt'
        }
    }

    stage('Test') {
      steps {
        sh 'python -m unittest'
      }
    }
  }
}
