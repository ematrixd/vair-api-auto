# Инсталяция

<details>
  <summary>Версионность</summary>

  - Python 3.9 и выше
  - VAIR 3.8.0 и выше
</details>

### Скачать проект

```plaintext
git clone https://github.com/ematrixd/vair-api-auto.git
```

### Перейти в директорию проекта

```plaintext
cd vair-api-auto
```

### Установить venv

```plaintext
python3 -m venv venv
```

### Подключение к venv

```plaintext
source venv/bin/activate
```

### Установка зависимостей

```plaintext
pip3 install pyyaml click requests

```

### Настроить config.ini

```plaintext
[node]
uri = http # Протокол соединения ( оставить http )
host = # указать ip адрес MGR
login = # Логин от веб интерфейса
password = # Пароль от веб интерфейса
version = 3.8.3 # Указать вашу версию vair
[api]
api_doc = apidoc/openapi.json # url swagger docs ( оставить по умолчанию )
```

### Пример запуска yaml файла

```plaintext
python3 start.py start-yaml yaml_auto/example/createVD.yaml
```

Это документация, которая показывает процесс установки и использование проекта.  

@ Разработано при поддержке АЭРОДИСК
