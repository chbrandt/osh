"""
Wrapper for sh to interface Docker containers seemlessly
"""
 # Stuff from versioneer
from . import _version
__version__ = _version.get_versions()['version']

from . import _log as log
from ._sh import Osh


def init(container:str, mappings=None, name:str=None):
    """
    Return a shell for docker 'container' with 'mappings' set

    If no mappings are given, osh will map all volumes defined for 'container'.
    You can give a 'name' for this instance of osh.

    Input:
        container: str
            Name of the container
        mappings: list or dict
            List of length-2 tuples with (host,container) volumes
            Ex: [('/host/path/','/container/path')]
            Dict of command arguments to length-2 tuples
            Ex: {'option': ('/host/path','/container/path')}
        name: str
            Name for this instance of Osh (placeholder for planned future)

    Output:
        Osh instance
    """
    sh = Osh(name)
    sh.set_docker(container, mappings, inspect=True)
    return sh
