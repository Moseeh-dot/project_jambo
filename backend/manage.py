#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_jambo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Are you sure it's installed and "
                          "available on your PYTHONPATH environment variable? "
                          f"Is there a typo in your DJANGO_SETTINGS_MODULE variable? Did you "
                          f"forget to activate a virtual environment?\n{exc}")
    execute_from_command_line(sys.argv)