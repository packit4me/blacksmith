#!/usr/bin/python

import os, json, requests
import jinja2

FORGE = u'https://forge.puppetlabs.com'
ANVIL = u'/var/lib/blacksmith'
PATTERN = u'/home/xaeth/Development/blacksmith/templates/module.spec.j2'

class PuppetModule(dict):
  def __init__(self, **kwargs):
    self.__keys = kwargs.keys()
    for key, value in kwargs.iteritems():
      setattr(self, key, value)
      self[key] = value

  def releasefile(self):
    return u'{full_name}/{version}.tar.gz'.format(**self)

  def download(self, forge=FORGE, anvil=ANVIL):
    self.forge  = forge
    self.anvil  = anvil
    releasefile = self.releasefile()
    source_url  = os.path.join(forge, releasefile)
    verify_directory(os.path.join(anvil, self.author))
    destination = os.path.join(anvil, releasefile)
    verify_directory(os.path.split(destination)[0])
    open(destination,'w').write(requests.get(os.path.join(forge, releasefile)).content)

  def generate_spec(self):
    return

class PuppetModules(list):
  def __init__(self, base_url, use_cache=False, cache_dir=ANVIL):
    self.base_url = base_url
    self.cache_dir = cache_dir
    self.cache_file = os.path.join(self.cache_dir, 'modules.json')
    if use_cache:
      module_list = self.read_cache()
    else:
      module_list = self.download_list()
    self.parse(module_list)

  def cache_list(self, module_list, cache_file=None):
    if cache_file is None:
      cache_file = self.cache_file
    open(self.cache_file, 'w').write(json.dumps(module_list))

  def read_cache(self):
    return json.loads(open(self.cache_file,'r').read())
      
  def download_list(self, base_url=None):
    if base_url is None:
      base_url = self.base_url
    return json.loads(requests.get(os.path.join(base_url, u'modules.json')).content)

  def parse(self, module_list):
    for module in module_list:
      self.append(PuppetModule(**module))

  def get(self, key, value):
    found = []
    for module in self:
      if module.key == value:
        found.append(module)


def verify_directory(directory):
  if not os.path.exists(directory):
    os.mkdir(directory)
  elif not os.path.isdir(directory):
    raise Exception, 'Path is not a directory'
  elif not os.access(directory, os.W_OK):
    raise Exception, 'Invalid permissions on {0}'.format(directory)
  
def download_modules_metadata(base_url):
  return json.loads(requests.get( os.path.join(base_url, u'modules.json')).content)

def download_module(module, forge=FORGE, anvil=ANVIL):
  releasefile = module.releasefile()
  source_url = os.path.join(forge, releasefile)
  verify_directory(os.path.join(anvil, module.author))
  destination = os.path.join(anvil, releasefile)
  verify_directory(os.path.split(destination)[0])
  open(destination,'w').write(requests.get(os.path.join(forge, releasefile)).content)

