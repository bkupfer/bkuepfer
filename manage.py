#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    print('manage . py --')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bkuepfer.settings")
    print('manage . py -- [2]')
    try:
        print('manage . py -- [3]')
        from django.core.management import execute_from_command_line
        print('manage . py -- [4]')
    except ImportError as exc:
        print('manage . py -- [5]')
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
    print('manage . py -- [6]')
    execute_from_command_line(sys.argv)
    print('manage . py -- [7]')
