import random
from typing import Iterator

import grpc
from faker import Faker

from pb import hello_service_pb2_grpc, hello_service_pb2
from logger import log

fake = Faker()


def create_many_greetings(n: int) -> Iterator[hello_service_pb2.Hello]:
    log.info("Creating %d greetings", n)
    for idx in range(1, n+1):
        name = fake.name()
        description = f"Hello!!! This is message from {name}!"
        yield hello_service_pb2.Hello(
            name=name,
            text=description,
        )
    

def send_many_greetings(stub: hello_service_pb2_grpc.HelloServiceStub):
    '''
    Если у нас streaming со стороны пользователя, 
    а мы возвращаем с сервера только один ответ, то на вход клиент должен подавать ИТЕРАТОР
    '''
    greetings_count = random.randint(1, 6)

    greetings_request = create_many_greetings(greetings_count)
    response: hello_service_pb2.MultiHelloResponse = stub.multiHello(greetings_request) 
    log.info(
        "Got response with title: %r\n Received: %s",
        response.title,
        response.greetings,
    )


def run() -> None:
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_service_pb2_grpc.HelloServiceStub(channel)
        send_many_greetings(stub)

def main():
    try:
        run()
    except KeyboardInterrupt:
        log.info("Received keyboard interrupt, shutting down")
        exit()

if __name__=="__main__":
    main()