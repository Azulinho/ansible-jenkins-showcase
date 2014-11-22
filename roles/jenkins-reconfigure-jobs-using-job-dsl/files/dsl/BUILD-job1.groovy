job {
    name 'DSL_BUILD-job1'
    parameters {
        stringParam("myParameter1", "default1")
    }
    scm {
        git('https://github.com/Azulinho/bristol-devops-jenkins-jobs.git')
    }
    triggers {
        scm('*/15 * * * *')
    }
    steps {
        shell('echo hello')
    }
    publishers {
        downstreamParameterized {
            trigger('DSL_DEPLOY-job1') {
                currentBuild()
            }
        }
    }
}