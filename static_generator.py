import jinja2
import os

iter = []
p = []
with open("p.txt") as fd:
    line = fd.readline()
    while line:
        p.append(line)
        line = fd.readline()
img_dir = "static/img/"
files = os.listdir(img_dir)
files.sort()
for i, file in enumerate(files):
    iter.append((p[i], img_dir + file))

vars = {
    "iter": iter
}

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader("templates"),
    autoescape=jinja2.select_autoescape(),
    undefined=jinja2.StrictUndefined,
)

template = env.get_template("index.html")
out = template.render(**vars)

with open("index.html", "w") as fd:
    fd.write(out)
