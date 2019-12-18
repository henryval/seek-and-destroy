#Third party imports
import tlslite

#Python imports
import socket
from typing import Tuple
from contextlib import suppress

#Local imports

default_port = 443

class connection:
    def __init__(self, host: str, port: int, min_version: Tuple[int, int], max_version: Tuple[int, int]):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        connection = tlslite.TLSConnection(sock)
        connection.ignoreAbruptClose = True
        settings = tlslite.HandshakeSettings()
        settings.minVersion = min_version
        settings.maxVersion = max_version
        settings.sendFallbackSCSV = False
        settings.use_heartbeat_extension = False
        connection.handshakeClientCert(settings=settings)
        try:
            connection
        finally:
            connection.close()
    def __enter__(self):
        return self    
    def __exit__(self, type, value, traceback):
        return isinstance(value, TypeError)

def check_ssl_3(host : str, port : int = default_port):
    enabled = False
    with suppress(tlslite.errors.TLSRemoteAlert,
                  tlslite.errors.TLSAbruptCloseError,
                  tlslite.errors.TLSLocalAlert):
        with connection(host, port, min_version=(3, 0), max_version=(3, 0)):
            enabled = True
    return enabled

def check_tls_10(host : str, port : int = default_port):
    enabled = False
    with suppress(tlslite.errors.TLSRemoteAlert,
                  tlslite.errors.TLSAbruptCloseError,
                  tlslite.errors.TLSLocalAlert):
        with connection(host, port, min_version=(3, 1), max_version=(3, 1)):
            enabled = True
    return enabled

def check_tls_11(host : str, port : int = default_port):
    enabled = False
    with suppress(tlslite.errors.TLSRemoteAlert,
                  tlslite.errors.TLSAbruptCloseError,
                  tlslite.errors.TLSLocalAlert):
        with connection(host, port, min_version=(3, 2), max_version=(3, 2)):
            enabled = True
    return enabled

def check_tls_12(host : str, port : int = default_port):
    enabled = False
    with suppress(tlslite.errors.TLSRemoteAlert,
                  tlslite.errors.TLSAbruptCloseError,
                  tlslite.errors.TLSLocalAlert):
        with connection(host, port, min_version=(3, 3), max_version=(3, 3)):
            enabled = True
    return enabled

def all_checks(host : str, port : int = default_port):
    dict_checks = {}
    dict_checks['ssl3'] = check_ssl_3(host, port)
    dict_checks['tls1'] = check_tls_10(host, port)
    dict_checks['tls11'] = check_tls_11(host, port)
    dict_checks['tls12'] = check_tls_12(host, port)
    return dict_checks
