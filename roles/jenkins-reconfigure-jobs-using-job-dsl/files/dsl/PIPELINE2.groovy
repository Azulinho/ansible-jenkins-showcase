view(type: BuildPipelineView) {
    name('PIPELINE2')
    filterBuildQueue()
    filterExecutors()
    title('Deployment Pipeline 2')
    displayedBuilds(5)
    selectedJob('jinja2_deploy_job1')
    alwaysAllowManualTrigger()
    showPipelineParameters()
    refreshFrequency(60)
}