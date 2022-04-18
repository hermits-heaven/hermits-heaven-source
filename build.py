from jinja2 import Environment, FileSystemLoader
import os


global_env = Environment(loader=FileSystemLoader("./src"))


def fwrite(fname, content):
    os.makedirs(os.path.dirname(fname), exist_ok=True)
    with open(fname, 'w', encoding="UTF-8") as fout:
        return fout.write(content)


def build_file(filename):
    template = global_env.get_template(filename)
    rendered = template.render()
    fwrite(os.path.join('deploy', filename), rendered)


def build():
    build_file('index.html')
    build_file('bases/index.html')


if __name__ == "__main__":
    build()
