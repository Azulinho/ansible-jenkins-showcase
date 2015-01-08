import requests
import json
import os

class Inventory:

    def __init__(self):
        self.hosts = {}
        self.hostgroups = []

    def check_for_terminal_credentials(self):
        if "TERMINAL_API_TOKEN" in os.environ:
            return True
        else:
            return False

    def gather_list_of_terminals(self):
        url = "https://api.terminal.com/v0.1/list_terminals"

        payload = {'user_token': os.environ['TERMINAL_API_TOKEN'],
                'access_token': os.environ['TERMINAL_ACCESS_TOKEN']}

        headers = {'content-type': 'application/json'}

        r = requests.post(url,
                        data=json.dumps(payload),
                        headers=headers)

        self.hosts = r.json()['terminals']


    def get_list_of_hostgroups(self):
        for vm in self.hosts:
            self.hostgroups.append(vm['custom_data'])


    def get_vm_details(self,vm_name):
        for vm in self.hosts:
            if vm['name'] == vm_name:
                return(vm)

    def get_hosts_in_hostgroup(self, hostgroup):
        result = []
        for host in self.hosts:
            if host['custom_data'] == hostgroup:
                result.append(host['name'])
        return result


    #def build_inventory_response(self,list_of_terminals):
        #hostgroups = get_list_of_hostgroups(list_of_terminals)
        #for hostgroup in hostgroups:
            #hosts = get_hosts_in_hostgroup(list_of_terminals, hostgroup)

        #response = Template("
            #{% for hostgroup in hostgroups %}
                #{"{{hostgroup}}": {"hosts" : [{% for host in hosts[hostgroup] %}
                                            #"{{ host }}",
                                            #{% endfor %}
                                            #]
                                #},
            #{% endfor %}
                #}")

    #list_of_terminals = gather_list_of_terminals
    #build_inventory_response(list_of_terminals)
