#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os as _os
import logging as _logging
import time as _time
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

from .reusables import safe_filename

log = _logging.getLogger('reusables.web')


def download(url, save_to_file=True, save_dir=".", filename=None,
             block_size=64000, overwrite=False, quiet=False):
    """
    Download a given URL to either file or memory

    :param url: Full url (with protocol) of path to download
    :param save_to_file: boolean if it should be saved to file or not
    :param save_dir: location of saved file, default is current working dir
    :param filename: filename to save as
    :param block_size: download chunk size
    :param overwrite: overwrite file if it already exists
    :param quiet: boolean to turn off logging for function
    :return: boolean or content if saved to memory
    """

    if save_to_file:
        if not filename:
            filename = safe_filename(url.split('/')[-1])
            if not filename:
                filename = "downloaded_at_{}.file".format(_time.time())
        save_location = _os.path.abspath(_os.path.join(save_dir, filename))
        if _os.path.exists(save_location) and not overwrite:
            log.error("File {0} already exists".format(save_location))
            return False
    else:
        save_location = "memory"

    try:
        request = urlopen(url)
    except ValueError as err:
        if not quiet and "unknown url type" in str(err):
            log.error("Please make sure URL is formatted correctly and"
                      " starts with http:// or other protocol")
        raise err
    except Exception as err:
        if not quiet:
            log.error("Could not download {0} - {1}".format(url, err))
        raise err

    try:
        kb_size = int(request.headers["Content-Length"]) / 1024
    except Exception as err:
        if not quiet:
            log.debug("Could not determine file size - {0}".format(err))
        file_size = "(unknown size)"
    else:
        file_size = "({0:.1f} {1})".format(*(kb_size, "KB") if kb_size < 9999
                                           else (kb_size / 1024, "MB"))

    if not quiet:
        log.info("Downloading {0} {1} to {2}".format(url, file_size,
                                                     save_location))

    if save_to_file:
        with open(save_location, "wb") as f:
            while True:
                buffer = request.read(block_size)
                if not buffer:
                    break
                f.write(buffer)
        return True
    else:
        return request.read()