pdflatex -synctex=1 -interaction=nonstopmode -shell-escape main.tex;
bibtex main;
pdflatex -synctex=1 -interaction=nonstopmode -shell-escape main.tex;
open -a Preview main.pdf;

