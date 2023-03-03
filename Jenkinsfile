pipeline {
   agent {
      label 'wfm-at'
   }
   stages {
      stage("Build image") {
         steps {
    	      catchError {
      	      script {
        	         docker.build("pvp-tests", "-f Dockerfile .")
      	      }
            }
         }
      }
      stage('Pull browser') {
         steps {
            catchError {
               script {
      	         docker.image('selenoid/chrome:110.0').pull()
      	      }
            }
         }
      }
      stage('Run tests') {
         steps {
            catchError {
               script {
          	      docker.image('aerokube/selenoid:1.10.9').withRun('-p 4445:4444 --shm-size=1gb -v /run/docker.sock:/var/run/docker.sock -v $PWD:/etc/selenoid/', '-limit 1') { c ->
              	   docker.image('pvp-tests').inside("--link ${c.id}:selenoid") { sh "python -m pytest --alluredir reports" }
                  }
        	      }
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
      stage('Remove none images') {
         steps {
            sh 'docker images | grep \'^<none>\' | awk \'{ print $3; }\' | xargs docker rmi --force'
         }
      }
   }
}
