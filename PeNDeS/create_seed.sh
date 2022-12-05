# !/bin/bash
echo Please enter the name of your seed:
read id
echo Please enter the name of the input project file:
read input
webgme node ./node_modules/webgme-cli/bin/webgme new seed -f $input $id
