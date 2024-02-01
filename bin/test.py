import sys

from caragols.lib import carp
from caragols.lib import clix


# myapp = clix.App(name="toad")
# print(myapp.conf.show())

# print(myapp.conf.get('log'))

if __name__ == "__main__":
    comargs = sys.argv[1:]
    print(f'Comargs=\n{comargs}\n')
    verb = comargs[0]
    print(f'Verb={verb}')
