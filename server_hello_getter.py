from concurrent import futures
import random
from typing import Generator, Iterator

import grpc

from pb import hello_service_pb2_grpc, hello_service_pb2
from logger import log


class HelloServiceServicer(hello_service_pb2_grpc.HelloServiceServicer):
    def multiHello(
        self,
        request_iterator: Iterator[hello_service_pb2.Hello],
        context: grpc.ServicerContext,
    ) -> hello_service_pb2.MultiHelloResponse:
        log.info("Got multi request for Hello %s", request_iterator)
        greetings = []
        for request in request_iterator:
            log.info("The request for multi Hello: %s", request)
            greetings.append(request)

        return hello_service_pb2.MultiHelloResponse(
            title=f"This is response for multi Hello. Total count: {len(greetings)}",
            greetings=greetings,
        )
        

def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_service_pb2_grpc.add_HelloServiceServicer_to_server(HelloServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    log.info("Start serving...")
    server.start()
    server.wait_for_termination()

def main():
    try:
        serve()
    except KeyboardInterrupt:
        log.info("Received keyboard interrupt, shutting down")
        exit()

if __name__=="__main__":
    main()