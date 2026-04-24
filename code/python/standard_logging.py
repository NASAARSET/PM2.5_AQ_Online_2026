#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 16:40:33 2025

A handy boilerplate logging solution

@author: jjfain
"""

import logging

info_formatter = logging.Formatter(
	fmt='%(asctime)s: %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S'
)

error_formatter = logging.Formatter(
	fmt='%(asctime)s [ERROR] %(message)s\n\t(File: %(filename)s\n\tLine: %(lineno)d',
	datefmt='%Y-%m-%d %H:%M:%S'
)

debug_formatter = logging.Formatter(
	fmt='%(asctime)s [DEBUG] %(message)s (%(module)s)',
	datefmt='%Y-%m-%d %H:%M:%S'
)

warning_formatter = logging.Formatter(
	fmt='%(asctime)s [WARNING] %(message)s (%(module)s)',
	datefmt='%Y-%m-%d %H:%M:%S'
)

# fatal_formatter = logging.Formatter(
# 	fmt='%(asctime)s [FATAL] %(message)s\n\t(File: %(filename)s\n\tLine: %(lineno)d\n\tModule: (%(module)s)',
# 	datefmt='%Y-%m-%d %H:%M:%S'
# )

info_handler = logging.StreamHandler()
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(info_formatter)

error_handler = logging.StreamHandler()
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(error_formatter)

debug_handler = logging.StreamHandler()
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(debug_formatter)

warning_handler = logging.StreamHandler()
warning_handler.setLevel(logging.WARNING)
warning_handler.setFormatter(warning_formatter)

log = logging.getLogger('multi_logger')
log.setLevel(logging.DEBUG)
log.addHandler(info_handler)
log.addHandler(error_handler)
log.addHandler(debug_handler)
log.addHandler(warning_handler)
log.propagate = False
