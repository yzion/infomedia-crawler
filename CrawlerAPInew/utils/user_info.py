import platform

"""
Get OS name
For linux distributions - return the distribution name
"""


def get_os_name():
    if platform.system() == 'Linux':
        return platform.linux_distribution()[0]

    return platform.system()


"""
Get OS version
"""


def get_os_version(os_name):
    versions = {
        'Ubuntu': platform.linux_distribution()[1],
        'Windows': platform.release(),
        'Darwin': platform.release()  # TODO: check it
    }
    return versions.get(os_name, 'unknown os name')

"""
Get app name
"""


"""
Get run method name
"""