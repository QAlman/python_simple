pipeline {
   agent {
      label 'wfm-at'
   }
   parameters {
      choice (choices: ['WebTest', 'ApiTest'], name: 'TESTS')
   }
   stages {
      stage('RUN TESTS') {
         steps {
            catchError {
               sh 'pytest -m $TESTS --alluredir reports || true'
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
