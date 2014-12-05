This repo contains a demo of how ansible can be used to deploy and configure Continous Delivery pipelines using
a jenkins box.

It shows how different libraries can be used with ansible to deploy and update plugins, jobs, view, pipelines:

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

![vagrant_up](https://github.com/Azulinho/ansible-jenkins-showcase/raw/master/videos/part1.gif)

and then connect to http://jenkins:8080

you should see a fully deployed, configured jenkins with two pipelines and a series of jobs.

The second pipeline PIPELINE2 should be automatically initiated by an Ansible task, this pipeline executes a job *jinja2_deploy_zabbix* with provisions and configures a zabbix server using an Ansible playbook.
Upon completion the Zabbix server will be configured to monitor itself as well as the Jenkins box which provisioned the Zabbix Server.


![boxes_up](https://github.com/Azulinho/ansible-jenkins-showcase/raw/master/videos/part2.gif)


This is an example of how Ansible can be used in an infrastructure as code environment, where all your deployment and configuration data resides in one of more GIT repositories, and the whole environment could be rebuilt from scratch at any time.


The configuration for the different jenkins jobs, pipelines, views, as well as the complete zabbix setup (including the monitored items) are all set in group_vars/all at the root of this repository:

![configuration](https://github.com/Azulinho/ansible-jenkins-showcase/raw/master/videos/part0.gif)