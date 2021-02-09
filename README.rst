Temporary fix for swagger in Flask-AppBuilder.
Waiting for this PR: https://github.com/dpgaspar/Flask-AppBuilder/pull/1465

- Install it:
    - for local develop:
        pip install -e <local path to source>

    - for use from git (via tarballs):
        pip install https://github.com/lexisstv/fab_addon_SwaggerTemporaryFix/archive/master.zip

- Use it:
    On you application add the following key to config.py

    ADDON_MANAGERS = ['fab_addon_SwaggerTemporaryFix.manager.SwaggerTemporaryFixManager']

