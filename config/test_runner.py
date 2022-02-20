from django.test.runner import DiscoverRunner


class TestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        """ Creates the test databases by calling setup_databases(). """
        pass

    def teardown_databases(self, old_config, **kwargs):
        """ Destroys the test databases, restoring pre-test conditions by calling teardown_databases(). """
        pass
