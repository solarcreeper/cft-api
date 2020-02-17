import requests

URL_PREFIX = 'http://localhost:8088/cft/api/v1/'


def mock_io_models(count):
    for i in range(count):
        result = requests.post(url=URL_PREFIX + 'io',
                               data={'io_name': '%sK' % i, 'tool_name': 'vdbench',
                                     'io_params': "{'read':'%s', 'write': '%s'}" % (i, i)})
        pass

if __name__ == '__main__':
    mock_io_models(100)
