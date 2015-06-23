# pinax-cms


!!! note "Pinax Ecosystem"
    This app was developed as part of the Pinax ecosystem but is just a Django app
    and can be used independently of other Pinax apps.
    
    To learn more about Pinax, see <http://pinaxproject.com/>


## Quickstart

Install the development version:

    pip install pinax-cms

Add `pinax-cms` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        # ...
        "pinax.cms",
        # ...
    )

Add entry to your `urls.py`:

    url(r"^", include("pinax.cms.urls"))
