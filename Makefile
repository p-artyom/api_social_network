WORKDIR = yatube_api
MANAGE = python $(WORKDIR)/manage.py

run:
	$(MANAGE) runserver

style:
	black -S -l 79 $(WORKDIR)
	isort $(WORKDIR)
	flake8 $(WORKDIR)

shell:
	$(MANAGE) shell
