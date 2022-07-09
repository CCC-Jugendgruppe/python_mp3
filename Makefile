install:
	python3 -m pip install .

gui:
	make install
	~/.local/bin/python-mp3 -g

cli:
	make install
	~/.local/bin/python-mp3 -i ./input