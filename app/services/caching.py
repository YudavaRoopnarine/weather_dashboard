from flask_caching import Cache

# Create a Cache object
cache = Cache()


def init_cache(app):
    """
    Initialize the cache with the Flask app configuration.
    """
    cache.init_app(app)  # Uses app.config to configure the cache backend


def cache_data(key, data, timeout=300):
    """
    Store data in the cache with a specific timeout.
    Args:
        key (str): The key to store the data under.
        data (any): The data to store in the cache.
        timeout (int): Time in seconds for data to remain in the cache.
    """
    cache.set(key, data, timeout)


def get_cached_data(key):
    """
    Retrieve data from the cache.
    Args:
        key (str): The key of the cached data.
    Returns:
        any: The cached data, or None if the key does not exist.
    """
    return cache.get(key)


def clear_cache_key(key):
    """
    Clear a specific key from the cache.
    Args:
        key (str): The key to remove from the cache.
    """
    cache.delete(key)


def clear_all_cache():
    """
    Clear all cached data.
    """
    cache.clear()

# When to Use Caching
# Data is frequently requested and doesn't change too often.
# API calls or database queries take significant time or resources.
# You need to minimize costs for third-party services or databases.
# The application needs to handle high traffic efficiently.
#
# Caching in the Weather Dashboard
# For your weather dashboard:
#
# Use case: Cache weather data by city or coordinates.
# Benefit: Avoid repeated API calls for the same location within a short timeframe.
# Example: Cache weather data for 10 minutes (or the duration for which the API guarantees freshness). If the same location is queried within this time, serve the data from the cache instead of calling the API again.
# By implementing caching, you enhance the performance, reduce costs, and improve the overall user experience of your application.