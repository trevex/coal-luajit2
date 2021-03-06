from coal import CoalFile
from util import download, unzip, cp, run, cd, system
from os import path

class Luajit2File(CoalFile):
    version = "2.0.4"
    zipfile = "LuaJIT-%s.zip" % version
    url = "http://luajit.org/download/%s" % zipfile
    exports = ["include", "libs"]

    def prepare(self):
        download(self.url, self.zipfile)
        unzip(self.zipfile, 'src')
    def build(self):
        with cd('src/LuaJIT-%s' % self.version):
            run('make')
    def package(self):
        src_path = 'src/LuaJIT-%s/src/' % self.version
        cp(src_path + '*.a', 'libs/')
        cp(src_path + '*.dll', 'libs/')
        cp(src_path + '*.h', 'include/')
    def info(self, generator):
        if system() == 'Windows':
            generator.add_library('-llua51')
        else:
            generator.add_library('-lluajit')
        generator.add_link_dir('libs/')
        generator.add_include_dir('include/')
