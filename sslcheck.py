#Third party imports
from sslyze import server_connectivity
from sslyze import synchronous_scanner
from sslyze.plugins import openssl_cipher_suites_plugin as cipher

#Python imports

#Local imports

default_port = 443

# DEPRECATED (SSLYZE = 2.1.4) UPGRADE METHODS TO 3.0.1

def syn_scanner(host, port, command_scanner):
    server_connection = server_connectivity.ServerConnectivityTester(
        hostname=host,
        port=port
        )
    connection = server_connection.perform()
    syn_scanner = synchronous_scanner.SynchronousScanner()
    scan_result = syn_scanner.run_scan_command(connection, command_scanner)
    return True if len(scan_result.accepted_cipher_list) > 0 else False

def check_ssl2(host : str, port : int = default_port):
    return syn_scanner(host, port, cipher.Sslv20ScanCommand())

def check_ssl3(host : str, port : int = default_port):
    return syn_scanner(host, port, cipher.Sslv30ScanCommand())

def check_tls10(host : str, port : int = default_port):
    return syn_scanner(host, port, cipher.Tlsv10ScanCommand())

def check_tls11(host : str, port : int = default_port):
    return syn_scanner(host, port, cipher.Tlsv11ScanCommand())

def check_tls12(host : str, port : int = default_port):
    return syn_scanner(host, port, cipher.Tlsv12ScanCommand())

def check_tls13(host : str, port : int = default_port):
    return syn_scanner(host, port, cipher.Tlsv13ScanCommand())

def all_scans(host : str, port : int = default_port):
    dict_checks = {}
    dict_checks['ssl2'] = check_ssl2(host, port)
    dict_checks['ssl3'] = check_ssl3(host, port)
    dict_checks['tls10'] = check_tls10(host, port)
    dict_checks['tls11'] = check_tls11(host, port)
    dict_checks['tls12'] = check_tls12(host, port)
    dict_checks['tls13'] = check_tls13(host, port)
    return dict_checks

def few_scans(host : str, port : int = default_port):
    dict_checks = {}
    dict_checks['ssl3'] = check_ssl3(host, port)
    dict_checks['tls10'] = check_tls10(host, port)
    dict_checks['tls11'] = check_tls11(host, port)
    return dict_checks
