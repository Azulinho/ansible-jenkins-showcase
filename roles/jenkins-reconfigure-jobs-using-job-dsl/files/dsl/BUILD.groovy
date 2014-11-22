view(type: ListView) {
    name('DSL_BUILD')
    description('All Build jobs')
    filterBuildQueue()
    filterExecutors()
    jobs {
        regex('DSL_BUILD-*')
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