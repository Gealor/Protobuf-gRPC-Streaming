from concurrent import futures
import random
from typing import Generator

import grpc

from pb import user_service_pb2_grpc, user_pb2, user_service_pb2
from logger import log


class UserGetterServicer(user_service_pb2_grpc.UserGetterServicer):
    @classmethod
    def get_random_user_from_username(cls, name: str) -> user_pb2.User:
        name_for_email = "".join(name.strip().split())
        user = user_pb2.User(
            id = random.randint(10, 100),
            name = name,
            email = f"{name_for_email}@example.com",
            status = random.choice(user_pb2.User.Status.keys()),
        )
        log.info("Generated user: \n%s", user)
        return user


    def GetUserById(
        self,
        request: user_service_pb2.UserRequestById,
        context: grpc.ServicerContext,
    ) -> user_service_pb2.UserResponse:
        log.info("Requested user by id: %d", request.id)
        name = f"user-{request.id:03d}"
        user = user_pb2.User(
            id = request.id,
            name = name,
            email = f"{name}@example.com",
            status = random.choice(user_pb2.User.Status.keys()),
        )
        log.info("Send user in response:\n%s", user)
        return user_service_pb2.UserResponse(
            user = user,
        )
    
    def GetUserByName(
        self,
        request: user_service_pb2.UserRequestByName,
        context: grpc.ServicerContext,
    ) -> user_service_pb2.UserResponse:
        log.info("Requested user by name: %s", request.name)
        user = self.get_random_user_from_username(name=request.name)
        log.info("Send user in response:\n%s", user)
        return user_service_pb2.UserResponse(
            user = user,
        )
    
    def GetAllUsersMatchingUsername(
        self,
        request: user_service_pb2.UserRequestByName,
        context: grpc.ServicerContext,
    ) -> Generator[user_service_pb2.UserResponse]:
        log.info("Requested matching users by username: %s", request.name)
        for idx in range(1, random.randint(3, 7)):
            user = self.get_random_user_from_username(
                name=f"{request.name} - {idx:02d}"
            )
            user_response = user_service_pb2.UserResponse(
                user = user
            )
            yield user_response



def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserGetterServicer_to_server(UserGetterServicer(), server)
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
        
