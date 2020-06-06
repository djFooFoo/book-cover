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
          sh 'virtualenv venv --distribute'
          sh '. venv/bin/activate'
          sh 'pip install --user -r requirements.txt'
          sh 'python -m unittest'
        }
      }
    }
  }
}
