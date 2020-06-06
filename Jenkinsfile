pipeline {
  agent {
    docker {
        image 'python:3.8'
    }
  }
  stages {
    stage('Build') {
      steps {
        sh 'python -m venv env'
        sh '. ./env/bin/activate'
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
