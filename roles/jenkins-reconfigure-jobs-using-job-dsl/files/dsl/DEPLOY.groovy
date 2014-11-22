view(type: ListView) {
    name('DSL_DEPLOY')
    description('All deploy jobs')
    filterBuildQueue()
    filterExecutors()
    jobs {
        regex('DSL_DEPLOY-*')
    }
    columns {
        status()
        weather()
        name()
        lastSuccess()
        lastFailure()
        lastDuration()
        buildButton()
    }
}