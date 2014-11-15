view(type: BuildPipelineView) {
    name('PIPELINE')
    filterBuildQueue()
    filterExecutors()
    title('Deployment Pipeline')
    displayedBuilds(5)
    selectedJob('DEPLOY-job1')
    alwaysAllowManualTrigger()
    showPipelineParameters()
    refreshFrequency(60)
}