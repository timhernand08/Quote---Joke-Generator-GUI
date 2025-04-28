import os, sys

def resource_path(relative_path):
  if getattr(sys, 'frozen', False):
        application_path = os.path.join(os.environ['APPDATA'], 'Quote Joke Gen')
        os.makedirs(application_path, exist_ok=True)
  else:
        application_path = os.path.dirname(os.path.abspath(__file__))
  return os.path.join(application_path, relative_path)    