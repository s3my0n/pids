#!/usr/bin/env python2.7

import ConfigParser
import logging
import optparse
import os.path
import re
import sys

DEF_CONFIG = "./config.ini"

proc_mon = []
proc_ignore = []
white_ips = []
black_ips = []

def parseConf(confPath):
    """
    Parse configuration file and feel variables:
    proc_mon - names of monitoring processes;
    proc_ignore - names of ignoring processes;
    white_ips - list of ignoring IPs;
    black_ips - list of monitoring IPs.
    """
    logging.debug("DEBUG: config file is %s" % confPath)
    if not os.path.isfile(confPath):
        print "File %s doesent exists" % confPath
        exit(1)
    parser = ConfigParser.ConfigParser(allow_no_value = True)
    try:
        parser.read(confPath)
    except Exception as e:
        logging.debug("DEBUG: Exception %s catched" % e.args)
        exit(1)
    opt_lists = {
                "processes-monitor": proc_mon,
                "processes-ignore": proc_ignore,
                "blacklist-ips": black_ips, 
                "whitelist-ips": white_ips,
               }

    for sect in opt_lists.keys():
        try:
            for item in parser.items(sect):
                opt_lists[sect].append(item[0])
        except ConfigParser.NoSectionError:
            logging.debug("DEBUG:exception nosection")
    print opt_lists
    
def parseOptions():
    """
    Parse options and returns pair (options, args)
    where:
    options.config - path to configuration file
    options.daemonize - need to daemonize flag
    options.verbose - verbose flag (Omg, rly?) 
    """
    op = optparse.OptionParser()
    op.add_option("-c", dest="config", default=DEF_CONFIG,
            action = "store", help = "path to config file")
    op.add_option("-D", dest="daemonize", default=False,
            action = "store_true", help = "daemonize process")
    op.add_option("-v", dest="verbose", default=False,
            action = "store_true", help = "programm will be more verbosekk")
    return op.parse_args()

def daemonize():
    """
    daemonize process
    FIXME: Need to use specific module or invent bicycle?;
    """
    pass

def main():
    (options, args) = parseOptions()
    if options.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    parseConf(options.config)
    if options.daemonize:
        daemonize() 

if __name__ == "__main__":
    main()
