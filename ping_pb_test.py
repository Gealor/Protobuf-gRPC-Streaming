from pathlib import Path

from pb import ping_pb2
from logger import log

BASE_DIR = Path(__file__).resolve().parent

PING_FILEPATH = BASE_DIR / "ping.bin"

def write(file_path: Path, obj: ping_pb2.Ping) -> None:
    with file_path.open("wb") as file:
        file.write(obj.SerializeToString())

def read(file_path: Path) -> ping_pb2.Ping:
    ping = ping_pb2.Ping()
    log.info("[reading before] isInitializing: %s", ping.IsInitialized()) # False
    with file_path.open(mode="rb") as file:
        ping.ParseFromString(file.read())
    
    log.info("[reading after] isInitializing: %s", ping.IsInitialized()) # True
    return ping


def main() -> None:
    ping = ping_pb2.Ping()
    log.info(ping.ok)
    log.info("[first before] isInitializing: %s", ping.IsInitialized()) # False с proto2
    ping.ok = True
    log.info("[first after] isInitializing: %s", ping.IsInitialized()) # True
    
    log.info("ping: %s, %s", ping.SerializeToString(), ping)

    write(PING_FILEPATH, ping)

    new_ping = read(PING_FILEPATH)
    log.info("new_ping: %s, %s", new_ping.SerializeToString(), new_ping)



if __name__ == "__main__":
    main()