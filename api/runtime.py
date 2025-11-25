import sys

def handler(request):
    return {
        "python_version": sys.version
    }
