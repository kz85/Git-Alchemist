import pytest
from src.utils import run_shell
from subprocess import CompletedProcess

@pytest.fixture
def completed_successful_process():
    return CompletedProcess("test_command", 0, "  Mocking successul command output  ")

@pytest.fixture
def completed_unsuccessful_process():
    return CompletedProcess("test_command", -1, "", "Mocking terminated process")

class TestCommandRunning:
    def test_run_shell_successful(self, completed_successful_process, mocker):
        mock_subprocess_run = mocker.patch("src.utils.subprocess.run")
        mock_subprocess_run.return_value = completed_successful_process
        assert run_shell("test_command", check=False) == "Mocking successul command output"

    def test_run_shell_unsuccessful(self, completed_unsuccessful_process, mocker, capsys):
        mock_subprocess_run = mocker.patch("src.utils.subprocess.run")
        mock_subprocess_run.return_value = completed_unsuccessful_process

        run_shell("test_command", check=False)

        captured = capsys.readouterr()

        assert "Mocking terminated process" in captured.err

    def test_run_shell_exception(self, mocker):
        mocker.patch("src.utils.subprocess.run", side_effect = Exception)
        assert run_shell("test_command", check=False) == None