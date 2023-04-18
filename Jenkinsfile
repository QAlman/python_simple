pipeline {
   agent {
      label 'wfm-at'
   }
   parameters {
      choice (choices: ['WebTest', 'ApiTest'], name: 'TESTS', description: 'Выборочный запуск тестов')
      booleanParam (description: 'Запуск всех тестов', defaultValue: false ,name: 'ALL_TEST')
   }
   stages {
      stage("Build name"){
         steps {
            script {
               if (env.ALL_TEST == 'false') {
                  currentBuild.displayName = "#${BUILD_NUMBER} : ${TESTS}"
               } else {
                  currentBuild.displayName = "#${BUILD_NUMBER} : ALL_TEST"
               }
            }
         }
      }
      stage('RUN TESTS') {
         steps {
            script {
               if (env.ALL_TEST == 'false') {
                  sh 'pytest -m $TESTS --alluredir reports || true'
               } else {
                  sh 'pytest --alluredir reports || true'
               }
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
