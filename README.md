This repo contains a demo of how ansible can be used to deploy and configure
a jenkins box.

it showcases integration with a few different libraries to deploy and update plugins, jobs, view, pipelines:

* python jenkins-job-builder
* groovy jenkins job DSL
* jinja2 XML templating


The following roles are used in this demo,

* yum-tools
* yum-repo-centos-release-SCL
* yum-repo-epel
* yum-repo-jenkins
* yum-repo-rpmforge
* python27
* python-pip
* git
* java-openjdk-jdk
* jenkins
* jenkins-job-builder
* jenkins-reconfigure-jobs-using-jinja2
* jenkins-reconfigure-jobs-using-job-builder
* jenkins-reconfigure-jobs-using-job-dsl
* jenkins-kick-pipelines

Simply run:

    rake
    vagrant provision jenkins

and then connect to http://localhost:8080

you should see a fully deployed, configured jenkins with two pipelines and a series of jobs.