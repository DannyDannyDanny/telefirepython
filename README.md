# telefirepython
Telegram Bot Connected to Google Firebase

## how to
1. Start server and start 2-pane tmux session
2. Start good_bot on pane 2
3. Detach from tmux session `^b, d`
4. Connect to server via ssh
5. Use tmux attach to continue session
6. Do work
7. Detach from tmux session, exit.

## dependencies
    # ipgetter
    pip install git+https://github.com/madmouser1/ipgetter.git



## Environment Setup Procedure
1. New git repository (w Python .gitignore)
2. Clone locally
3. `cd` to into repository
4. Make folder for sensitive data: `mkdir creds`
5. Add creds to .gitignore with: `echo "creds/" >> .gitignore`
6. Make sure `pipenv` is installed: `pip install --user pipenv`
7. Set up python environment with `firebase-admin` module: `pipenv install firebase-admin`
8. Run `pipenv run python /path/file.py` to run python scripts

>6. Make python environment `virtualenv envname`
>7. Install module dependencies `envname/bin/pip install firebase-admin`

[Telegram Bot Forum Chat](https://t.me/pythontelegrambotgroup)
