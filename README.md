# Проект Тестирования с использованием метода BDD и библиотеки Paspailleur

Данный проект представляет собой пример использования метода BDD (Behavior-Driven Development) для тестирования функционала с использованием библиотеки Paspailleur. 

## Описание

В этом проекте используется метод BDD для тестирования функционала библиотеки Paspailleur, которая предоставляет инструменты для анализа и обработки шаблонов данных. Создаются сценарии, описывающие ожидаемое поведение функций этой библиотеки, и затем автоматизируем их выполнение с использованием инструмента Behave.

## Структура проекта

- **features/**: Директория для хранения файлов сценариев на языке Gherkin.
- **steps/**: Директория для хранения файлов с шагами для сценариев BDD.
- **README.md**: Файл, который вы сейчас читаете.

## Установка и запуск

1. Клонируйте репозиторий на свой локальный компьютер:

https://github.com/Gonerr/BDD_Tests

2. Установите зависимости проекта:

pip install -r requirements.txt

3. Запустите тесты с помощью Behave (или auto_test.py):

behave
