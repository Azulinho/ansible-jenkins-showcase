#!/usr/bin/env python2

import requests
import json
import os
import operator
# from IPython import embed


class Inventory:

    def __init__(self):
        self.hosts = self.gather_list_of_terminals()
        self.hostgroups = self.get_list_of_hostgroups()

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

        if r.json() is None:
            return []
        else:
            return r.json()['terminals']

    def get_list_of_hostgroups(self):
        hostgroups = []
        for vm in self.hosts:
            hostgroups.append(vm['custom_data'])
        return hostgroups

    def get_vm_details(self, vm_name):
        for vm in self.hosts:
            if vm['name'] == vm_name:
                return(vm)

    def get_hosts_in_hostgroup(self, hostgroup):
        result = []
        for host in self.hosts:
            if host['custom_data'] == hostgroup:
                result.append(host['name'])
        return result

    def produce_inventory(self):
        response = {}
        response['_meta'] = {}
        response['_meta']['hostvars'] = {}
        for hostgroup in self.hostgroups:
            for host in self.get_hosts_in_hostgroup(hostgroup):
                response['_meta']['hostvars'][host] = self.get_vm_details(host)
                response['_meta']['hostvars'][host]['ansible_ssh_host'] = self.get_vm_details(host)['subdomain'] + '.terminal.com'

        for hostgroup in self.hostgroups:
            response[hostgroup] = {"hosts": self.get_hosts_in_hostgroup(hostgroup) }
        response['local'] = ["127.0.0.1"]
        #return sorted(response.items(), key=operator.itemgetter(0))
        return json.dumps(sorted(response.items(),
                                 key=operator.itemgetter(0)),
                          indent=4)


if __name__ == "__main__":
    x = Inventory()
    print(x.produce_inventory())
