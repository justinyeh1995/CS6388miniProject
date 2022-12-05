# !/bin/bash
echo Please enter the name of your plugin:
read id
webgme node ./node_modules/webgme-cli/bin/webgme new plugin --language Python $id
webgme npm i
