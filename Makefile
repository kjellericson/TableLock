FILES = TableLock.js index.cgi
DEST = ../../tablelock/

all:
	@echo "Makefile is only used for installation."

HELP += "install: Install local files in Kjell's directory."
install:
	cp $(FILES) $(DEST)

help:
	@for a in ${HELP} ; do \
		echo -e "$$a" ;\
	done
