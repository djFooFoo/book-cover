pipeline {
  agent {
    docker {
        image 'continuumio/miniconda3'
    }
  }
  stages {
    stage('Build') {
      steps {
        sh 'apt-get update'
        sh 'conda env create -f environment.yml'
        sh '. ~/.bashrc'
        sh 'conda activate book-cover'
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
