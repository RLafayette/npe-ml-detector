from hashlib import sha1
import numpy as np
from numpy import array
from numpy.linalg import norm
from datasketch.minhash import MinHash
from datasketch.weighted_minhash import WeightedMinHashGenerator
from datasketch.lsh import MinHashLSH
import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from dist.python_parser.Java8Lexer import Java8Lexer
from dist.python_parser.Java8Parser import Java8Parser
import glob
import re
import csv
from datetime import date
from analysis import *

def parse_samples():
    samples_filepaths = glob.glob("example/mix/dataset/*.java")

    for filepath in samples_filepaths:
        print(str(filepath))
        input_stream = FileStream(str(filepath), encoding='utf-8')
        lexer = Java8Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = Java8Parser(stream)
        tree = parser.compilationUnit()
        tree_string = Trees.toStringTree(tree, None, parser)
        #print(tree_string)
        sample_filename = re.search(r"example\/mix\/dataset\/(.+\.java)", str(filepath)).group(1)
        tree_string = re.sub(r'literal 0[xX][0-9a-fA-F]+(.\d*p[\+\-]\d*)?[Lfd]?', 'literal HEXADECIMAL', tree_string)
        tree_string = re.sub(r'literal (\d+[eE][\+\-]\d+|[\+\-]?\d+\.?\d*[Ldf]?|\.\d+)', 'literal NUMBER', tree_string)
        tree_string = re.sub(r'literal (\'[^\']?\')', 'literal CHAR', tree_string)
        tree_string = re.sub(r'literal (\"[^\"]*\")', 'literal STRING', tree_string)
        tree_string = re.sub(r'literal (true|false)', 'literal BOOLEAN', tree_string)
        with open( "example/mix/ast/" + sample_filename.replace("java", "txt"), "w+") as file:
            file.write(tree_string)

def parse_ast():
    ast_filepaths = glob.glob("example/mix/ast/*.txt")
    #ast_filepaths = glob.glob("astTree.txt")

    for filepath in ast_filepaths:
        print(str(filepath))
        ast_name = re.search(r"example\/mix\/ast\/(.+)\.txt", str(filepath)).group(1)
        #ast_name = re.search(r"(.+)\.txt", str(filepath)).group(1)
        s = set()

        with open(filepath, "r") as file:
            '''
            Pega só as folhas de cada AST
            '''
            matches = re.findall(r"\(?([a-zA-Z_]+) (\"?[_\,\ a-zA-Z]+\"?)\)?", file.read())
            for matchNum, match in enumerate(matches, start=1):
                #print(match)
                for groupNum in range(0, len(match)):
                    s.add(match[groupNum])
        samples_dict[ast_name] = s

def main(argv):
    #parse_samples()
    parse_ast()
    analyse()

if __name__ == '__main__':
    main(sys.argv)
