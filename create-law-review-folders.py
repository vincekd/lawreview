import argparse, os
from pathlib import Path

### usage: create_law_review-folders.py [HOME_DIR] [LAW_REVIEW_NAME] [ARTICLE_AUTHOR_NAME] [FOOTNOTE_RANGE]


home = str(Path.home())
print(home)

parser = argparse.ArgumentParser()
parser.add_argument("home_dir")
parser.add_argument("lw_name")
parser.add_argument("auth_name")
parser.add_argument("fn_range")
args = parser.parse_args()

print(vars(args))

if not os.path.exists(args.home_dir):
	os.mkdir(args.home_dir)

issue_root = os.path.join(args.home_dir, args.lw_name + ", " + args.auth_name + ", Footnotes " + args.fn_range)
footnote_root = os.path.join(issue_root, "Footnotes " + args.fn_range)
print(issue_root, footnote_root)

if not os.path.exists(issue_root):
	os.mkdir(issue_root)

if not os.path.exists(footnote_root):
	os.mkdir(footnote_root)

nums = args.fn_range
[start, stop] = nums.split("-")
print(start, stop)
footnote_count = range(int(start), int(stop))
print(footnote_count)

for n in footnote_count:
	path = os.path.join(footnote_root, "Footnote " + str(n) + ",")
	if not os.path.exists(path):
		os.mkdir(path)
