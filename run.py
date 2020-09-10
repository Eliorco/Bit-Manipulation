class BitOperators:
    """
    Simple Wrapper that commit bit operation as a function
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

    Class that gather all basic Bit manipulation and demonstrate it with explained prints
    """
    b = BitOperators()

    @staticmethod
    def _create_mask(size: int) -> int:
        return (1 << size)

    @classmethod
    def get_the_ith_bit(cls, binary_num: int, i: int) -> int:
        mask = cls._create_mask(i)
        print(f'create a mask: move 1 bit i={i} times left(multiply it by 2) --> {bin(mask)[2:]}')
        bit_is_on = (binary_num & mask) != 0
        print(f'Commit AND operator between {bin(mask)[2:]} & {bin(binary_num)[2:]} --> {binary_num & mask}')
        return 1 if bit_is_on else 0

    @classmethod
    def set_the_ith_bit(cls, binary_num: int, i: int) -> int:
        """

        :param binary_num: decimal number that need to adjust
        :param i: the index of the wished bit
        :return: decimal number with the new bit
        """
        mask = cls._create_mask(i)
        print(f'create a mask: move 1 bit i={i} times left(multiply it by 2) --> {bin(mask)[2:]}')
        bit_is_set = (binary_num | mask)
        print(f'Commit OR operator between {bin(mask)[2:]} | {bin(binary_num)[2:]} --> {binary_num | mask}')
        return bit_is_set

    @classmethod
    def clear_ith_bit(cls, binary_num: int, i: int) -> int:
        """
        Go to the ith bit and clear it
        :param binary_num: decimal number that need to adjust
        :param i: the index of the wished bit to be modified
        :return: new decimal number by the cleared bit
        """
        # k = 1 << i
        mask = cls.b._not(cls._create_mask(i)) # equivalent to ~(1 << i)
        # mask = f'{"0" * (len(bin(23)[2:]) - len(bin(k)[2:]))}{bin(k)[2:]}'
        print(bin(mask))
        print(f'create a mask: move 1 bit i={i} times left(multiply it by 2) and negate it (python show it different) --> {bin(mask)[2:]}')
        bit_is_cleared = binary_num & mask
        print(f'Commit AND operator between {bin(mask)[2:]} & {bin(binary_num)[2:]} --> {bit_is_cleared}')
        return bit_is_cleared

    @classmethod
    def clear_MSB_to_i_bits(cls, binary_num: int, i: int) -> int:
        mask = cls._create_mask(i) - 1 # to create sequence of i 1s
        print(mask)
        print(f'create a mask: move 1 bit i={i} times left(multiply it by 2) --> {bin(mask)[2:]}')
        bit_is_cleared = binary_num & mask
        print(f'Commit AND operator between {bin(mask)[2:]} & {bin(binary_num)[2:]} --> {bit_is_cleared}')
        return bit_is_cleared


    @classmethod
    def clear_i_to_LSB_bits(cls, binary_num: int, i: int) -> int:
        mask = (-1 << i + 1)
        print(mask)
        print(f'create a mask: move 1 bit i={i} times left(multiply it by 2) --> {bin(mask)[2:]}')
        bit_is_cleared = binary_num & mask
        print(f'Commit AND operator between {bin(mask)[2:]} & {bin(binary_num)[2:]} --> {bit_is_cleared}')
        return bit_is_cleared

    @classmethod
    def update_ith_bit(cls, binary_num: int, i: int, bit: bool = False) -> int:
        val = bit
        mask = cls.b._not(cls._create_mask(i))
        print(bin(mask))
        print(f'create a mask: move 1 bit i={i} times left(multiply it by 2) and negate it (python show it different) --> {bin(mask)[2:]}')
        print(f'bit is: {bit}')
        bit_is_updated = binary_num & mask
        print(f'Commit AND operator between {bin(mask)[2:]} & {bin(binary_num)[2:]} --> {bit_is_updated}')
        result = bit_is_updated | (val << i)
        print(f'Commit OR operator between {bit_is_updated} | {(val << i)} --> {result}')
        return result