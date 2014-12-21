This is an example of how Ansible can be used in an *infrastructure as code environment*,
where all your deployment and configuration data resides in one of more GIT repositories, and the whole environment could be rebuilt from scratch at any time.

The configuration for the different jenkins jobs, pipelines, views,
as well as the complete zabbix setup (including the monitored items) are all set in [group_vars/all.yaml](https://github.com/Azulinho/ansible-jenkins-showcase/group_vars/all.yaml) at the root of this repository:

![configuration](https://github.com/Azulinho/ansible-jenkins-showcase/raw/master/videos/part0.gif)

This repo contains a demo of how ansible can be used to deploy and configure Continous Delivery pipelines using
a jenkins box.

It shows how different libraries can be used with ansible to deploy and update plugins, jobs, view, pipelines:

* python jenkins-job-builder
* groovy jenkins job DSL
* jinja2 XML templating


The following roles are used in this demo,

* Azulinho.azulinho-ansible
* Azulinho.azulinho-apache
* Azulinho.azulinho-devel-packages
* Azulinho.azulinho-git
* Azulinho.azulinho-google-dns
* Azulinho.azulinho-java-openjdk-jdk
* Azulinho.azulinho-jenkins-job-builder
* Azulinho.azulinho-jenkins-kick-pipelines
* Azulinho.azulinho-jenkins-plugins
* Azulinho.azulinho-jenkins-reconfigure-jobs-using-jinja2
* Azulinho.azulinho-jenkins-reconfigure-jobs-using-job-builder
* Azulinho.azulinho-jenkins-reconfigure-jobs-using-job-dsl
* Azulinho.azulinho-jenkins-server
* Azulinho.azulinho-mysql-server
* Azulinho.azulinho-python27
* Azulinho.azulinho-ssh-keys
* Azulinho.azulinho-yum-plugin-versionlock
* Azulinho.azulinho-yum-repo-epel
* Azulinho.azulinho-yum-repo-jenkins
* Azulinho.azulinho-yum-repo-rpmforge
* Azulinho.azulinho-zabbix-agent
* Azulinho.azulinho-zabbix-checks
* Azulinho.azulinho-zabbix-server
* joshualund.ruby-2_1
* joshualund.ruby-common


Simply run:

    rake

![vagrant_up](https://github.com/Azulinho/ansible-jenkins-showcase/raw/master/videos/part1.gif)

and then connect to http://jenkins:8080

you should see a fully deployed, configured jenkins with two pipelines and a series of jobs.

The second pipeline PIPELINE2 should be automatically initiated by an Ansible task,
this pipeline executes a job *jinja2_deploy_zabbix* with provisions and configures a zabbix server using an Ansible playbook.
Then another job *jinja2_zabbix_checks* will populate the zabbix server with templates, hosts, and items.
Upon completion the Zabbix server will be configured to monitor itself as well as the Jenkins box which provisioned the Zabbix Server.


![boxes_up](https://github.com/Azulinho/ansible-jenkins-showcase/raw/master/videos/part2.gif)

