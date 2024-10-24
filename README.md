# shell-emulator

## Общие сведения

Эмулятор Shell созданный в рамках домашнего задания по Конфигурационному управлению.

РТУ МИРЭА.Нехаенко Алексей.ИКБО-12-23

## Необходимые зависимости

python3.12

## Описание функционала

- ls - вывод всех объектов в текущей деректории
- pwd - вывод пути к текущей папке от корневой
- cd  <имя(путь_до)_директории> - переход в указанную директорию
- exit - выход из эмулятора
- uname - вывод имени системы
- uname -a - вывод полного имени системы
- makdir <имя_директории> - создание директории с указаным именем

## Запуск

python emulator.py <имя_пользователя> <путь_до_виртуальной_файловой_сиситемы> <путь_скрипта>

**Пример использования комманд cd и ls:**

![image](https://github.com/user-attachments/assets/5376ad3a-db0d-4a13-98f8-a4658effbb25)

**Пример использования команды mkdir:**

![image](https://github.com/user-attachments/assets/8677029f-84a8-4a7d-b781-1fa1b772a636)

**Пример использования команды uname:**

![image](https://github.com/user-attachments/assets/1c236efc-c699-4287-88e1-d0793d796e1c)

**Пример использования exit:**

![image](https://github.com/user-attachments/assets/3431b47d-9e53-4858-b4fe-9413022f824e)

## Тестирование

python -m unittest discover

**Скриншот тестирования:**

![test_config_hw1](https://github.com/user-attachments/assets/9e7c1e01-305b-40ac-8209-fdd4f2130f21)
