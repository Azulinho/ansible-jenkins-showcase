
vagrant_plugins = { 'ansible' => '0.2.0' ,
                    'vagrant-cachier' => '1.1.0',
                    'vagrant-hostmanager' => '1.5.0',
                    'vagrant-triggers' => '0.4.3',
                    'vagrant-hostsupdater' => '0.0.11'}

task :default => ['setup', 'vagrant_up'] do

end

desc "let me sort out all the goodies you may need"
task :setup do
  vagrant_plugins.each_pair do |name, version|
    system("vagrant plugin install #{ name } --plugin-version #{ version }")
    end
end

desc "power up the vagrant boxes"
task :vagrant_up do
  ['zabbix', 'jenkins'].each do |box|
    system("vagrant up #{ box } --no-provision")
  end
  system("vagrant provision jenkins")
end

