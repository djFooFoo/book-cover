pipeline {
  agent {
    docker {
        image 'python:3.8'
    }
  }
  stages {
    stage('Test') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh 'pip install --user -r requirements.txt'
          sh 'python -m unittest'
        }
      }
    }
  }
}
