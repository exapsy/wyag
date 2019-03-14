import argparse
import collections
import hashlib
import re
import sys
import zlib
import gitRepository

argparser = argparse.ArgumentParser(description="The stupid content tracker")
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True
argsp = argsubparsers.add_parser("init", help="Initialize a new, empty repository.")
argsp.add_argument("path",
                   metavar="directory",
                   nargs="?",
                   default=".",
                   help="Where to create the repository.")

def main(argv=sys.argv[1:]):
  args = argparser.parse_args(argv)

  # if   args.command == "add"         : cmd_add(args)
  # elif args.command == "cat-file"    : cmd_cat_file(args)
  # elif args.command == "checkout"    : cmd_checkout(args)
  # elif args.command == "commit"      : cmd_commit(args)
  # elif args.command == "hash-object" : cmd_hash_object(args)
  if args.command == "init"        : cmd_init(args)
  # elif args.command == "log"         : cmd_log(args)
  # elif args.command == "ls-tree"     : cmd_ls_tree(args)
  # elif args.command == "merge"       : cmd_merge(args)
  # elif args.command == "rebase"      : cmd_rebase(args)
  # elif args.command == "rev-parse"   : cmd_rev_parse(args)
  # elif args.command == "rm"          : cmd_rm(args)
  # elif args.command == "show-ref"    : cmd_show-ref(args)
  # elif args.command == "tag"         : cmd_tag(tag)

def cmd_init(args):
  gitRepository.repo_create(args.path)