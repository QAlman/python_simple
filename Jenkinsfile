pipeline {
   agent {
      label 'wfm-at'
   }
   stages {
      stage('RUN TESTS') {
         steps {
            catchError {
               sh 'pytest -m "WebTest" --alluredir reports'
            }
         }
      }
      stage('Remove hidden tests') {
         steps {
            sh """
               grep -rl '"status": "skipped"' reports | xargs rm -rf
            """
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
