import json

from controllercreator import create_controllers
from entitycreator import create_entities
from initializr import initialize_project
from javaconverterstyler import JavaConverterStyler
from servicecreator import create_services
from sqlgenerator import generate_sql


def get_input():
    with open('input.json', 'r') as f:
        return json.load(f)


def get_coder():
    return JavaConverterStyler(inp.get("indentation_space_count"),
                               inp.get("open_curly_brackets_same_line"),
                               inp.get("beautify_with_spaces"),
                               inp.get("beautify_with_blank_lines"))


inp = get_input()
# todo: validate input
initialize_project(inp)
java_coder = get_coder()
create_entities(java_coder, inp.get("entities"), inp.get("app_name"))
create_controllers(java_coder, inp.get("entities"), inp.get("app_name"))
create_services(java_coder, inp.get("entities"), inp.get("app_name"))
# SQL Generator
generate_sql(inp.get("entities"), inp.get("app_name"))
