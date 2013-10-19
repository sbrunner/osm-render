
import glob
import os
from bottle import jinja2_template

def generate_configs():
    os.chdir(os.path.dirname(__file__))

    result = jinja2_template(
        'config.yaml.jinja',
        update=False,
    )
    file_open = open('config.yaml', 'w')
    file_open.write(result)
    file_open.close()

    result = jinja2_template(
        'config.yaml.jinja',
        update=True,
    )
    file_open = open('config-update.yaml', 'w')
    file_open.write(result)
    file_open.close()
