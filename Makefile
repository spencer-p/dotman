
# Project metadata
NAME=dotman

# Utils
ZIP=zip
SHEBANG=\#!/usr/bin/env python3

# Files
SRC=src/

.INTERMEDIATE: $(NAME).zip

$(NAME): $(NAME).zip
	echo "$(SHEBANG)" | cat - $^ > $@
	chmod +x $@

$(NAME).zip: $(SRC)
	cd $(SRC);\
	zip -r ../$@ * --exclude \*_pycache__/ \*.pyc \*.pyo

clean:
	rm -f $(NAME) $(NAME).zip
