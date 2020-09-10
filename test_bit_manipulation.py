from unittest import TestCase
from run import BitManipulation


class TestBitManipulation(TestCase):

    def setUp(self):
        self.bm = BitManipulation()

    def test__create_mask(self):
        """
        creating simple mask
        :return: mask with i shifts to the left => '10000'
        """
        mask = self.bm._create_mask(4)
        self.assertEqual(16, mask)

    def test_get_the_ith_bit(self):
        """    16 8 4 2 1
        23 =>  '1 0 1 1 1'
        index:  4 3 2 1 0
        :return: bit at index 4 => 16 == 1
        """
        self.assertEqual(1, self.bm.get_the_ith_bit(23, 4))

    def test_set_the_ith_bit(self):
        """
        setting the 8 bit to 1
                  16 8 4 2 1
        input =>  '1 0 1 1 1'
        index:     4 3 2 1 0
        :return: 31  =>  '1 1 1 1 1'
        """
        self.assertEqual(31, self.bm.set_the_ith_bit(23, 3))

    def test_clear_ith_bit(self):
        """
        clearing the 8 bit to 0
                  16 8 4 2 1
        input =>  '1 1 1 1 1'
        index:     4 3 2 1 0
        :return: 23  =>  '1 0 1 1 1'
        """
        self.assertEqual(23, self.bm.clear_ith_bit(31, 3))

    def test_clear_MSB_to_i_bits(self):
        """
        clearing the MSB bit to ith bit to 0, index 4,3
                  16 8 4 2 1
        input =>  '1 1 1 1 1'
        index:     4 3 2 1 0
        :return: 3  =>  '0 0 0 1 1'
        """
        self.assertEqual(3, self.bm.clear_MSB_to_i_bits(31, 2))

    def test_clear_i_to_LSB_bits(self):
        """
        clearing the 8 bit to LSB to 0, index 2,1,0
                  16 8 4 2 1
        input =>  '1 1 1 1 1'
        index:     4 3 2 1 0
        :return: 24  =>  '1 1 0 0 0'
        """
        self.assertEqual(24, self.bm.clear_i_to_LSB_bits(31, 2))

    def test_update_ith_bit(self):
        """
        updating the 8 bit to 1 and the 2 bit to 0
                  16 8 4 2 1
        input =>  '1 0 1 1 1'
        index:     4 3 2 1 0
        :return: 31  =>  '1 1 1 1 1'
        and
        :return: 21  =>  '1 0 1 0 1'
        """
        self.assertEqual(31, self.bm.update_ith_bit(23, 3, True))
        self.assertEqual(21, self.bm.update_ith_bit(23, 1))
