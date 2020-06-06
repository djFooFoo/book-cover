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
          sh 'python --version'
        }
      }
    }
  }
}
