require 'rest_client'
require 'json'
require 'awesome_print'


def list_public_snapshots
  puts "list_public_snapshots..."
  response = RestClient.post 'https://api.terminal.com/v0.1/list_public_snapshots',
    {
      'tag'     => 'centos',
      'user'    => 'terminal',
      'title'   => 'Official Centos 6',
      'page'    => 0,
      'perPage' => 10,
      'sortby'  => 'popularity' }.to_json,
    :content_type => :json, :accept => :json

  ap JSON.parse(response)
end

def get_snapshot_centos
  puts "get_snapshot centos..."
  response = RestClient.post 'https://api.terminal.com/v0.1/get_snapshot',
    {
      'snapshot_id' => '2dca905d923d8154c555c5271cbba75927cb3fd705aba1eb9d93cbd59e3ef100'
    }.to_json,
    :content_type => :json, :accept => :json

  ap JSON.parse(response)
end

def start_snapshot(name, custom_data)
  puts "start_snapshot..."
  response = RestClient.post 'https://api.terminal.com/v0.1/start_snapshot',
    {
      'user_token' => ENV['TERMINAL_API_TOKEN'],
      'access_token' => ENV['TERMINAL_ACCESS_TOKEN'],
      'snapshot_id' => '2dca905d923d8154c555c5271cbba75927cb3fd705aba1eb9d93cbd59e3ef100',
      'cpu' => '2 (max)',
      'ram' => 256,
      'temporary' => false,
      'name' => name,
      'autopause' => true,
      'startup_script' => "echo hi",
      'custom_data' => custom_data
    }.to_json,
    :content_type => :json, :accept => :json

  jenkins = JSON.parse(response)
  ap jenkins
  return jenkins
end


def get_terminal(vm)
  puts "get_terminal..."
  response = RestClient.post 'https://api.terminal.com/v0.1/get_terminal',
    {
      'user_token' => ENV['TERMINAL_API_TOKEN'],
      'access_token' => ENV['TERMINAL_ACCESS_TOKEN'],
      'container_key' => vm['container_key']
    }.to_json,
    :content_type => :json, :accept => :json

  puts JSON.parse(response)
  return response
end


def list_terminals
  puts "list_terminals..."
  response = RestClient.post 'https://api.terminal.com/v0.1/list_terminals',
    {
      'user_token' => ENV['TERMINAL_API_TOKEN'],
      'access_token' => ENV['TERMINAL_ACCESS_TOKEN']
    }.to_json,
    :content_type => :json, :accept => :json

  puts JSON.parse(response)

  vms = {}
  puts "printing out details from VM"
  JSON.parse(response)['terminals'].each do |vm|
    #ap vm
    vms["#{vm['name']}"] = vm
  end

  puts "printing out vms..."
  ap vms
  return vms
end

def add_terminal_links_jenkins(vm)
  puts "add_terminal_links..."
  response = RestClient.post 'https://api.terminal.com/v0.1/add_terminal_links',
    {
      'container_key' => vm['container_key'],
      'user_token' => ENV['TERMINAL_API_TOKEN'],
      'access_token' => ENV['TERMINAL_ACCESS_TOKEN'],
      'links' => [
        {
          "port" => "*",
          "source" => "jenkins"
        }
      ]
    }.to_json,
    :content_type => :json, :accept => :json

  ap JSON.parse(response)
end

def get_cname_records
  puts "get_cname_records..."
  response = RestClient.post 'https://api.terminal.com/v0.1/get_cname_records',
    {
      'user_token' => ENV['TERMINAL_API_TOKEN'],
      'access_token' => ENV['TERMINAL_ACCESS_TOKEN']
    }.to_json,
    :content_type => :json, :accept => :json

  ap JSON.parse(response)
end

def add_ssh_key(vm, ssh_key)
  puts "add ssh_key..."
  response = RestClient.post 'https://api.terminal.com/v0.1/add_authorized_key_to_terminal',
    {
      'container_key' => vm['container_key'],
      'user_token' => ENV['TERMINAL_API_TOKEN'],
      'access_token' => ENV['TERMINAL_ACCESS_TOKEN'],
      'publicKey' => ssh_key,
    }.to_json,
    :content_type => :json, :accept => :json

  ap JSON.parse(response)

end


vm = start_snapshot('jenkins', 'jenkins_servers')
vm = start_snapshot('zabbix', 'zabbix_servers')
sleep 10
vms = list_terminals
ssh_key = File.read("#{ENV['HOME']}/.ssh/id_rsa.pub")

add_ssh_key(vms['jenkins'], ssh_key)
add_ssh_key(vms['zabbix'], ssh_key)
#add_terminal_links_jenkins(vms['jenkins'])
#get_terminal(vms['jenkins'])
get_cname_records
