import warnings

# Turn deprecation warnings into errors
warnings.simplefilter('error', DeprecationWarning)

pytest_plugins = ['giantarctic.fixtures.arctic']
