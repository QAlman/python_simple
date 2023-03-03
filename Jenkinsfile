pipeline {
   agent {
      label 'wfm-at'
   }
   stages {
      stage('RUN TESTS') {
         steps {
            catchError {
               sh 'python3 -m pytest --alluredir reports'
            }
         }
      }
      stage('Reports') {
         steps {
            allure([
      	      includeProperties: false,
      	      jdk: '',
      	      properties: [],
      	      reportBuildPolicy: 'ALWAYS',
      	      results: [[path: 'reports']]
    	      ])
  	      }
      }
   }
}