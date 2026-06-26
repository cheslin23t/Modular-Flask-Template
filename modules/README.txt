Flask Thing module guide

Use this folder as the blueprint for new app sections.

Suggested pattern for a new module:

modules/
  feature_name/
    index.py
    example.txt

Keep the route registration in index.py and add any related templates or helpers beside it.
Use modules/utils/ for shared code that more than one module needs.
Copy any folder that fits your app and rename it to match the feature you want to build.