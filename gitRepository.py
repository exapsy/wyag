import configparser
import os

class GitRepository(object):
  """A git repository"""

  worktree = None
  gitdir = None
  conf = None

  def __init__(self, path, force=False):
    self.worktree = path
    self.gitdir = os.path.join(path, ".git")

    if not (force or os.path.isdir(self.gitdir)):
      raise Exception("Not a Git repository %s" % path)

    # Read configuration file in .git/config
    self.conf = configparser.ConfigParser()
    cf = repo_file(self, "config")

    if cf and os.path.exists(cf):
      self.conf.read([cf])
    elif not force:
      raise Exception("Configuration file missing")
    
    if not force:
      vers = int(self.conf.get("core", "repositoryformatversion"))
      if vers != 0 and not force:
        raise Exception("Unsupported repositoryformatversion %s" % vers)

def repo_path(repo, *path):
  """Compute path under repo's gitdir."""
  return os.path.join(repo.gitdir, *path)

def repo_file(repo, *path, mkdir=False):
  """Same as repo_path, but create dirname(*path) if absent. 
    For example, repo_file(r, \"refs\" \"remotes\", \"origin\", \"HEAD\")  will create
    .git/refs/remotes/origin."""

  if repo_dir(repo, *path[:-1], mkdir=mkdir):
    return repo_path(repo, *path)
def repo_dir(repo, *path, mkdir=False):
  """Same as repo_path, but mkdir *path if absent if mkdir."""

  path = repo_path(repo, *path)

  if os.path.exists(path):
    if(os.path.isdir(path)):
      return path
    else:
      raise Exception("Not a directory %s" % path)

  if mkdir:
    os.makedirs(path)
    return path
  else:
    return None
  
def repo_create(path):
  """Create a new repository at path."""

  repo = GitRepository(path, True)

  # First we make sure the path either doesn't exist or is an
  # empty dir

  if os.path.exists(repo.worktree):
    if not os.path.isdir(repo.worktree):
      raise Exception ("%s is not a directory!" % path)
    if os.listdir(repo.worktree):
      raise Exception("%s is not empty!" % path)

  else:
    os.makedirs(repo.worktree)

  assert(repo_dir(repo, "branches", mkdir=True))
  assert(repo_dir(repo, "objects", mkdir=True))
  assert(repo_dir(repo, "refs", "tags", mkdir=True))
  assert(repo_dir(repo, "refs", "heads", mkdir=True))

  # .git/description
  with open(repo_file(repo, "description"), "w") as f:
    f.write("Unnamed repository; edit this file 'description' to name the repository.\n")
  
  # .git/HEAD
  with open(repo_file(repo, "HEAD"), "w") as f:
    f.write("ref: refs/heads/master\n")

  with open(repo_file(repo, "config"), "w") as f:
    config = repo_default_config()
    config.write(f)

  return repo
  
def repo_default_config():
  ret = configparser.ConfigParser()

  ret.add_section("core")
  ret.set("core", "repositoryformatversion", "0")
  ret.set("core", "filemode", "false")
  ret.set("core", "bare", "false")

  return ret