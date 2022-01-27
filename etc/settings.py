'''
BFS 2020 Scripte settings
'''
import os, sys
import git

GIT_ROOT    =   os.path.dirname(  os.path.dirname( os.path.abspath(__file__)  ) )

LIB_DIR     =   os.path.join(GIT_ROOT, 'library')

LOGO_DIR    =   os.path.join(LIB_DIR, 'allgemein')

SOURCE_DIR  =   os.path.join(GIT_ROOT, 'source')
#
# Create Version and Revision
#
repo = git.Repo(GIT_ROOT)
#
try :
    GIT_VERSION=repo.tags[-1].name
    GIT_MESSAGE=repo.git.tag(n=True).split('\n')[-1]
except IndexError :
    GIT_VERSION = os.environ.get('BFS_VERSION', 'Initial Version not defined yet')
    GIT_MESSAGE = os.environ.get('BFS_MESSAGE', 'Initial Message not defined yet')
#
GIT_REVISION=repo.commit().hexsha