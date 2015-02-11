import unittest
import os
from inventory import Inventory
import requests_mock
import json
import operator

class InventoryUnitTests(unittest.TestCase):

    def setUp(self):
        with requests_mock.Mocker() as m:
            m.register_uri('POST', 'https://api.terminal.com/v0.1/list_terminals',
                           json={
                               "terminals":[
                                   {"cpu":"2 (max)",
                                    "ram":"256",
                                    "diskspace":"10",
                                    "name":"jenkins",
                                    "snapshot_id":"2dca905d923d8154c555c5271cbba75927cb3fd705aba1eb9d93cbd59e3ef100",
                                    "temporary":"false",
                                    "custom_data":"jenkins_servers",
                                    "status":"running",
                                    "allow_spot":"false",
                                    "container_key":"909f97cd-88c2-449e-89fc-37a4afd42a24",
                                    "subdomain":"azul45",
                                    "container_ip":"240.5.144.135",
                                    "creation_time":"1420753333931"},
                                   {"cpu":"2 (max)",
                                    "ram":"256",
                                    "diskspace":"10",
                                    "name":"zabbix",
                                    "snapshot_id":"2dca905d923d8154c555c5271cbba75927cb3fd705aba1eb9d93cbd59e3ef100",
                                    "temporary":"false",
                                    "custom_data":"zabbix_servers",
                                    "status":"running",
                                    "allow_spot":"false",
                                    "container_key":"c76d268b-fcfe-4f22-8751-5d2cdd0580d8",
                                    "subdomain":"azul46",
                                    "container_ip":"240.5.144.136",
                                    "creation_time":"1420753335619"}]})
            os.environ['TERMINAL_API_TOKEN'] = 'XXXXXXXXXXXXXXXX'
            os.environ['TERMINAL_ACCESS_TOKEN'] = 'XXXXXXXXXXXXX'
            self.inventory = Inventory()

    def unset_environment_variable(self,var):
        if var in os.environ: os.environ.pop(var)

    def test_validates_check_for_terminal_credentials_fails_when_not_set(self):
        self.unset_environment_variable('TERMINAL_API_TOKEN')
        self.unset_environment_variable('TERMINAL_ACCESS_TOKEN')
        self.assertEqual(self.inventory.check_for_terminal_credentials(), False)

    def test_validates_check_for_terminal_credentials_passes_when_set(self):
        os.environ['TERMINAL_API_TOKEN'] = 'XXXXXXXXXXXXXXXX'
        os.environ['TERMINAL_ACCESS_TOKEN'] = 'XXXXXXXXXXXXX'
        self.assertEqual(self.inventory.check_for_terminal_credentials(), True)

    def test_gather_list_of_hosts_returns_json_object(self):
        response = [{"cpu":"2 (max)",
                "ram":"256",
                "diskspace":"10",
                "name":"jenkins",
                "snapshot_id":"2dca905d923d8154c555c5271cbba75927cb3fd705aba1eb9d93cbd59e3ef100",
                "temporary":"false",
                "custom_data":"jenkins_servers",
                "status":"running",
                "allow_spot":"false",
                "container_key":"909f97cd-88c2-449e-89fc-37a4afd42a24",
                "subdomain":"azul45",
                "container_ip":"240.5.144.135",
                "creation_time":"1420753333931"},
                {"cpu":"2 (max)",
                "ram":"256",
                "diskspace":"10",
                "name":"zabbix",
                "snapshot_id":"2dca905d923d8154c555c5271cbba75927cb3fd705aba1eb9d93cbd59e3ef100",
                "temporary":"false",
                "custom_data":"zabbix_servers",
                "status":"running",
                "allow_spot":"false",
                "container_key":"c76d268b-fcfe-4f22-8751-5d2cdd0580d8",
                "subdomain":"azul46",
                "container_ip":"240.5.144.136",
                "creation_time":"1420753335619"}]
        self.assertEqual(self.inventory.hosts, response)

    def test_get_list_of_hostgroups_returns_array_object(self):
        self.assertEqual(self.inventory.hostgroups,
                ['jenkins_servers', 'zabbix_servers'])

    def test_get_vm_details_returns_hash_object(self):
        self.inventory.hosts = [{'name': 'host1'}]
        vm = self.inventory.get_vm_details('host1')
        self.assertEqual(vm, {'name': 'host1'})

    def test_build_inventory_list_response(self):
            response = self.inventory.produce_inventory()
            expected_response = {
                "_meta": {
                    "hostvars": {
                        "jenkins": {
                            "status": "running",
                            "ansible_ssh_host": "azul45.terminal.com",
                            "temporary": "false",
                            "name": "jenkins",
                            "diskspace": "10",
                            "custom_data": "jenkins_servers",
                            "ram": "256",
                            "creation_time":"1420753333931",
                            "container_key":"909f97cd-88c2-449e-89fc-37a4afd42a24",
                            "snapshot_id":"2dca905d923d8154c555c5271cbba75927cb3fd705aba1eb9d93cbd59e3ef100",
                            "subdomain": "azul45",
                            "allow_spot": "false",
                            "cpu": "2 (max)",
                            "container_ip": "240.5.144.135"
                        },
                        "zabbix": {
                            "status": "running",
                            "ansible_ssh_host": "azul46.terminal.com",
                            "temporary": "false",
                            "name": "zabbix",
                            "diskspace": "10",
                            "custom_data": "zabbix_servers",
                            "ram": "256",
                            "creation_time":"1420753335619",
                            "container_key":"c76d268b-fcfe-4f22-8751-5d2cdd0580d8",
                            "snapshot_id":"2dca905d923d8154c555c5271cbba75927cb3fd705aba1eb9d93cbd59e3ef100",
                            "subdomain": "azul46",
                            "allow_spot": "false",
                            "cpu": "2 (max)",
                            "container_ip":"240.5.144.136"
                        }
                    }
                },
                "jenkins_servers": {
                    "hosts": [
                        "jenkins"
                    ]
                },
                "zabbix_servers": {
                    "hosts": [
                        "zabbix"
                    ]
                },
                "local": [
                    "127.0.0.1"
                ]
            }
            self.assertEqual(json.dumps(sorted(expected_response.items(),
                                    key=operator.itemgetter(0)), indent=4), response)



if __name__ == "__main__":

    unittest.main()
