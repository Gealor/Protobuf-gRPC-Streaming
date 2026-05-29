from time import sleep
from typing import Iterator

import grpc
from faker import Faker

from pb import user_service_pb2, user_service_pb2_grpc
from logger import log

fake = Faker()

type IteratorResponse = Iterator[user_service_pb2.UserResponse]

def get_user_by_id(stub: user_service_pb2_grpc.UserGetterStub) -> None:
    response = stub.GetUserById(user_service_pb2.UserRequestById(id=5))
    log.info("User by id received:\n %s", response.user)

def get_user_by_name(stub: user_service_pb2_grpc.UserGetterStub) -> None:
    response = stub.GetUserByName(user_service_pb2.UserRequestByName(name='Gealor'))
    log.info("User by name received:\n %s", response.user)

def get_matching_users_by_name(stub: user_service_pb2_grpc.UserGetterStub) -> None:
    name = fake.name()
    user_request = user_service_pb2.UserRequestByName(name = name)
    response: IteratorResponse = stub.GetAllUsersMatchingUsername(
        user_request
    )
    for user_data in response:
        log.info(
            "Got user by name: \n%s, response:\n%s",
            user_request.name,
            user_data.user
        )
        sleep(1)

def run() -> None:
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_service_pb2_grpc.UserGetterStub(channel)
        # get_user_by_id(stub)
        # get_user_by_name(stub)
        get_matching_users_by_name(stub)

def main():
    try:
        run()
    except KeyboardInterrupt:
        log.info("Received keyboard interrupt, shutting down")
        exit()

if __name__=="__main__":
    main()