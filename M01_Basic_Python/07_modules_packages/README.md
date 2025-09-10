# M1.7 — Модули и пакеты

## 🎯 Цели модуля
- Понять устройство модулей и пакетов в Python (`import`, `__main__`, `__all__`).
- Научиться строить структуру пакета с подмодулями и утилитами.
- Освоить создание CLI через `argparse` (флаги, подкоманды, валидация).
- Научиться работать с файловой системой (`pathlib`, `os`) и сохранять данные через сериализацию (`JSON`, `Pickle`).
- Освоить работу с датами и временем (`datetime`, `zoneinfo`).
- На практике использовать стандартные библиотеки: `random`, `collections`, `functools`, `itertools`.

## 📂 Структура модуля
```
M01_Basic_Python/
└── 07_modules_packages/
    ├── step01_module/
    ├── step02_imports/
    ├── step03_main_guard/
    ├── step04_calculator_pkg/
    ├── step05_cli_argparse/
    ├── step06_storage_pathlib_os/
    ├── step07_json_pickle/
    ├── step08_datetime/
    ├── step09_random/
    ├── step10_collections/
    ├── step11_functools/   (запланировано)
    └── step12_itertools/   (запланировано)
```

## 📊 Прогресс по шагам
| Шаг | Тема                         | Статус | Основные файлы |
|-----|------------------------------|--------|----------------|
| 01  | импорты                      | ✅ | `check_import.py` |
| 02  | структура пакета             | ✅ | `app/main.py`, `core/operations.py` |
| 03  | __main__                     | ✅ | `runner.py`, `app/main.py` |
| 04  | __all__ / calculator pkg     | ✅ | `calculator/*.py` |
| 05  | CLI через argparse           | ✅ | `app/main.py` |
| 06  | работа с файловой системой   | ✅ | `utils/storage.py` |
| 07  | сериализация (JSON/Pickle)   | ✅ | `data/history.json`, `data/history.pkl` |
| 08  | datetime                     | ✅ | `utils/utils_datetime.py`, practice tasks |
| 09  | random                       | ✅ | `task01_seed_repeat.py` … `task13_queue_simulation.py` |
| 10  | collections.Counter          | ✅ | `task01_point_distance.py` … `task12_lru_cache_sim.py` |
| 11  | functools.lru_cache          | ❌ | запланировано |
| 12  | itertools                    | ❌ | запланировано |

## ▶️ Запуск (примеры)
```bash
python -m app.main --help
python -m app.main add 2 3 --show-history
python task01_point_distance.py  # пример запуска из step10
```

## 📦 Зависимости
- Python 3.13
- Все зависимости указаны в `requirements.txt` (в корне модуля).

## 📝 Мини-итог
- Получен практический опыт построения пакетов и создания CLI-приложений.
- Освоена работа с файловой системой через `pathlib` и `os`.
- Реализовано сохранение и загрузка данных в форматах JSON и Pickle.
- Изучены работа с датами, часовыми поясами и форматированием времени.
- Применены стандартные библиотеки (`random`, `collections`) для практических задач.
- Следующие шаги: изучение `functools.lru_cache` и `itertools`.
