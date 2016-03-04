from coal import CoalFile
from util import download, unzip, cp, run
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
        run('make')
    def package(self):
        cp('src/src/*.a', 'libs/')
        cp('src/src/*.dll', 'libs/')
        cp('src/src/*.h', 'include')
    def info(self, generator):
        generator.add_library('-lluajit')
        generator.add_link_dir('libs/')
        generator.add_include_dir('include/')
