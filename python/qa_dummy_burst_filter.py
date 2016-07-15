#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file
# @author Roman Khassraf <rkhassraf@gmail.com>
# @section LICENSE
# 
# Gr-gsm is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# Gr-gsm is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with gr-gsm; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 
# 

from gnuradio import gr, gr_unittest, blocks
import grgsm_swig as grgsm

class qa_dummy_burst_filter (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001 (self):
        """
            filter mode less_or_equal, limiting frame number 1500123
            24 bursts as input, 10 of them dummy bursts
        """
        framenumbers_input = [1259192, 1076346, 1076242, 235879, 1259218, 2194302, 2714322, 1588, 1259244, 1563637, 1435624, 1928543, 503726, 1571144, 2658397, 1807445, 869789, 624070, 2005511, 1306953, 2284894, 1600339, 551375, 1259270]
        timeslots_input = [6, 3, 4, 3, 5, 3, 2, 7, 1, 6, 0, 7, 2, 3, 2, 0, 7, 1, 0, 6, 0, 6, 5, 7]
        bursts_input = [
            "0001100001000111100111101111100101000100101011000010011110011101001111101100010100111111100000110100011111101011101100100111110011000100010001010000",
            "0001000101000000001001111110000110010110110111110111101000001101001111101100010100111111001110001001110101110001010001000111011010010001011011000000",
            "0001111101101110110000010100100111000001001000100000001111100011100010111000101110001010111010010100011001100111001111010011111000100101111101010000",
            "0000010010100000001001101010100001011100010001101100111111101101001111101100010100111111101101001110100010101110010110101111100010010000110010110000",
            "0000010101010110010011110101010101101100000000001000100100101010000111011101001000011101011101110000101011001111000100001000000000001110010001111000",
            "0001000000000010111010100000010101000010001010111010000000011010000111011101001000011101000000100010111110101000000001000000000010111010100000000000",
            "0001111101101110110000010100100111000001001000100000001111100011100010111000101110001010111010010100011001100111001111010011111000100101111101010000",
            "0000000000111110101010100001000000100010101110101010000101001010000111011101001000011101001010001111101010001000010000000000101110101010100000010000",
            "0001111101101110110000010100100111000001001000100000001111100011100010111000101110001010111010010100011001100111001111010011111000100101111101010000",
            "0001111101101110110000010100100111000001001000100000001111100011100010111000101110001010111010010100011001100111001111010011111000100101111101010000",
            "0001111101101110110000010100100111000001001000100000001111100011100010111000101110001010111010010100011001100111001111010011111000100101111101010000",
            "0001111101101110110000010100100111000001001000100000001111100011100010111000101110001010111010010100011001100111001111010011111000100101111101010000",
            "0001000100000011001010111001111100011010000000000000001001001010000111011101001000011101010110000101111010011001110110001001011010101000011110110000",
            "0001100001000111111111100001011000000011010110111010110000111010000111011101001000011101100010111100100101110001101000110100110000001010101110011000",
            "0000000100111011000000000010100100001100101010000000010010101010000111011101001000011101000110110001110110000100110100110110011001100100000101100000",
            "0000100101111010011110111010100111010100011011011101100111001010000111011101001000011101010000111010000110100000001000010011101011001001110100011000",
            "0001111101101110110000010100100111000001001000100000001111100011100010111000101110001010111010010100011001100111001111010011111000100101111101010000",
            "0000110101000011011010110000110011010000000001001010110010001010000111011101001000011101010000011000111001101110000000110010100001101110101000100000",
            "0001111101101110110000010100100111000001001000100000001111100011100010111000101110001010111010010100011001100111001111010011111000100101111101010000",
            "0001111101101110110000010100100111000001001000100000001111100011100010111000101110001010111010010100011001100111001111010011111000100101111101010000",
            "0001100010000001000111011100101101101010100001111101001000101010000111011101001000011101111010000011010110010111011111010010001000001101100011111000",
            "0001111101101110110000010100100111000001001000100000001111100011100010111000101110001010111010010100011001100111001111010011111000100101111101010000",
            "0000001000100011000000000000110100000000010000001010100100001010000111011101001000011101000010010000000000001001000001011000000001010000000100010000",
            "0000100000110001000000000100000110001011100001001000000000001010000111011101001000011101001010010001010000000111010000000011000001000000000101010000",
        ]

        bursts_expected = [
            "0001100001000111100111101111100101000100101011000010011110011101001111101100010100111111100000110100011111101011101100100111110011000100010001010000",
            "0001000101000000001001111110000110010110110111110111101000001101001111101100010100111111001110001001110101110001010001000111011010010001011011000000",
            "0000010010100000001001101010100001011100010001101100111111101101001111101100010100111111101101001110100010101110010110101111100010010000110010110000",
            "0000010101010110010011110101010101101100000000001000100100101010000111011101001000011101011101110000101011001111000100001000000000001110010001111000",
            "0001000000000010111010100000010101000010001010111010000000011010000111011101001000011101000000100010111110101000000001000000000010111010100000000000",
            "0000000000111110101010100001000000100010101110101010000101001010000111011101001000011101001010001111101010001000010000000000101110101010100000010000",
            "0001000100000011001010111001111100011010000000000000001001001010000111011101001000011101010110000101111010011001110110001001011010101000011110110000",
            "0001100001000111111111100001011000000011010110111010110000111010000111011101001000011101100010111100100101110001101000110100110000001010101110011000",
            "0000000100111011000000000010100100001100101010000000010010101010000111011101001000011101000110110001110110000100110100110110011001100100000101100000",
            "0000100101111010011110111010100111010100011011011101100111001010000111011101001000011101010000111010000110100000001000010011101011001001110100011000",
            "0000110101000011011010110000110011010000000001001010110010001010000111011101001000011101010000011000111001101110000000110010100001101110101000100000",
            "0001100010000001000111011100101101101010100001111101001000101010000111011101001000011101111010000011010110010111011111010010001000001101100011111000",
            "0000001000100011000000000000110100000000010000001010100100001010000111011101001000011101000010010000000000001001000001011000000001010000000100010000",
            "0000100000110001000000000100000110001011100001001000000000001010000111011101001000011101001010010001010000000111010000000011000001000000000101010000"
        ]

        dummy_burst_filter = grgsm.dummy_burst_filter()
        
        src = grgsm.burst_source(framenumbers_input, timeslots_input, bursts_input)
        sink = grgsm.burst_sink()

        self.tb.msg_connect(src, "out", dummy_burst_filter, "in")
        self.tb.msg_connect(dummy_burst_filter, "out", sink, "in")

        self.tb.run()

        bursts_result = list(sink.get_burst_data())
        
        self.assertEqual(bursts_expected, bursts_result)


if __name__ == '__main__':
    gr_unittest.run(qa_dummy_burst_filter, "qa_dummy_burst_filter.xml")
