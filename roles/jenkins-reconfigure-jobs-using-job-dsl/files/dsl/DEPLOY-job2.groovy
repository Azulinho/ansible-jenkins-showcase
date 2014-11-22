job {
    name 'DSL_DEPLOY-job2'
    steps {
        shell("echo lixo")
    }
    deliveryPipelineConfiguration("Stage 1", "Task 2")
    publishers {
        downstreamParameterized {
            trigger('DSL_DEPLOY-job3') {
                currentBuild()
            }
        }
    }
}