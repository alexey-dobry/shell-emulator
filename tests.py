import unittest
import time
from emulator import ShellEmulator

class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        """Подготовка перед каждым тестом"""
        self.emulator = ShellEmulator(user_name="some_buddy",path_to_arxiv="./file.zip", path_to_script=None)

    def test_ls_root(self):
        """Тест команды ls в корневой директории"""
        result = self._capture_output(self.emulator.ls, [])
        self.assertIn('new_folder', result)  # Проверяем, что 'new_folder' присутствует в выводе

    def test_cd_and_ls(self):
        """Тест команды cd и ls внутри папки"""
        self.emulator.cd(["new_folder"])  # Переходим в папку 'new_folder'
        result = self._capture_output(self.emulator.ls, [])
        self.assertIn('content', result)  # Проверяем, что 'content' находится в 'new_folder'

    def test_cd_back_to_root(self):
        """Тест команды cd для возвращения в корневую директорию"""
        self.emulator.cd(["new_folder"])  # Переходим в папку 'new_folder'
        self.emulator.cd([".."])  # Возвращаемся в корневую директорию
        self.assertEqual(self.emulator.cwd, "/")  # Проверяем, что текущая директория - это корень
    
    def test_cd_absolute_path(self):
        """Тест команды  cd для перемещения по абсолютному пути"""
        self.emulator.cd(["/new_folder/content"])
        self.assertEqual(self.emulator.cwd,"/new_folder/content/") # Проверка, что текущий путь это введенный путь

    def test_uname(self):
        """Тест команды uname"""
        result = self._capture_output(self.emulator.uname, [])
        self.assertEqual(result.strip(), "Linux")  # Проверяем, что команда uname возвращает 'Linux'

    def test_uname_with_a(self):
        """Тест команды uname с опцией -a"""
        result = self._capture_output(self.emulator.uname, ["-a"])
        self.assertIn("Linux some_buddy 5.15.0-1-generic x86_64 GNU/Linux\n", result)  # Проверяем вывод с опцией -a
    def test_uname_with_bad_flag(self):
        """Тест команды uname с неправильным флагом"""
        result = self._capture_output(self.emulator.uname, ["-cheeseburger"])
        self.assertIn("No such flag",result)

    def test_cd_nonexistent_directory(self):
        """Тест ошибки при переходе в несуществующую директорию"""
        result = self._capture_output(self.emulator.cd, ["none_dir"])
        self.assertIn("No such file or directory", result)  # Проверяем, что выводится сообщение об ошибке
    
    def test_mkdir_in_root(self):
        """Тест mkdir в корневой директории"""
        self.emulator.mkdir(["2_directory"])
        result = self._capture_output(self.emulator.ls, [])
        self.assertIn('2_directory', result) # Проверяем, что в выводе ls появилась созданная директория
    
    def test_mkdir_in_folder(self):
        """Тест mkdir в другой директории"""
        self.emulator.cd(["new_folder"])
        self.emulator.mkdir(["another_dir"])
        result = self._capture_output(self.emulator.ls, [])
        self.assertIn('another_dir',result) # Проверяем, что в выводе ls появилась созданная директория
    
    def test_mkdir_bad_name(self):
        """Тест mkdir с недопустимым названием"""
        result = self._capture_output(self.emulator.mkdir, ['/'])
        self.assertIn('Name is not allowed',result)

    def test_exit(self):
        """Тест команды exit"""
        with self.assertRaises(SystemExit):  # Ожидаем завершения программы
            self.emulator.exit()

    def _capture_output(self, func, args):
        from io import StringIO
        import sys
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            func(args)
            return out.getvalue()
        finally:
            sys.stdout = saved_stdout

if __name__ == '__main__':
    unittest.main()
