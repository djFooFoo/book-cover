pipeline {
  agent {
    dockerfile true
  }
  stages {
    stage('Test') {
      steps {
          sh 'python --version'
          sh 'sleep 5'
          sh 'python -m unittest'
      }
    }
  }
}
