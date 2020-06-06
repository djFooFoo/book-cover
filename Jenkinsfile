pipeline {
  agent {
    dockerfile true
  }
  stages {
    stage('Test') {
      parallel {
        stage('Static code analysis') {
          steps {
            sh 'ls -la'
            sh 'cd /app'
            sh 'pylint *.py'
          }
        }
        stage('Unit tests') {
          steps {
            sh 'ls -la'
            sh 'python -m unittest' }
        }
      }
    }
  }
}
