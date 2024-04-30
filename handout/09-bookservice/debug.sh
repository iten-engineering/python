export FLASK_APP=bookservice.py

# If you enable debug support the server will reload itself on code changes, and it will also provide you with a helpful debugger
# if things go wrong. Setting FLASK_ENV=development does the following things:
#   a) it activates the debugger
#   b) it activates the automatic reloader
#   c) it enables the debug mode on the Flask application
#
# Attention
# - Even though the interactive debugger does not work in forking environments (which makes it nearly impossible to use on
#   production servers), it still allows the execution of arbitrary code.
# - This makes it a major security risk and therefore it must never be used on production machines.
export FLASK_ENV=development

# run server
flask run