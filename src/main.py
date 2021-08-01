from argparse import ArgumentParser
from renamer import Renamer

def getParse():
    # setup arguments
    parser = ArgumentParser()
    parser.add_argument('-n', '--name', dest='name', help='Enter new name for file or folder.')
    parser.add_argument('-s', '--sequence', dest='sequence', help='Enter number of leadig zeros to add to name.')
    parser.add_argument('-e', '--ext', dest='ext', help='Enter files extention to change.')
    parser.add_argument('-r', '--recursive', dest='recursive', help='Recursive files search.', action='store_true')
    parser.add_argument('-i', '--input', dest='input', help='Enter path to INPUT folder or file.')
    parser.add_argument('-v', '--verbose', dest='verbose', help='Verbose on/off.', action='store_true')
    # check arguments
    arguments = parser.parse_args()
    if not arguments.name or not arguments.sequence:
        parser.error('[!] Specify Mode, rename to change filename.\n sequence for adding sequence to name --help for more information')
    elif not arguments.input:
        parser.error('[!] Specify INPUT path for folder or a file --help for more information')
    else:
        name = ''
        seq = 0
        ext = []
        recursive = False
        verbose = False
        if arguments.name:
            name = arguments.name
        if arguments.sequence:
            seq = int(arguments.sequence)
        if arguments.ext:
            ext = arguments.ext.split(',')
        if arguments.recursive:
            recursive = True
        if arguments.verbose:
            verbose = True
        Renamer(arguments.input, name, seq, ext, recursive, verbose)

def main():
    getParse()

if __name__ == "__main__":
    main()