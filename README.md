# Analisador de código Java (nome provisório)

## Para gerar os arquivos do parser na pasta dist.

Esse projeto versiona a pasta dist e seus arquivos como forma de poupar tempo de quem planeja desenvolver ou executar o projeto, dessa forma isso está aqui apenas para fins de documentação.

Instalar antlr4 (retirado de https://levlaz.org/setting-up-antlr4-on-windows/):
- Faça download do antlr-4.9.3-complete.jar em https://www.antlr.org/download.html.
- Crie a pasta C:\Javalib e copie o jar para ela.
- Nessa pasta crie os arquivos antlr4.bat e grun.bat
- Em antlr4.bat escreva java org.antlr.v4.Tool %*
- Em grun.bat escreva java -cp .;org.antlr.v4.runtime.misc.TestRig %*
- Salve os arquivos
- Adicione C:\Javalib no PATH do Windows.
- Crie a variável de ambiente CLASSPATH se não existir e coloque C:\Javalib\antlr-4.9.3-complete.jar

Executar os seguintes comandos na raiz desse projeto:
- antlr4 -Dlanguage=Python3 grammar/Java8Lexer.g4 -visitor -o dist
- antlr4 -Dlanguage=Python3 grammar/Java8Parser.g4 -visitor -o dist

## Para executar o projeto e gerar uma árvore sintática (formato texto):

- `python app.py <PATH PARA ARQUIVO JAVA/>`

## Para gerar uma representação gráfica do código:
Executar os comandos para gerar um parser em código Java:
- `antlr4 -Dlanguage=Java grammar/Java8Lexer.g4 -visitor -o dist_tree`
- `antlr4 -Dlanguage=Java grammar/Java8Parser.g4 -visitor -o dist_tree`
- Compilar os arquivos Java gerados: `javac dist_tree/*.java`
- Entre na pasta onde está o parser Java (`cd dist_tree`)
- Gerar árvore: `java -cp .;C:\Javalib\antlr-4.9.3-complete.jar org.antlr.v4.runtime.misc.TestRig Java8 compilationUnit -tree -gui < "<PATH DO ARQUIVO JAVA/>"`

-----

Links úteis ~~para revisitar em caso de problemas~~: 

- https://stackoverflow.com/questions/38739804/antlr4-error-problems-calling-org-antlr-v4-gui-testrig-main
- https://stackoverflow.com/questions/25067047/antlr-could-not-find-or-local-main-class-even-when-it-is-there
- https://stackoverflow.com/questions/47121549/antlr4-testrig-grun-throws-java-lang-noclassdeffounderror-exception
- https://stackoverflow.com/questions/23315302/antlr4-cant-load-hello-as-lexer-or-parser
- https://stackoverflow.com/questions/31841151/antrl4-cant-get-python-antlr-to-generate-a-graphic-of-the-parse-tree

Lembretes importantes:

- A regra **S** (regra inicial da gramática, como é normalmente referenciada no campo de linguagens formais) da gramática do Java não vem por padrão na gramática que utilizamos, então devemos sempre lembrar de incluí-la se o arquivo for substituído:
```
compilationUnit 
   : packageDeclaration? importDeclaration* typeDeclaration* EOF
   ;
```

--------------------

# Para executar:

`python app.py` -> Gera as matrizes de similaridade. Ver o main, caso já as tenha gerado é possível comentar parse_samples()

`python knn.py` -> Executa o k-nn no considerando cada matriz de similaridade.
