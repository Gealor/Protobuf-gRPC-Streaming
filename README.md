# Тема

Изучение ProtoBuf и gRPC

# Протокол Ping

1. Описали простой протокол Ping

2. Скачиваем protobuf

    ```cli
    uv add protobuf
    ```

3. Скачиваем protoc

    ```cli
    winget install protobuf
    ```

4. Выяснили, что есть пакет mypy-protobuf, который позволяет сгенерировать интерфейсы сообщений и сервисов.

    ```cli
    uv add mypy-protobuf
    ```

5. Скомпилировать ping.proto, вместе с mypy генерируем интерфейс

    ```cli
    protoc --python_out=./pb --mypy_out=./pb proto/ping.proto
    ```

6. Сделали запись в файл и чтение из него

7. Проверили 'ping.IsInitialized()'

# Протокол User

1. Описали протокол User, использовали разные типы и написали свой enum

2. Скомпилировали протокол

    ```cli
    protoc --python_out=./pb --mypy_out=./pb proto/user.proto
    ```

3. В protoc параметр --proto_path указывает папку, относительно которой будет производиться поиск .proto файлов при импорте.

    ```cli
    protoc --proto_path=proto --python_out=./pb proto/* 
    ```

    Т.е. тут будет производиться поиск относительно папки proto (где у нас сразу лежат .proto файлы)

4. Так же узнали, что вместо --mypy_out можно использовать --pyi_out, но по реализации он будет отличаться от того, что дает --mypy_out.

    ```cli
    protoc --proto_path=proto --python_out=./pb --pyi_out=./pb proto/* 
    ```

5. Импорты правим вручную, если протокол импортирует из другого протокола

# Сервис UserGetter

1. Описываем сервис UserGetter и сигнатуру его методов

2. Описываем протоколы запросы и ответа

3. Ставим пакет grpcio-tools

    ```cli
    uv add "grpcio-tools==1.80.0" "protobuf>=6.31.1,<7.0.0"
    ```

4. Компилируем протокол в сервис и stub, перешли на grpcio-tools

    ```cli
    python -m grpc_tools.protoc --proto_path=proto --python_out=./pb --pyi_out=./pb --grpc_python_out=./pb proto/*_service.proto
    ```

5. Все остальное генерируем как обычно

    ```cli
    protoc --proto_path=proto --python_out=./pb --pyi_out=./pb proto/* 
    ```
