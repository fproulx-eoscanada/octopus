# Global Ethereum-specific constant

DEFAULT_GAS_PER_TX = 90000
DEFAULT_GAS_PRICE = 50 * 10**9  # 50 gwei

BLOCK_TAG_EARLIEST = 'earliest'
BLOCK_TAG_LATEST = 'latest'
BLOCK_TAG_PENDING = 'pending'
BLOCK_TAGS = (
    BLOCK_TAG_EARLIEST,
    BLOCK_TAG_LATEST,
    BLOCK_TAG_PENDING,
)


TT256 = 2 ** 256
TT256M1 = 2 ** 256 - 1
TT255 = 2 ** 255
