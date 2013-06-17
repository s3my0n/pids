PIDS: Personal Intrusion Detection System
===============================

Description
----------------

Constantly monitors /proc files to identify any possible network intrusion attempts.

Features:

* Port scan identification
* Alert on new connections from or to unknown hosts by running processes
* Alert on new processes that spawn connections from or to unknown hosts
* Configuration file settings
* Monitor/Ignore specific processes
* Whitelist/Blacklist IP addresses

Architecture:
-----------------

### Configuration File:

Using ConfigParser module to parse INI configuration file.

Example config:

    [processes-monitor]
    ftpd
    sshd

    [processes-ignore]
    firefox
    chrome
    opera

    [whitelist-ips]
    127.0.0.1

    [blacklist-ips]
    8.8.8.8

### Function prototypes

main prototype:

    main:
        config = read("pids.ini")
        if config:
            options = parseConfig(config)
        else:
            options = default_options
        startMonitor(options)



ParseConfig prototype:

    parseConfig:

        for each in [process-monitor]: (if empty monitor all processes)
            monitor this process
        for each in [process-ignore]:
            don't monitor this process
        for each in [whitelist-ips]:
            do not alert for the ip
        for each in [blacklist-ips]: (if empty alert on all non-whitelisted)
            alert for this ip

## Remark

Each new TCP processes will have a unique ID that will be stored in a dictionary.    

    monitoredProcesses = {id: [user, lhost, lport, rhost, rport, tcp_state, pid, exe_name]}
