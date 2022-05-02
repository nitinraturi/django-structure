from split_settings.tools import optional, include

include(
    # Load environment settings
    'base/env.py',

    # Here we should have the order because of dependencies
    'base/constant.py',
    'base/paths.py',
    'base/apps.py',
    'base/middleware.py',
    'base/debug_toolbar.py',

    # Load all other settings
    'base/*.py',

    # optional('local/*.py'),  # we can load any other settings from local folder
)
