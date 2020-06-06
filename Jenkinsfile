pipeline {
  agent {
    docker {
        image 'python:3.8'
    }
  }
  stages {
    stage('Build') {
      steps {
          withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'pip install --user -r requirements.txt'
          }
        }
    }

    stage('Test') {
      steps {
        sh 'python -m unittest'
      }
    }
  }
}
