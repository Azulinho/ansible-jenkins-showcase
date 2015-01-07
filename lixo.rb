require 'rest_client'
require 'json'
require 'awesome_print'

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

puts "get_snapshot..."
response = RestClient.post 'https://api.terminal.com/v0.1/get_snapshot',
  {
    'snapshot_id' => '2dca905d923d8154c555c5271cbba75927cb3fd705aba1eb9d93cbd59e3ef100'
  }.to_json,
  :content_type => :json, :accept => :json

ap JSON.parse(response)

puts "start_snapshot..."
response = RestClient.post 'https://api.terminal.com/v0.1/start_snapshot',
  {
    'user_token' => ENV['TERMINAL_API_TOKEN'],
    'access_token' => ENV['TERMINAL_ACCESS_TOKEN'],
    'snapshot_id' => '2dca905d923d8154c555c5271cbba75927cb3fd705aba1eb9d93cbd59e3ef100',
    'cpu' => '2 (max)',
    'ram' => 256,
    'temporary' => true,
    'name' => "jenkins",
    'autopause' => true,
    'startup_script' => "echo hi",
    'custom_data' => "jenkins"
  }.to_json,
  :content_type => :json, :accept => :json

jenkins = JSON.parse(response)
ap jenkins




puts "get_snapshot..."
response = RestClient.post 'https://api.terminal.com/v0.1/get_snapshot',
  {
    'user_token' => ENV['TERMINAL_API_TOKEN'],
    'access_token' => ENV['TERMINAL_ACCESS_TOKEN'],
    'container_key' => /.*::.*@.*:create:.*::(.*)/.match(jenkins['request_id'])[1],
  }.to_json,
  :content_type => :json, :accept => :json

puts JSON.parse(response)


puts "start_snapshot..."
response = RestClient.post 'https://api.terminal.com/v0.1/start_snapshot',
  {
    'user_token' => ENV['TERMINAL_API_TOKEN'],
    'access_token' => ENV['TERMINAL_ACCESS_TOKEN'],
    'snapshot_id' => '2dca905d923d8154c555c5271cbba75927cb3fd705aba1eb9d93cbd59e3ef100',
    'cpu' => '2 (max)',
    'ram' => 256,
    'temporary' => true,
    'name' => "zabbix",
    'autopause' => true,
    'startup_script' => "echo hi",
    'custom_data' => "jenkins"
  }.to_json,
  :content_type => :json, :accept => :json

zabbix = JSON.parse(response)
ap zabbix

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
  ap vm
  vms["#{vm[name]}"] = vm
end

puts "printing out vms..."
ap vms


puts "add_terminal_links..."
response = RestClient.post 'https://api.terminal.com/v0.1/add_terminal_links',
  {
    'container_key' => /.*::.*@.*:create:.*::(.*)/.match(jenkins['request_id'])[1],
    'user_token' => ENV['TERMINAL_API_TOKEN'],
    'access_token' => ENV['TERMINAL_ACCESS_TOKEN'],
    'links' => [
      {
        "port" => "*",
        "source" => "zabbix"
      }
    ]
  }.to_json,
  :content_type => :json, :accept => :json

ap JSON.parse(response)

puts "add_terminal_links..."
response = RestClient.post 'https://api.terminal.com/v0.1/add_terminal_links',
  {
    'container_key' => /.*::.*@.*:create:.*::(.*)/.match(zabbix['request_id'])[1],
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

puts "get_cname_records..."
response = RestClient.post 'https://api.terminal.com/v0.1/get_cname_records',
  {
    'user_token' => ENV['TERMINAL_API_TOKEN'],
    'access_token' => ENV['TERMINAL_ACCESS_TOKEN']
  }.to_json,
  :content_type => :json, :accept => :json

ap JSON.parse(response)
