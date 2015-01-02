
vagrant_plugins = { 'ansible' => '0.2.0' ,
                    'vagrant-hostmanager' => '1.5.0',
                    'vagrant-triggers' => '0.4.3',
                    'vagrant-cachier' => '1.1.0',
                    'vagrant-lxc' => '1.0.1',
                    'vagrant-hostsupdater' => '0.0.11'}

ansible_roles = [
  'Azulinho.azulinho-ansible',
  'Azulinho.azulinho-apache',
  'Azulinho.azulinho-google-dns',
  'Azulinho.azulinho-git',
  'Azulinho.azulinho-jenkins-kick-pipelines',
  'Azulinho.azulinho-jenkins-plugins',
  'Azulinho.azulinho-yum-repo-epel',
  'Azulinho.azulinho-java-openjdk-jdk',
  'Azulinho.azulinho-yum-repo-jenkins',
  'Azulinho.azulinho-yum-plugin-versionlock',
  'Azulinho.azulinho-jenkins-reconfigure-jobs-using-jinja2',
  'Azulinho.azulinho-jenkins-reconfigure-jobs-using-job-builder',
  'Azulinho.azulinho-jenkins-reconfigure-jobs-using-job-dsl',
  'Azulinho.azulinho-jenkins-server',
  'Azulinho.azulinho-mysql-server',
  'Azulinho.azulinho-python27',
  'Azulinho.azulinho-ssh-keys',
  'joshualund.ruby-2_1',
  'joshualund.ruby-common',
  'Azulinho.azulinho-zabbix-agent',
  'Azulinho.azulinho-zabbix-checks',
  'Azulinho.azulinho-zabbix-server',
]

task :default => ['setup', 'vagrant_up'] do

end

desc "let me sort out all the goodies you may need"
task :setup do
  plugins_installed = `vagrant plugin list`
  vagrant_plugins.each_pair do |name, version|
    unless plugins_installed =~ /.*#{ name }.*#{version}.*/
      system("vagrant plugin install #{ name } --plugin-version #{ version }")
    end
  end
  ansible_roles.each do |role|
    unless Dir.exists?("roles/#{role}")
      system("ansible-galaxy install #{ role } -p ./roles --force ")
    end
  end
end

desc "download all the ansible roles"
task :galaxy_install do
  ansible_roles.each do |role|
    unless Dir.exists?("roles/#{role}")
      system("ansible-galaxy install #{ role } -p ./roles --force ")
    end
  end
end


desc "power up the vagrant boxes"
task :vagrant_up do
  ['zabbix', 'jenkins'].each do |box|
    system("vagrant up #{ box } --no-provision")
  end
  system("vagrant provision jenkins")
end

