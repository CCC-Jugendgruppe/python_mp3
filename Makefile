install:
	python3 -m pip install .

install_sudo:
	sudo python3 -m pip install .

gui:
	make install
	~/.local/bin/python-mp3 -g

gui_sudo:
	make install_sudo
	/usr/bin/python-mp3 -g

cli:
	make install
	~/.local/bin/python-mp3 -i ./input

cli_sudo:
	make install_sudo
	/usr/bin/python-mp3 -i ./input