# gcp-python-helpers

A Python library of helper functions to use in Google Cloud functions.

All of the functions included are tested in the scope of Google Cloud functions, so they might not work properly outside of that.

## Installation

```python
python3 -m pip install gcphelpers 
```

## Helper functions

There currently exist some wrappers around the following tools:

- Prometheus PushGateway
  - Push to PushGateway

- Secret Manager
  - Fetch Secret Manager secret

- Google Cloud Storage
  - Push a file to GCS