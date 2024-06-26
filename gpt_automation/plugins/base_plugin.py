class BasePlugin:
    def __init__(self, env, settings):
        self.env = env
        self.settings = settings

    def get_visitors(self):
        """
        Return a list of visitor instances that this plugins wants to use.
        """
        raise NotImplementedError("Each plugins must implement the 'get_visitors' method.")
