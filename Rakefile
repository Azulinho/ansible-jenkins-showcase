
vagrant_plugins = ['ansible',
                   'vagrant-cachier',
                   'vagrant-hostmanager',
                   'vagrant-triggers',
                   'vagrant-hostsupdater']

task :default => ['setup', 'vagrant_up'] do

end

desc "let me sort out all the goodies you may need"
task :setup do
  vagrant_plugins.each do |plugin|
    system("vagrant plugin install #{ plugin }")
    end
end

desc "power up the vagrant boxes"
task :vagrant_up do
  ['zabbix', 'jenkins'].each do |box|
    system("vagrant up #{ box } --no-provision")
  end
  system("vagrant provision jenkins")
end
