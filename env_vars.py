import os

def get_owner():
    try:
        owner_name = os.environ['OWNER']

    except KeyError:
        owner_name = 'no owner'

    return 'OWNER Environment Variable is defined as: {0}'.format(owner_name)
