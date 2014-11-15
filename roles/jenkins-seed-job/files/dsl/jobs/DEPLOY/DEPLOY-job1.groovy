job {
    name 'DEPLOY-job1'
    parameters {
        stringParam("PARAM1")
        stringParam("PARAM2")
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
            trigger('DEPLOY-job2') {
                currentBuild()
            }
        }

    }
}