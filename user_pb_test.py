from pathlib import Path

from pb import user_pb2
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
    user = user_pb2.User()
    log.info(user.name)
    log.info("[first before] isInitializing: %s", user.IsInitialized()) # False с proto2

    log.info("user: %s", user) # ' '
    log.info("user.status: %s", user.status) # 0

    log.info("User Status Enum: %s", user_pb2.User.Status)
    log.info("User Status Enum values: %s", user_pb2.User.Status.items())

    user = user_pb2.User(
        id = 42,
        name = "John",
        email = "john@example.com",
        status=user_pb2.User.Status.PROSPECT,
    )
    log.info("[first after] isInitializing: %s", user.IsInitialized()) # False
    
    
    log.info("user: %s, %s", user.SerializeToString(), user)

    write(USER_FILEPATH, user)

    new_user = read(USER_FILEPATH)
    log.info("new_user: %s, %s", new_user.SerializeToString(), new_user)



if __name__ == "__main__":
    main()