import importlib.metadata


def get_pypi_package_name(module_name):
    """
    Attempt to get the PyPI package name for a given Python module using importlib.metadata by checking top-level packages.

    Args:
        module_name (str): The name of the module/package to look up.

    Returns:
        str or None: The name of the PyPI package if found, otherwise None.
    """
    try:
        # Retrieve all distribution packages available
        distributions = importlib.metadata.distributions()
        for distribution in distributions:
            # Checking if module_name matches any top-level package of the distribution
            if module_name in distribution.read_text('top_level.txt').split():
                return distribution.metadata['Name']
    except (importlib.metadata.PackageNotFoundError, FileNotFoundError):
        # Return None if no matching distribution was found or if 'top_level.txt' is missing
        return None


# Example usage
if __name__ == "__main__":
    module_name = "gpt_automation"  # Change this to the module you want to check.
    pypi_name = get_pypi_package_name(module_name)
    if pypi_name:
        print(f"The PyPI package name for '{module_name}' is '{pypi_name}'.")
    else:
        print(f"Could not find the PyPI package name for '{module_name}'.")
