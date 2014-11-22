view(type: BuildPipelineView) {
    name('PIPELINE1')
    filterBuildQueue()
    filterExecutors()
    title('Deployment Pipeline 1')
    displayedBuilds(5)
    selectedJob('DSL_DEPLOY-job1')
    alwaysAllowManualTrigger()
    showPipelineParameters()
    refreshFrequency(60)
}