import argparse, os
from pathlib import Path
from docxtpl import DocxTemplate

parser = argparse.ArgumentParser()
parser.add_argument("template_doc")
parser.add_argument("output_path")
parser.add_argument("--range")
parser.add_argument("--author")
parser.add_argument("--checker")
parser.add_argument("--editor")
args = parser.parse_args()

print(vars(args))
name = os.path.basename(args.template_doc)
[start, stop] = args.range.split("-")
r = range(int(start), int(stop))
print(name)

doc = DocxTemplate(args.template_doc)
context = {
    'start': int(start),
    'stop': int(stop),
    'author': args.author,
    'checker': args.checker,
    'editor': args.editor,
}
print(context)
doc.render(context)
doc.save(os.path.join(args.output_path, name))

