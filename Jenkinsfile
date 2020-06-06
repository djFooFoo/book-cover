pipeline {
  agent {
    docker {
        image 'continuumio/miniconda3'
    }
  }
  stages {
    stage('Build') {
      steps {
        sh 'echo $USER'
        sh 'conda env create -f environment.yml'
        sh 'python --version'
        }
    }

    stage('Test') {
      steps {
        sh 'python -m unittest'
      }
    }
  }
}
