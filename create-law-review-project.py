import argparse, os
from docxtpl import DocxTemplate

def get_range_str(args):
    return str(args.start) + "-" + str(args.stop)

def get_root_name(args):
    return args.checker + ", " + args.author + ", Footnotes " + get_range_str(args)

def get_issue_root(args):
    return os.path.join(args.home_dir, get_root_name(args))

def create_dir_structure(args):
    if not os.path.exists(args.home_dir):
        os.mkdir(args.home_dir)
    else:
        print(args.home_dir, "already exists")

    issue_root = get_issue_root(args)
    footnote_root = os.path.join(issue_root, "Footnotes " + get_range_str(args))
    print(issue_root, footnote_root)

    if not os.path.exists(issue_root):
        os.mkdir(issue_root)
    else:
        print(issue_root, "already exists")

    if not os.path.exists(footnote_root):
        os.mkdir(footnote_root)
    else:
        print(footnote_root, "already exists")

    for n in range(args.start, args.stop + 1):
        path = os.path.join(footnote_root, "Footnote " + str(n) + ",")
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            print(path, "already exists")


def create_source_file(args):
    name = os.path.basename(args.template_doc).replace(" Template", "")
    print(name)
    doc = DocxTemplate(args.template_doc)
    context = {
        'start': args.start,
        'stop': args.stop,
        'author': args.author,
        'checker': args.checker,
        'editor': args.editor,
    }
    print(context)
    doc.render(context, autoescape=True)
    doc.save(os.path.join(get_issue_root(args), name))

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("home_dir")
    parser.add_argument("template_doc")
    parser.add_argument("--start", type=int)
    parser.add_argument("--stop", type=int)
    parser.add_argument("--author")
    parser.add_argument("--checker")
    parser.add_argument("--editor")
    args = parser.parse_args()
    return args

args = get_args()
print(vars(args))

create_dir_structure(args)
create_source_file(args)
