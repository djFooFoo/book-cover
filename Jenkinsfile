pipeline {
  agent {
    dockerfile true
  }
  stages {
    stage('Test') {
      parallel {
        stage('Static code analysis') {
          withEnv(['PYLINTHOME=.']) {
            steps { sh 'pylint *.py' }
          }
        }
        stage('Unit tests') {
            steps { sh 'python -m unittest' }
        }
      }
    }
  }
}
