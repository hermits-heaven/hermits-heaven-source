from jinja2 import Environment, BaseLoader, Template, FileSystemLoader
import os


def build_file(filename):
    src_pth = 'src/' + filename
    with open(src_pth, encoding='utf-8') as f_in:
        source = f_in.read()
    template = Environment(loader=FileSystemLoader('./src')).from_string(source)
    rendered = template.render()

    out_pth = 'deploy/' + filename
    os.makedirs(os.path.dirname(out_pth), exist_ok=True)
    with open(out_pth, 'w', encoding='utf-8') as f_out:
        f_out.write(rendered)

    
if __name__ == "__main__":
    build_file('index.html')
    build_file('bases/index.html')
