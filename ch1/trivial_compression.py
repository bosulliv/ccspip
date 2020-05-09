# -*- coding: utf-8 -*-
"""
Work with nucleotide sequences
"""

class CompressedGene:
    """ Efficient storage of gene strings in binary """
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        """ Turn string into binary encoding """
        # start with 1, the sentinel
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            # shift left 2 bits
            self.bit_string <<= 2
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == 'C':
                self.bit_string |= 0b01
            elif nucleotide == 'G':
                self.bit_string |= 0b10
            elif nucleotide == 'T':
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self) -> str:
        """ Turn bits back into string """
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            # shift to the 2 bits of interest, then mask the next
            # two bits
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()

if __name__ == '__main__':
    from sys import getsizeof
    original: str = \
        "TAGGGATTAACCGTTATATATATATAT" * 100
    print("Original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)
    print("Compresssed is {} bytes".format(getsizeof(compressed)))
    truth = original == compressed.decompress()
    print("original and decompressed are the same: {}".format(truth))
    