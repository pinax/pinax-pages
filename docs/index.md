# pinax-pages


!!! note "Pinax Ecosystem"
    This app was developed as part of the Pinax ecosystem but is just a Django app
    and can be used independently of other Pinax apps.
    
    To learn more about Pinax, see <http://pinaxproject.com/>


## Quickstart

Install the development version:

    pip install pinax-pages

Add `pinax-pages` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        # ...
        "pinax.pages",
        # ...
    )

Add entry to your `urls.py`:

    url(r"^", include("pinax.pages.urls"))
