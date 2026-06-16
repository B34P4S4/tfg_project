# Information Disclosure (CWE-200)
function getServerStatus():
    status = {
        "os_version": System.getOSVersion(),
        "internal_ips": System.getInternalNetworkIPs(),
        "debug_mode": true
    }

    # Vulnerable: exposes sensitive system information
    return status