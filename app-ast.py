import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from dist.python_parser.Java8Lexer import Java8Lexer
from dist.python_parser.Java8Parser import Java8Parser


def writeFile(astTree):
    f = open("astTree.txt","w+")
    
    if(f.writable()):
        f.write(str(astTree))
    else:
        print("Erro ao escrever no arquivo astTree.txt")
    
    f.close()


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = Java8Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Java8Parser(stream)
    tree = parser.compilationUnit()

    tree_string = Trees.toStringTree(tree, None, parser)
    
    print(tree_string)
    writeFile(tree_string)
 
if __name__ == '__main__':
    main(sys.argv)
