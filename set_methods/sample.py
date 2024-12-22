import logging


# Cấu hình logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Logger cho module này
logger = logging.getLogger(__name__)

# Định nghĩa original_set
original_set: set = {
    1,
    2,
    1,
    4,
    2,
    1,
    2,
    5,
    6,
    3,
}


def create_set_sample() -> None:
    # Hàm này sẽ hoạt động bình thường vì chỉ được thực thi sau khi gọi
    new_set: set = original_set.copy()

    original_set.add(9)
    new_set.add(9)

    # Sử dụng các level logging khác nhau
    logger.debug(f"New set content: {new_set}")
    logger.info(f"Sets are equal: {new_set == original_set}")

    if len(new_set) > 5:
        logger.warning("Set size is larger than 5 elements")


create_set_sample()
