import subprocess

def execute_command(command, text):
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        return text in output
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def test_list_files(command, expected_files):
    assert execute_command(command, '\n'.join(expected_files)) == True, f"Ошибка: файлы {expected_files} не найдены"

def test_extract_archive(command, expected_files):
    assert execute_command(command, '\n'.join(expected_files)) == True, f"Ошибка: файлы {expected_files} не удалось разархивировать"

test_extract_archive("unzip -j archive.zip", ["file1.txt", "file2.txt", "file3.txt"])

test_list_files("ls", ["file1.txt", "file2.txt", "file3.txt"])