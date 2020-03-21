import random

import requests

URL_PREFIX = 'http://localhost:8088/cft/api/v1/'


def mock_io_models(count):
    for i in range(count):
        result = requests.post(url=URL_PREFIX + 'io',
                               data={'io_name': '%sK' % i,
                                     'tool_name': random.choice(['vdbench', 'uniblkIO', 'unifsIO']),
                                     'io_params': "{'read':'%s', 'write': '%s'}" % (i, i)})
        print(result.status_code)


def mock_his_io_models(count):
    for i in range(count):
        result = requests.post(url=URL_PREFIX + 'io/his_io',
                               data={'io_name': '%sK' % i,
                                     'tool_name': random.choice(['vdbench', 'uniblkIO', 'unifsIO']),
                                     'device_model': random.choice(['5500 V5', '5600 V5', '5800 V5']),
                                     'device_version': random.choice(
                                         ['V500R007C00B031', 'V500R007C00B032', 'V500R007C00B033']),
                                     'script_name': random.choice(['test1', 'test2', 'test3']),
                                     'date': random.choice(
                                         ['2020-02-02 22:22:22', '2020-02-02 11:11:11', '2020-02-02 12:12:12']),
                                     'result': 'true',
                                     'io_params': "{'read':'%s', 'write': '%s'}" % (i, i)})
        print(result.status_code)


def mock_his_script_data(count):
    for i in range(count):
        result = requests.post(url=URL_PREFIX + 'script/his_script',
                               data={'script_name': 'TEST%d' % i,
                                     'script_path': random.choice(['/TETS1', '/TETS2', '/TETS3']),
                                     'script_params"': random.choice(['5500 V5', '5600 V5', '5800 V5']),
                                     'classification': random.choice(['NAS', 'SAN', 'SYSTEM']),
                                     'device_model': random.choice(['5500 V5', '5600 V5', '5800 V5']),
                                     'device_version': random.choice(
                                         ['V500R007C00B031', 'V500R007C00B032', 'V500R007C00B033']),
                                     'date': random.choice(
                                         ['2020-02-02 22:22:22', '2020-02-02 11:11:11', '2020-02-02 12:12:12']),
                                     'result': 'true',
                                     'script_desc': random.choice(['desc1', 'desc2', 'desc3'])})
        print(result.status_code)


def mock_script_data(count):
    for i in range(count):
        result = requests.post(url=URL_PREFIX + 'script',
                               data={'script_name': 'TEST%d' % i,
                                     'script_path': random.choice(['/TETS1', '/TETS2', '/TETS3']),
                                     'script_params"': random.choice(['5500 V5', '5600 V5', '5800 V5']),
                                     'classification': random.choice(['NAS', 'SAN', 'SYSTEM']),
                                     'script_desc': random.choice(['desc1', 'desc2', 'desc3'])})
        print(result.status_code)


if __name__ == '__main__':
    mock_his_script_data(100)
