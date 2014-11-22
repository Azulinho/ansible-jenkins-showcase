job {
    name 'DSL_DEPLOY-job1'
    parameters {
        stringParam("PARAM1", "default1")
        stringParam("PARAM2", "default2")
    }
    deliveryPipelineConfiguration("Stage 1", "Task 1")

    configure {
        (it / 'blockBuildWhenUpstreamBuilding').setValue('true')
        (it / 'blockBuildWhenDownstreamBuilding').setValue('true')
    }

    configure {

        it / 'properties' / 'hudson.plugins.throttleconcurrents.ThrottleJobProperty' {
            maxConcurrentPerNode(0)
            maxConcurrentTotal(1)
            throttleEnabled(true)
            throttleOption('category')
            categories('Stage 1')
        }
    }


    steps {
        shell("echo DEPLOY 1")
    }
    publishers {
        downstreamParameterized {
            trigger('DSL_DEPLOY-job2') {
                currentBuild()
            }
        }

    }
}