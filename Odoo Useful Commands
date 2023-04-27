- Initialize a Virtual Environment --> virtualenv -p python3 PROJECTNAME

- Clone Odoo Repo                  --> git clone --branch 15.0 --single-branch --depth 1 git@github.com:odoo/odoo.git

- Install Dependencies             --> pip3 install -r ~/src/odoo/requirements.txt
				       sudo npm install -g rtlcss

- Generate a Configuration File    --> ~/src/odoo/odoo-bin --save --config config.cfg --stop-after-init

- Create a New Module              --> ~/src/odoo/odoo-bin scaffold MODULENAME

- Run Odoo Server                  --> 
~/src/odoo/odoo-bin -d DBNAME --addons-path=~/src/odoo/addons,. -i MODULENAME -u all --dev all --db-filter '.*'
- OR
~/src/odoo/odoo-bin -c config.cfg --dev=all -i MODULENAME

