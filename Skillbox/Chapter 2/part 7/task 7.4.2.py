server_data = {

    "server": {

        "host": "127.0.0.1",

        "port": "10"

    },

    "configuration": {

        "access": "true",

        "login": "Ivan",

        "password": "qwerty"

    }

}

for name, configuration in server_data.items():
    print(name, ':')
    for i_params, data in configuration.items():
        print('\t', i_params, ':', data)