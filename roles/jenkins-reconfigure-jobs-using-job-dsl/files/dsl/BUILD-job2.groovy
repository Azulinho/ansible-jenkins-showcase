job {
    name 'DSL_BUILD-job2'
    scm {
        git('https://github.com/facebook/AsyncDisplayKit.git')
    }
    triggers {
        scm('*/15 * * * *')
    }
    steps {
        downstreamParameterized {
            trigger('DSL_DEPLOY-job1') {
                currentBuild()
            }
        }
    }
}