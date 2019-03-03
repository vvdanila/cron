# Crontab Entry Parser

Python cli written in Python 3.6

Test coverage 72%

## To run the cron cli:

Note: the * symbol has to be escaped in the bash shell

`$ python cron.py 0 0 1,15 1-3 \* /bin/foo bar`

`$ python cron.py 2-24/3 0 1,15 1-3 \* /bin/foo bar`

## To run the unit tests:

`$ python test_cron.py`
