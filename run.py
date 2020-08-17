import os

class BitOperators:
    """
    Receive decimal number and return decimal number
    after changing it to binary
    compute it and
    return it to decimal number
    """
    @classmethod
    def _not(cls, first: int) -> int:
        return int(~first)

    @classmethod
    def _and(cls, first: int, second: int) -> int:
        return int(first & second)

    @classmethod
    def _or(cls, first: int, second: int) -> int:
        return int(first | second)

    @classmethod
    def _xor(cls, first: int, second: int) -> int:
        return int(first ^ second)

class BitManipulation:
    """
    Class that gather all major bit manipulation and show it the easiest way
    """
    b = BitOperators()

    @classmethod
    def _get_the_ith_bit(cls, binary_num: int, i: int) -> int:
        mask = (1 << i)
        print(f'create a mask: move 1 bit i={i} times left(multiply it by 2) --> {bin(mask)[2:]}')
        bit_is_on = (binary_num & mask) != 0
        print(f'Commit AND operator between {bin(mask)[2:]} & {bin(binary_num)[2:]} --> {binary_num & mask}')
        return 1 if bit_is_on else 0

    @classmethod
    def _set_the_ith_bit(cls, binary_num: int, i: int) -> int:
        """

        :param binary_num: decimal number that need to adjust
        :param i: the index of the wished bit
        :return: decimal number with the new bit
        """
        mask = (1 << i)
        print(f'create a mask: move 1 bit i={i} times left(multiply it by 2) --> {bin(mask)[2:]}')
        bit_is_set = (binary_num | mask)
        print(f'Commit OR operator between {bin(mask)[2:]} | {bin(binary_num)[2:]} --> {binary_num | mask}')
        return bit_is_set

    @classmethod
    def _clear_ith_bit(cls, binary_num: int, i: int) -> int:
        """
        Go to the ith bit and clear it
        :param binary_num: decimal number that need to adjust
        :param i: the index of the wished bit to be modified
        :return: new decimal number by the cleared bit
        """
        # k = 1 << i
        mask = -(1 << i) -1 # equivalent to ~(1 << i)
        # mask = f'{"0" * (len(bin(23)[2:]) - len(bin(k)[2:]))}{bin(k)[2:]}'
        print(bin(mask))
        print(f'create a mask: move 1 bit i={i} times left(multiply it by 2) and negate it (python show it different) --> {bin(mask)[2:]}')
        bit_is_cleared = binary_num & mask
        print(f'Commit AND operator between {bin(mask)[2:]} & {bin(binary_num)[2:]} --> {bit_is_cleared}')
        return bit_is_cleared

    @classmethod
    def _clear_MSB_to_i_bits(cls, binary_num: int, i: int) -> int:
        mask = (1 << i) - 1 # to create sequence of i 1s
        print(mask)
        print(f'create a mask: move 1 bit i={i} times left(multiply it by 2) --> {bin(mask)[2:]}')
        bit_is_cleared = binary_num & mask
        print(f'Commit AND operator between {bin(mask)[2:]} & {bin(binary_num)[2:]} --> {bit_is_cleared}')
        return bit_is_cleared


    @classmethod
    def _clear_i_to_LSB_bits(cls, binary_num: int, i: int) -> int:
        mask = (-1 << i + 1)
        print(mask)
        print(f'create a mask: move 1 bit i={i} times left(multiply it by 2) --> {bin(mask)[2:]}')
        bit_is_cleared = binary_num & mask
        print(f'Commit AND operator between {bin(mask)[2:]} & {bin(binary_num)[2:]} --> {bit_is_cleared}')
        return bit_is_cleared

    @classmethod
    def _update_ith_bit(cls, binary_num: int, i: int, bit: bool = False) -> int:
        val = bit
        mask = ~(1 << i)
        print(bin(mask))
        print(f'create a mask: move 1 bit i={i} times left(multiply it by 2) and negate it (python show it different) --> {bin(mask)[2:]}')
        print(f'bit is: {bit}')
        bit_is_updated = binary_num & mask
        print(f'Commit AND operator between {bin(mask)[2:]} & {bin(binary_num)[2:]} --> {bit_is_updated}')
        result = bit_is_updated | (val << i)
        print(f'Commit OR operator between {bit_is_updated} | {(val << i)} --> {result}')
        return result