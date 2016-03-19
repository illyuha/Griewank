from lib import *

# TODO: use concurrency?
initialize()
while True:
    evaluate()
    if stop():
        break
    select()
    break
    applyOperators()
