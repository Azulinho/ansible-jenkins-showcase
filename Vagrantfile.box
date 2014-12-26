# vi: set ft=ruby :
#

VAGRANTFILE_API_VERSION = '2'

box = 'CENTOS_6.5'
box_url = 'https://github.com/2creatives/vagrant-centos/releases/download/v6.5.3/centos65-x86_64-20140116.box'

boxes = [
  {
    :name => :jenkins,
    :ram => 1512,
    :book => 'jenkins',
    :ip => "2"
  },
  {
    :name => :zabbix,
    :ram => 512,
    :book => 'zabbix',
    :ip => "3"
  },


]

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.hostmanager.enabled      = true
  config.hostmanager.include_offline  = true
  config.hostmanager.manager_host   = true
  config.vm.provision :hostmanager

  if Vagrant.has_plugin?("vagrant-cachier")
      # Configure cached packages to be shared between instances of the same base box.
      # More info on http://fgrehm.viewdocs.io/vagrant-cachier/usage
      config.cache.scope = :box
  end

  boxes.each do |opts|
    config.vm.define opts[:name] do |machine|
      machine.vm.box = box
      machine.vm.box_url = box_url
      machine.vm.hostname = opts[:name]
      machine.vm.network :private_network, ip: "192.168.67.#{opts[:ip]}"


      machine.vm.provider :virtualbox do |virtual|
        virtual.customize ['modifyvm', :id, '--cpus', "2"  ]
        virtual.customize ['modifyvm', :id, '--memory', opts[:ram] ]
        virtual.customize ['modifyvm', :id, '--name', opts[:name].to_s ]
        virtual.customize ['modifyvm', :id, '--natdnsproxy1', "off"]
        virtual.customize ['modifyvm', :id, '--natdnshostresolver1', "off"]
        virtual.customize ['modifyvm', :id, '--usbehci', "off"]
      end

      config.vm.provision :ansible do |ansible|
        if defined? ENV['TAGS']
          ansible.tags = ENV['TAGS']
        end
        if defined? ENV['START_AT_TASK']
          ansible.start_at_task = ENV['START_AT_TASK']
        end

        #ansible.verbose = 'vvv'
        ansible.sudo = true
        ansible.playbook = "vagrant-#{opts[:book]}.yml"
        ansible.inventory_path= 'vagrant'
        ansible.vault_password_file = 'vagrant-vault'
        ansible.limit = opts[:name].to_s

        ansible.extra_vars = {
          'deploy_environment'    => 'vagrant',
        }
      end
    end
  end
end
# -*- mode: ruby -*-
