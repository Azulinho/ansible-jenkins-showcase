import unittest
import os
from inventory import Inventory
import requests_mock

class InventoryUnitTests(unittest.TestCase):

    def setUp(self):
        with requests_mock.Mocker() as m:
            m.register_uri('POST', 'https://api.terminal.com/v0.1/list_terminals', json={"terminals":[]})
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
        with requests_mock.Mocker() as m:
            m.register_uri('POST', 'https://api.terminal.com/v0.1/list_terminals', json={"terminals":[]})
            self.inventory.gather_list_of_terminals()
            self.assertEqual(self.inventory.hosts, [])

    def test_get_list_of_hostgroups_returns_array_object(self):
        self.inventory.hosts = [{'custom_data': 'hostgroup1'}]
        self.inventory.get_list_of_hostgroups()
        self.assertEqual(self.inventory.hostgroups, ['hostgroup1'])

    def test_get_vm_details_returns_hash_object(self):
        self.inventory.hosts = [{'name': 'host1'}]
        vm = self.inventory.get_vm_details('host1')
        self.assertEqual(vm, {'name': 'host1'})

    def test_get_hosts_in_hostgroup_returns_array_object(self):
        self.inventory.hosts = [{'name': 'host1', 'custom_data': 'hostgroup1'}]
        host_list = self.inventory.get_hosts_in_hostgroup('hostgroup1')
        self.assertEqual(host_list, ['host1'])

    #def test_build_inventory_response_returns_json(self):
        #self.assertEqual(True, False)

    def test_build_inventory_list_response(self):
        self.inventory.hosts = [{'name': 'host1', 'custom_data': 'hostgroup1'}]
        #with requests_mock.Mocker() as m:
            #m.register_uri('POST', 'https://api.terminal.com/v0.1/list_terminals', json={"terminals":[]})
        expected_response = {
                                "hostgroup1": {
                                    "hosts": [
                                        "host1"
                                    ]
                                },
                                "local": [
                                    "127.0.0.1"
                                ],
                            }
        self.assertEqual(True, False)



if __name__ == "__main__":

    unittest.main()
