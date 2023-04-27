- Initialize a virtual environment

      virtualenv -p python3 PROJECTNAME

- Clone Odoo repo

      git clone --branch 15.0 --single-branch --depth 1 git@github.com:odoo/odoo.git

- Install dependencies

      pip3 install -r ~/src/odoo/requirements.txt
      sudo npm install -g rtlcss

- Generate a config file

      ~/src/odoo/odoo-bin --save --config config.cfg --stop-after-init

- Create a new module

      ~/src/odoo/odoo-bin scaffold MODULENAME

- Run Odoo server

      ~/src/odoo/odoo-bin -d DBNAME --addons-path=~/src/odoo/addons,. -i MODULENAME -u all --dev all --db-filter '.*'

- OR with a config file

      ~/src/odoo/odoo-bin -c config.cfg --dev=all -i MODULENAME
