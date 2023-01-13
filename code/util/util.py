import platform

def get_os():
    """Get the os of the system this is running on -- used to decide the browser image to run on"""
    platform_decoder = {'linux': 'linux', 'windows': 'windows', 'darwin': 'mac'}
    platform_system = platform.system().lower()
    system = platform_decoder.get(platform_system, False)
    return system

def get_os_seperator():
    """Get the file seperator used for this os"""
    seperators = {'mac': '/', 'linux': '/', 'windows': '\''}
    return seperators.get(get_os(), '?')