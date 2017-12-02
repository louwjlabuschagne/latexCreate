v=$1
_filename=${v::${#v}-4}

pdflatex -synctex=1 -interac$ion=nonstopmode -shell-escape $_filename.tex;
bibtex $_filename;
pdflatex -synctex=1 -interaction=nonstopmode -shell-escape $_filename.tex;
open -a Preview $_filename.pdf;

