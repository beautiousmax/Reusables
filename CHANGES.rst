Changelog
=========

Version 0.8.0
-------------

- Adding log_exception wrapper
- Adding ProtectedDict
- Adding hooks for Tasker main loop
- Adding roman number functions
- Breaking change: Removing reuse wrapper

Version 0.7.0
-------------

- Adding archive_all and now methods
- Adding logger helpers to add stream and file handlers
- Adding depth and abspath to find files methods
- Adding head, tail, cat bash equivalents
- Adding command queue to Tasking class, to give commands asynchronously and without directly referencing the instance
- Changing test suite to have a common file it pulls imports and info from
- Changing logger helpers to accept string instead of logger
- Breaking change: Moving log formats from variables to Namespace log_formats
- Breaking change: Moving command line helpers to cli
- Breaking change: Command line helpers are not imported by default, should now use: from reusables.cli import *
- Breaking change: join_root has been better named join_here

Version 0.6.1
-------------

- Changing config_dict auto_find to accept a path to search at
- PyPI is stupid is why 0.6.0 is not up there

Version 0.6.0
-------------

- Adding multiprocessing helpers, Tasker class and run_in_pool
- Adding download and cmd helper functions
- Adding ThreadedServer class, for running a server (defaults to local file server) in the background
- Adding terminal analogue functions: cd, pwd, ls, pushd, popd
- Adding match_case option for find_all_files and count_all_files
- Fix 'run' call to CalledProcessError on older python versions
- Changing logger to _logger to be hidden by default (should not be breaking, if so you coded wrong)

Version 0.5.2
-------------

- Fix setup.py to use __init__.py instead of reusables.py for attrs

Version 0.5.1
-------------

- Adding default argument to confignamespace's int, float, list and boolean methods
- Adding change_logger_levels
- Changing __version__ location to __init__ so it can be accessed properly
- Changing protected_keys in Namespace to be hidden from documentation
- Changing linux only tests to be in their own class
- Breaking change: keyword arg position for confignamespace.list now has 'default' as first kwarg

Version 0.5.0
-------------

- Adding ConfigNamespace
- Adding lock wrapper for functions
- Adding duplicate file finder
- Adding easy CSV / list transformation
- Adding protected keys for namespaces
- Adding touch
- Adding extensions for scripts, binary and markup files
- Changing logging to be more explicit and run on sys.stdout
- Breaking change: removed command line running options and main function

Version 0.4.1
-------------

- Fixing Firefox dump command not working
- Adding MissingCookiesDB exception for clearer
- Wrapping commits with exceptions clauses for BrowserException
- Adding "created" and "expires" in _row_to_dict for Browsers

Version 0.4.0
-------------

- Breaking change: Removed 'dnd' from functions for clearer 'dry_run' or 'delete_on_success'
- Breaking change: Removing 'dangerzone' file, moving 'reuse' function to root namespace
- Added management tools for Firefox and Chrome cookies
- Added unique wrapper tool, ensures return value has not been returned before
- Changed all top level imports to have underscore before them like standard library

Version 0.3.0
-------------

- Namespace re-written to be more compatible with built-in dict
- Added support for rarfile extraction
- Adding PY2, PY3 as compliments of the booleans python3x to be similar to the six package
- Adding logging features
- Separating functionality to individual files
- Adding sphinx generated API documentation

Version 0.2.0
-------------

- Added DateTime class
- Added and rearranged several regular expression
- Added tree_view of dictionaries
- Added os_tree of a directory to a dictionary

Version 0.1.3
-------------

- Addition of Makefile
- Fixing issues with setup.py not including all needed files
- Tests now pass on windows by skipping some linux specific tests
- Improved config tests to only test against known sections, instead of entire dictionaries

Version 0.1.2
-------------

- Name change from reuse to reusables due to name already being registration on pypi

Version 0.1.1
-------------

- find_all_files_iter renamed to find_all_files_generator
- Added python2.6 and pypy testing and support
- Namespace is now a subclass of dict.
- Changing Readme into rst format.

Version 0.1
-----------

- initial release
