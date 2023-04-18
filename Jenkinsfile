pipeline {
   agent {
      label 'wfm-at'
   }
   parameters {
      string ( name: 'TESTS', trim: true, description: 'Введите название тестов')
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
                  sh 'pytest -m $TESTS --alluredir reports/${TESTS} || true'
               } else {
                  sh 'pytest --alluredir reports/ALL_TEST || true'
               }
            }
         }
      }
      stage('Remove hidden tests') {
         steps {
            script {
               if (env.ALL_TEST == 'false') {
                  sh """
                     grep -rl '"status": "skipped"' reports/${TESTS} | xargs rm -rf
                  """
               } else {
                  sh """
                     grep -rl '"status": "skipped"' reports/ALL_TEST | xargs rm -rf
                  """
               }
            }
         }
      }
      stage('Reports') {
         steps {
            script {
               if (env.ALL_TEST == 'false') {
                  allure([
      	         includeProperties: false,
      	         jdk: '',
      	         properties: [],
      	         reportBuildPolicy: 'ALWAYS',
      	         results: [[path: "reports/${TESTS}"]]
    	            ])
               } else {
                  allure([
      	         includeProperties: false,
      	         jdk: '',
      	         properties: [],
      	         reportBuildPolicy: 'ALWAYS',
      	         results: [[path: "reports/ALL_TEST"]]
    	            ])
               }
            }
  	      }
      }
   }
}
