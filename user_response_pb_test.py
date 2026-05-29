from pathlib import Path

from pb import user_pb2, user_response_pb2
from logger import log

BASE_DIR = Path(__file__).resolve().parent

USER_FILEPATH = BASE_DIR / "user_file.bin"

def write(file_path: Path, obj: user_pb2.User) -> None:
    with file_path.open("wb") as file:
        file.write(obj.SerializeToString())

def read(file_path: Path) -> user_pb2.User:
    user = user_pb2.User()
    log.info("[reading before] isInitializing: %s", user.IsInitialized()) # False
    with file_path.open(mode="rb") as file:
        user.ParseFromString(file.read())
    
    log.info("[reading after] isInitializing: %s", user.IsInitialized()) # True
    return user


def main() -> None:
    user_john = user_pb2.User(
        id = 42,
        name = "John",
        email = "john@example.com",
        status=user_pb2.User.Status.PROSPECT,
    )
    user_sam = user_pb2.User(
        id = 33,
        name = "Sam",
        email = "sam@example.com",
        status=user_pb2.User.Status.ACTIVE,
    )
    user_nick = user_pb2.User(
        id = 27,
        name = "Nick",
        status=user_pb2.User.Status.BLOCKED,
    )

    users = [
        user_john, 
        user_sam,
        user_nick,
    ]
    response_meta = user_response_pb2.ResponseMeta(
        page = 1,
        total = len(users),
        pageSize = max(len(users), 10),
    )
    users_response = user_response_pb2.UserResponse(
        users = users,
        meta = response_meta,
    )
    
    log.info("users response: %s", users_response)
    
    
    # log.info("user: %s", user.SerializeToString(), user)

    # write(USER_FILEPATH, user)

    # new_user = read(USER_FILEPATH)
    # log.info("new_user: %s", new_user.SerializeToString(), new_user)



if __name__ == "__main__":
    main()