import time

import pytest


class ResultsCollector:  # pragma: no cover
    def __init__(self):
        self.reports = []

    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        outcome = yield
        report = outcome.get_result()
        if report.when == 'call':
            self.reports.append(report)
