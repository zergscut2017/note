import yaml
import os.path

class Loader(yaml.Loader):

    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, 'r') as f:
            return yaml.load(f, Loader)

Loader.add_constructor('!include_1', Loader.include)
Loader.add_constructor('!include_2', Loader.include)

with open('foo.yaml', 'r') as f:
    data = yaml.load(f, Loader)

with open('output.yaml', 'w') as out:
    yaml.dump(data, out)

