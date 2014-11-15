view(type: ListView) {
    name('BUILD')
    description('All Build jobs')
    filterBuildQueue()
    filterExecutors()
    jobs {
        regex('BUILD-*')
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