view(type: ListView) {
    name('DEPLOY')
    description('All deploy jobs')
    filterBuildQueue()
    filterExecutors()
    jobs {
        regex('DEPLOY-*')
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