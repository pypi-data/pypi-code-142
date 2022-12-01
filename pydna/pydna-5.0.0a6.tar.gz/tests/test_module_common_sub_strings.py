#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest


def test_():
    from pydna import common_sub_strings

    a = "tcaaaaatcatcgcttcgctgattaattaccccagaaataaggctaaaaaactaatcgcattatcatcctatggttgttaatttgattcgttcatttgaaggtttgtggggccaggttactgccaatttttcctcttcataaccataaaagctagtattgtagaatctttattgttcggagcagtgcggcgcgaggcacatctgcgtttcaggaacgcgaccggtgaagacgaggacgcacggaggagagtcttccttcggagggctgtcacccgctcggcggcttctaatccgtacttcaatatagcaatgagcagttaagcgtattactgaaagttccaaagagaaggtttttttaggctaagataatggggctctttacatttccacaacatataagtaagattagatatggatagttatatggatatgtatatggtggtaatgccatgtaatatgattattaaacttctttgcgtccatccaaaaaaaaagtaagaatttttggatcaataacagtgtttgtggagcattttctgaatacaataaacccaaaacagaaacttcccttttgtatcactgttctggaaaaggggtgggcggtaataaagctaatagggtgtgtccataagtaatactgaacttggaaatgtgcggctttgcagcattttgtctttctataaaaatgtgtcgttcctttttttcattttttggcgcgtcgcctcggggtcgtatagaatatgcgtcacttttaaaaataagattgcagatcagggcaaaacaagtagcaaatcatagcaagagaccctgatttttgtgacataaatatttttacttctgtgttaggttaactttttatgtaactgtaaatggaatagagttgaggggatagtgcccacaagtcaatatgtttattttgtaaagttgaaagataattatttttatgctcaggtgattttggtgttgaattttctgtaatattaacataagagtaatacattgagtggttagtatatggtgtaaaagtggtataacgcatgtattaagagcagttatacaatatttggggccgctgaatgagatatagatattaaaatgtggataatcatgggctttatgggtaaatggaacagggtatagaccactgaggcaagtgccgtgcataatgatatgagtgcatctagtactgatttagtgagagatgggccgtggagtggaatgtgagagtagggtaagttgagagtggtatatacttgtagcatccgtgtgcgtatgccatatcagtatacaagtgaaggtgagtatggcaagtggtggtgggattggtataaagtggtagggtaagtatgtgtgtattatttacgatcgtgccatctgtgcagacaaacgcatcaggatttaaat"

    # a= "actctacgacttgatctttacgta"

    # 9772
    b = "ccggtgaagacgaggacgcacggaggagagtcttccttcggagggctgtcacccgctcggcggcttctaatccgtacttcaatatagcaatgagcagttaagcgtattactgaaagttccaaagagaaggtttttttaggctaagataatggggctctttacatttccacaacatataagtaagattagatatggatatgtatatggatatgtatatggtggtaatgccatgtaatatgattattaaacttctttgcgtccatccaacgagatctggcgcgccttaattaacccaacctgcattaatgaatcggccaacgcgcggattaccctgttatccctacatattgttcgcgccatctgtgcagacaaacgcatcaggattcagtactgacaataaaaagattcttgttttcaagaacttgtcatttgtatagtttttttatattgtagttgttctattttaatcaaatgttagcgtgatttatattttttttcgcctcgacatcatctgcccagatgcgaagttaagtgcgcagaaagtaatatcatgcgtcaatcgtatgtgaatgctggtcgctatactgctgtcgattcgatactaacgccgccatccagtgtcgaaaacgagctcgaattcatcgatgatatcagatccactagtggcctatgcggccgcggatctgccggtctccctatagtgagtcgatccggatttacctgaatcaattggcgaaattttttgtacgaaatttcagccacttcacaggcggttttcgcacgtacccatgcgctacgttcctggccctcttcaaacaggcccagttcgccaataaaatcaccctgattcagataggagaggatcatttctttaccctcttcgtctttgatcagcactgccacagagcctttaacgatgtagtacagcgtttccgctttttcaccctggtgaataagcgtgctcttggatgggtacttatgaatgtggcaatgagacaagaaccattcgagagtaggatccgtttgaggtttaccaagtaccataagatccttaaatttttattatctagctagatgataatattatatcaagaattgtacctgaaagcaaataaattttttatctggcttaactatgcggcatcagagcagattgtactgagagtgcaccatatgcggtgtgaaataccgcacagatgcgtaaggagaaaataccgcatcaggcgctcttccgcttcctcgctcactgactcgctgcgctcggtcgttcggctgcggcgagcggtatcagctcactcaaaggcggtaatacggttatccacagaatcaggggataacgcaggaaagaacatgtgagcaaaaggccagcaaaaggccaggaaccgtaaaaaggccgcgttgctggcgtttttccataggctccgcccccctgacgagcatcacaaaaatcgacgctcaagtcagaggtggcgaaacccgacaggactataaagataccaggcgtttccccctggaagctccctcgtgcgctctcctgttccgaccctgccgcttaccggatacctgtccgcctttctcccttcgggaagcgtggcgctttctcatagctcacgctgtaggtatctcagttcggtgtaggtcgttcgctccaagctgggctgtgtgcacgaaccccccgttcagcccgaccgctgcgccttatccggtaactatcgtcttgagtccaacccggtaagacacgacttatcgccactggcagcagccactggtaacaggattagcagagcgaggtatgtaggcggtgctacagagttcttgaagtggtggcctaactacggctacactagaaggacagtatttggtatctgcgctctgctgaagccagttaccttcggaaaaagagttggtagctcttgatccggcaaacaaaccaccgctggtagcggtggtttttttgtttgcaagcagcagattacgcgcagaaaaaaaggatctcaagaagatcctttgatcttttctacggggtctgacgctcagtggaacgaaaactcacgttaagggattttggtcatgaggggtaataactgatataattaaattgaagctctaatttgtgagtttagtatacatgcatttacttataatacagttttttagttttgctggccgcatcttctcaaatatgcttcccagcctgcttttctgtaacgttcaccctctaccttagcatcccttccctttgcaaatagtcctcttccaacaataataatgtcagatcctgtagagaccacatcatccacggttctatactgttgacccaatgcgtctcccttgtcatctaaacccacaccgggtgtcataatcaaccaatcgtaaccttcatctcttccacccatgtctctttgagcaataaagccgataacaaaatctttgtcgctcttcgcaatgtcaacagtacccttagtatattctccagtagatagggagcccttgcatgacaattctgctaacatcaaaaggcctctaggttcctttgttacttcttctgccgcctgcttcaaaccgctaacaatacctgggcccaccacaccgtgtgcattcgtaatgtctgcccattctgctattctgtatacacccgcagagtactgcaatttgactgtattaccaatgtcagcaaattttctgtcttcgaagagtaaaaaattgtacttggcggataatgcctttagcggcttaactgtgccctccatggaaaaatcagtcaaaatatccacatgtgtttttagtaaacaaattttgggacctaatgcttcaactaactccagtaattccttggtggtacgaacatccaatgaagcacacaagtttgtttgcttttcgtgcatgatattaaatagcttggcagcaacaggactaggatgagtagcagcacgttccttatatgtagctttcgacatgatttatcttcgtttcctgcaggtttttgttctgtgcagttgggttaagaatactgggcaatttcatgtttcttcaacactacatatgcgtatatataccaatctaagtctgtgctccttccttcgttcttccttctgttcggagattaccgaatcaaaaaaatttcaaagaaaccgaaatcaaaaaaaagaataaaaaaaaaatgatgaattgaattgaaaagctagcttatcgatgataagctgtcaaagatgagaattaattccacggactatagactatactagatactccgtctactgtacgatacacttccgctcaggtccttgtcctttaacgaggccttaccactcttttgttactctattgatccagctcagcaaaggcagtgtgatctaagattctatcttcgcgatgtagtaaaactagctagaccgagaaagagactagaaatgcaaaaggcacttctacaatggctgccatcattattatccgatgtgacgctgcagcttctcaatgatattcgaatacgctttgaggagatacagcctaatatccgacaaactgttttacagatttacgatcgtacttgttacccatcattgaattttgaacatccgaacctgggagttttccctgaaacagatagtatatttgaacctgtataataatatatagtctagcgctttacggaagacaatgtatgtatttcggttcctggagaaactattgcatctattgcataggtaatcttgcacgtcgcatccccggttcattttctgcgtttccatcttgcacttcaatagcatatctttgttaacgaagcatctgtgcttcattttgtagaacaaaaatgcaacgcgagagcgctaatttttcaaacaaagaatctgagctgcatttttacagaacagaaatgcaacgcgaaagcgctattttaccaacgaagaatctgtgcttcatttttgtaaaacaaaaatgcaacgcgacgagagcgctaatttttcaaacaaagaatctgagctgcatttttacagaacagaaatgcaacgcgagagcgctattttaccaacaaagaatctatacttcttttttgttctacaaaaatgcatcccgagagcgctatttttctaacaaagcatcttagattactttttttctcctttgtgcgctctataatgcagtctcttgataactttttgcactgtaggtccgttaaggttagaagaaggctactttggtgtctattttctcttccataaaaaaagcctgactccacttcccgcgtttactgattactagcgaagctgcgggtgcattttttcaagataaaggcatccccgattatattctataccgatgtggattgcgcatactttgtgaacagaaagtgatagcgttgatgattcttcattggtcagaaaattatgaacggtttcttctattttgtctctatatactacgtataggaaatgtttacattttcgtattgttttcgattcactctatgaatagttcttactacaatttttttgtctaaagagtaatactagagataaacataaaaaatgtagaggtcgagtttagatgcaagttcaaggagcgaaaggtggatgggtaggttatatagggatatagcacagagatatatagcaaagagatacttttgagcaatgtttgtggaagcggtattcgcaatgggaagctccaccccggttgataatcagaaaagccccaaaaacaggaagattattatcaaaaaggatcttcacctagatccttttaaattaaaaatgaagttttaaatcaatctaaagtatatatgagtaaacttggtctgacagttaccaatgcttaatcagtgaggcacctatctcagcgatctgtctatttcgttcatccatagttgcctgactccccgtcgtgtagataactacgatacgggagcgcttaccatctggccccagtgctgcaatgataccgcgagacccacgctcaccggctccagatttatcagcaataaaccagccagccggaagggccgagcgcagaagtggtcctgcaactttatccgcctccatccagtctattaattgttgccgggaagctagagtaagtagttcgccagttaatagtttgcgcaacgttgttggcattgctacaggcatcgtggtgtcactctcgtcgtttggtatggcttcattcagctccggttcccaacgatcaaggcgagttacatgatcccccatgttgtgcaaaaaagcggttagctccttcggtcctccgatcgttgtcagaagtaagttggccgcagtgttatcactcatggttatggcagcactgcataattctcttactgtcatgccatccgtaagatgcttttctgtgactggtgagtactcaaccaagtcattctgagaatagtgtatgcggcgaccgagttgctcttgcccggcgtcaatacgggataatagtgtatcacatagcagaactttaaaagtgctcatcattggaaaacgttcttcggggcgaaaactctcaaggatcttaccgctgttgagatccagttcgatgtaacccactcgtgcacccaactgatcttcagcatcttttactttcaccagcgtttctgggtgagcaaaaacaggaaggcaaaatgccgcaaaaaagggaataagggcgacacggaaatgttgaatactcatactcttcctttttcaatattattgaagcatttatcagggttattgtctcatgagcggatacatatttgaatgtatttagaaaaataaacaaataggggttccgcgcacatttccccgaaaagtgccacctgctaagaaaccattattatcatgacattaacctataaaaataggcgtatcacgaggccctttcgtctcgcgcgtttcggtgatgacggtgaaaacctctgacacatgcagctcccggagacggtcacagcttgtctgtaagcggatgccgggagcagacaagcccgtcagggcgcgtcagcgggtgttggcgggtgtcggggctggcttaactatgcggcatcagagcagattgtactgagagtgcaccatagatcctgaggatcggggtgataaatcagtctgcgccacatcgggggaaacaaaatggcgcgagatctaaaaaaaaaggctccaaaaggagcctttcgcgctaccaggtaacgcgccactccgacgggattaacgagtgccgtaaacgacgatggttttaccgtgtgcggagatcaggttctgatcctcgagcatcttaagaattcgtcccacggtttgtctagagcagccgacaatctggccaatttcctgacgggtaattttgatttgcatgccgtccgggtgagtcatagcgtctggttgttttgccagattcagcagagtctgtgcaatgcggccgctgaccacatacgatttaggtgacactatagaacgcggccgccagctgaagcttcgtacgctgcaggtcgacggatccccgggttaattaaggcgcgccagatctgtttagcttgccttgtccccgccgggtcacccggccagcgacatggaggcccagaataccctccttgacagtcttgacgtgcgcagctcaggggcatgatgtgactgtcgcccgtacatttagcccatacatccccatgtataatcatttgcatccatacattttgatggccgcacggcgcgaagcaaaaattacggctcctcgctgcagacctgcgagcagggaaacgctcccctcacagacgcgttgaattgtccccacgccgcgcccctgtagagaaatataaaaggttaggatttgccactgaggttcttctttcatatacttccttttaaaatcttgctaggatacagttctcacatcacatccgaacataaacaaccgtcgaggaacgccaggttgcccactttctcactagtgacctgcagccggccaatcacatcacatccgaacataaacaaccatgggtaaaaagcctgaactcaccgcgacgtctgtcgagaagtttctgatcgaaaagttcgacagcgtctccgacctgatgcagctctcggagggcgaagaatctcgtgctttcagcttcgatgtaggagggcgtggatatgtcctgcgggtaaatagctgcgccgatggtttctacaaagatcgttatgtttatcggcactttgcatcggccgcgctcccgattccggaagtgcttgacattggggaattcagcgagagcctgacctattgcatctcccgccgtgcacagggtgtcacgttgcaagacctgcctgaaaccgaactgcccgctgttctgcagccggtcgcggaggccatggatgcgatcgctgcggccgatcttagccagacgagcgggttcggcccattcggaccgcaaggaatcggtcaatacactacatggcgtgatttcatatgcgcgattgctgatccccatgtgtatcactggcaaactgtgatggacgacaccgtcagtgcgtccgtcgcgcaggctctcgatgagctgatgctttgggccgaggactgccccgaagtccggcacctcgtgcacgcggatttcggctccaacaatgtcctgacggacaatggccgcataacagcggtcattgactggagcgaggcgatgttcggggattcccaatacgaggtcgccaacatcttcttctggaggccgtggttggcttgtatggagcagcagacgcgctacttcgagcggaggcatccggagcttgcaggatcgccgcggctccgggcgtatatgctccgcattggtcttgaccaactctatcagagcttggttgacggcaatttcgatgatgcagcttgggcgcagggtcgatgcgacgcaatcgtccgatccggagccgggactgtcgggcgtacacaaatcgcccgcagaagcgcggccgtctggaccgatggctgtgtagaagtactcgccgatagtggaaaccgacgccccagcactcgtccgagggcaaaggaataatcagtactgacaataaaaagattcttgtagggataacagggtaatcggacgcgccatctgtgcagacaaacgcatcaggatagagtcttttgtaacgaccccgtctccaccaacttggtatgcttgaaatctcaaggccattacacattcagttatgtgaacgaaaggtctttatttaacgtagcataaactaaataatacaggttccggttagcctgcaatgtgttaaatctaaaggagcatacccaaaatgaactgaagacaaggaaatttgcttgtccagatgtgattgagcatttgaacgttaataacataacatttttatacttaactatagaaagacttgtataaaaactggcaaacgagatattctgaatattggtgcatatttcaggtagaaaagcttacaaaacaatctaatcataatattgagatgaagagaaagataaaagaaaaaacgataagtcagatgagattatgattgtactttgaaatcgaggaacaaagtatatacggtagtagttccccgagttataacgggagatcatgtaaattgagaaaccagataaagatttggtatgcactctagcaagaaaataaaatgatgaatctatgatatagatcacttttgttccagcgtcgaggaacgccaggttgcccactttctcactagtgacctgcagccgggatcagatctttcaggaaagtttcggaggagatagtgttcggcagtttgtacatcatctgcgggatcaggtacggtttgatcaggttgtagaagatcaggtaagacatagaatcgatgtagatgatcggtttgtttttgttgatttttacgtaacagttcagttggaatttgttacgcagacccttaaccaggtattctacttcttcgaaagtgaaagactgggtgttcagtacgatcgatttgttggtagagtttttgttgtaatcccatttaccaccatcatccatgaaccagtatgccagagacatcggggtcaggtagttttcaaccaggttgttcgggatggtttttttgttgttaacgatgaacaggttagccagtttgttgaaagcttggtgtttgaaagtctgggcgccccaggtgattaccaggttacccaggtggttaacacgttcttttttgtgcggcggggacagtacccactgatcgtacagcagacatacgtggtccatgtatgctttgtttttccactcgaactgcatacagtaggttttaccttcatcacgagaacggatgtaagcatcacccaggatcagaccgatacctgcttcgaactgttcgatgttcagttcgatcagctgggatttgtattctttcagcagtttagagttcggacccaggttcattacctggttttttttgatgtttttcatatgcatggatccggggttttttctccttgacgttaaagtatagaggtatattaacaattttttgttgatacttttattacatttgaataagaagtaatacaaaccgaaaatgttgaaagtattagttaaagtggttatgcagtttttgcatttatatatctgttaatagatcaaaaatcatcgcttcgctgattaattaccccagaaataaggctaaaaaactaatcgcattatcatcctatggttgttaatttgattcgttcatttgaaggtttgtggggccaggttactgccaatttttcctcttcataaccataaaagctagtattgtagaatctttattgttcggagcagtgcggcgcgaggcacatctgcgtttcaggaacgcga"

    assert common_sub_strings.common_sub_strings(a, b, limit=29) == [
        (0, 9552, 220),
        (220, 0, 198),
        (420, 200, 67),
        (1369, 355, 30),
        (1369, 8033, 29),
    ]

    a = "actctacgacttgatctttacgta"

    # 9772
    b = "ccggtgaagacgaggacgcacggaggagagtcttccttcggagggctgtcacccgctcggcggcttctaatccgtacttcaatatagcaatgagcagttaagcgtattactgaaagttccaaagagaaggtttttttaggctaagataatggggctctttacatttccacaacatataagtaagattagatatggatatgtatatggatatgtatatggtggtaatgccatgtaatatgattattaaacttctttgcgtccatccaacgagatctggcgcgccttaattaacccaacctgcattaatgaatcggccaacgcgcggattaccctgttatccctacatattgttcgcgccatctgtgcagacaaacgcatcaggattcagtactgacaataaaaagattcttgttttcaagaacttgtcatttgtatagtttttttatattgtagttgttctattttaatcaaatgttagcgtgatttatattttttttcgcctcgacatcatctgcccagatgcgaagttaagtgcgcagaaagtaatatcatgcgtcaatcgtatgtgaatgctggtcgctatactgctgtcgattcgatactaacgccgccatccagtgtcgaaaacgagctcgaattcatcgatgatatcagatccactagtggcctatgcggccgcggatctgccggtctccctatagtgagtcgatccggatttacctgaatcaattggcgaaattttttgtacgaaatttcagccacttcacaggcggttttcgcacgtacccatgcgctacgttcctggccctcttcaaacaggcccagttcgccaataaaatcaccctgattcagataggagaggatcatttctttaccctcttcgtctttgatcagcactgccacagagcctttaacgatgtagtacagcgtttccgctttttcaccctggtgaataagcgtgctcttggatgggtacttatgaatgtggcaatgagacaagaaccattcgagagtaggatccgtttgaggtttaccaagtaccataagatccttaaatttttattatctagctagatgataatattatatcaagaattgtacctgaaagcaaataaattttttatctggcttaactatgcggcatcagagcagattgtactgagagtgcaccatatgcggtgtgaaataccgcacagatgcgtaaggagaaaataccgcatcaggcgctcttccgcttcctcgctcactgactcgctgcgctcggtcgttcggctgcggcgagcggtatcagctcactcaaaggcggtaatacggttatccacagaatcaggggataacgcaggaaagaacatgtgagcaaaaggccagcaaaaggccaggaaccgtaaaaaggccgcgttgctggcgtttttccataggctccgcccccctgacgagcatcacaaaaatcgacgctcaagtcagaggtggcgaaacccgacaggactataaagataccaggcgtttccccctggaagctccctcgtgcgctctcctgttccgaccctgccgcttaccggatacctgtccgcctttctcccttcgggaagcgtggcgctttctcatagctcacgctgtaggtatctcagttcggtgtaggtcgttcgctccaagctgggctgtgtgcacgaaccccccgttcagcccgaccgctgcgccttatccggtaactatcgtcttgagtccaacccggtaagacacgacttatcgccactggcagcagccactggtaacaggattagcagagcgaggtatgtaggcggtgctacagagttcttgaagtggtggcctaactacggctacactagaaggacagtatttggtatctgcgctctgctgaagccagttaccttcggaaaaagagttggtagctcttgatccggcaaacaaaccaccgctggtagcggtggtttttttgtttgcaagcagcagattacgcgcagaaaaaaaggatctcaagaagatcctttgatcttttctacggggtctgacgctcagtggaacgaaaactcacgttaagggattttggtcatgaggggtaataactgatataattaaattgaagctctaatttgtgagtttagtatacatgcatttacttataatacagttttttagttttgctggccgcatcttctcaaatatgcttcccagcctgcttttctgtaacgttcaccctctaccttagcatcccttccctttgcaaatagtcctcttccaacaataataatgtcagatcctgtagagaccacatcatccacggttctatactgttgacccaatgcgtctcccttgtcatctaaacccacaccgggtgtcataatcaaccaatcgtaaccttcatctcttccacccatgtctctttgagcaataaagccgataacaaaatctttgtcgctcttcgcaatgtcaacagtacccttagtatattctccagtagatagggagcccttgcatgacaattctgctaacatcaaaaggcctctaggttcctttgttacttcttctgccgcctgcttcaaaccgctaacaatacctgggcccaccacaccgtgtgcattcgtaatgtctgcccattctgctattctgtatacacccgcagagtactgcaatttgactgtattaccaatgtcagcaaattttctgtcttcgaagagtaaaaaattgtacttggcggataatgcctttagcggcttaactgtgccctccatggaaaaatcagtcaaaatatccacatgtgtttttagtaaacaaattttgggacctaatgcttcaactaactccagtaattccttggtggtacgaacatccaatgaagcacacaagtttgtttgcttttcgtgcatgatattaaatagcttggcagcaacaggactaggatgagtagcagcacgttccttatatgtagctttcgacatgatttatcttcgtttcctgcaggtttttgttctgtgcagttgggttaagaatactgggcaatttcatgtttcttcaacactacatatgcgtatatataccaatctaagtctgtgctccttccttcgttcttccttctgttcggagattaccgaatcaaaaaaatttcaaagaaaccgaaatcaaaaaaaagaataaaaaaaaaatgatgaattgaattgaaaagctagcttatcgatgataagctgtcaaagatgagaattaattccacggactatagactatactagatactccgtctactgtacgatacacttccgctcaggtccttgtcctttaacgaggccttaccactcttttgttactctattgatccagctcagcaaaggcagtgtgatctaagattctatcttcgcgatgtagtaaaactagctagaccgagaaagagactagaaatgcaaaaggcacttctacaatggctgccatcattattatccgatgtgacgctgcagcttctcaatgatattcgaatacgctttgaggagatacagcctaatatccgacaaactgttttacagatttacgatcgtacttgttacccatcattgaattttgaacatccgaacctgggagttttccctgaaacagatagtatatttgaacctgtataataatatatagtctagcgctttacggaagacaatgtatgtatttcggttcctggagaaactattgcatctattgcataggtaatcttgcacgtcgcatccccggttcattttctgcgtttccatcttgcacttcaatagcatatctttgttaacgaagcatctgtgcttcattttgtagaacaaaaatgcaacgcgagagcgctaatttttcaaacaaagaatctgagctgcatttttacagaacagaaatgcaacgcgaaagcgctattttaccaacgaagaatctgtgcttcatttttgtaaaacaaaaatgcaacgcgacgagagcgctaatttttcaaacaaagaatctgagctgcatttttacagaacagaaatgcaacgcgagagcgctattttaccaacaaagaatctatacttcttttttgttctacaaaaatgcatcccgagagcgctatttttctaacaaagcatcttagattactttttttctcctttgtgcgctctataatgcagtctcttgataactttttgcactgtaggtccgttaaggttagaagaaggctactttggtgtctattttctcttccataaaaaaagcctgactccacttcccgcgtttactgattactagcgaagctgcgggtgcattttttcaagataaaggcatccccgattatattctataccgatgtggattgcgcatactttgtgaacagaaagtgatagcgttgatgattcttcattggtcagaaaattatgaacggtttcttctattttgtctctatatactacgtataggaaatgtttacattttcgtattgttttcgattcactctatgaatagttcttactacaatttttttgtctaaagagtaatactagagataaacataaaaaatgtagaggtcgagtttagatgcaagttcaaggagcgaaaggtggatgggtaggttatatagggatatagcacagagatatatagcaaagagatacttttgagcaatgtttgtggaagcggtattcgcaatgggaagctccaccccggttgataatcagaaaagccccaaaaacaggaagattattatcaaaaaggatcttcacctagatccttttaaattaaaaatgaagttttaaatcaatctaaagtatatatgagtaaacttggtctgacagttaccaatgcttaatcagtgaggcacctatctcagcgatctgtctatttcgttcatccatagttgcctgactccccgtcgtgtagataactacgatacgggagcgcttaccatctggccccagtgctgcaatgataccgcgagacccacgctcaccggctccagatttatcagcaataaaccagccagccggaagggccgagcgcagaagtggtcctgcaactttatccgcctccatccagtctattaattgttgccgggaagctagagtaagtagttcgccagttaatagtttgcgcaacgttgttggcattgctacaggcatcgtggtgtcactctcgtcgtttggtatggcttcattcagctccggttcccaacgatcaaggcgagttacatgatcccccatgttgtgcaaaaaagcggttagctccttcggtcctccgatcgttgtcagaagtaagttggccgcagtgttatcactcatggttatggcagcactgcataattctcttactgtcatgccatccgtaagatgcttttctgtgactggtgagtactcaaccaagtcattctgagaatagtgtatgcggcgaccgagttgctcttgcccggcgtcaatacgggataatagtgtatcacatagcagaactttaaaagtgctcatcattggaaaacgttcttcggggcgaaaactctcaaggatcttaccgctgttgagatccagttcgatgtaacccactcgtgcacccaactgatcttcagcatcttttactttcaccagcgtttctgggtgagcaaaaacaggaaggcaaaatgccgcaaaaaagggaataagggcgacacggaaatgttgaatactcatactcttcctttttcaatattattgaagcatttatcagggttattgtctcatgagcggatacatatttgaatgtatttagaaaaataaacaaataggggttccgcgcacatttccccgaaaagtgccacctgctaagaaaccattattatcatgacattaacctataaaaataggcgtatcacgaggccctttcgtctcgcgcgtttcggtgatgacggtgaaaacctctgacacatgcagctcccggagacggtcacagcttgtctgtaagcggatgccgggagcagacaagcccgtcagggcgcgtcagcgggtgttggcgggtgtcggggctggcttaactatgcggcatcagagcagattgtactgagagtgcaccatagatcctgaggatcggggtgataaatcagtctgcgccacatcgggggaaacaaaatggcgcgagatctaaaaaaaaaggctccaaaaggagcctttcgcgctaccaggtaacgcgccactccgacgggattaacgagtgccgtaaacgacgatggttttaccgtgtgcggagatcaggttctgatcctcgagcatcttaagaattcgtcccacggtttgtctagagcagccgacaatctggccaatttcctgacgggtaattttgatttgcatgccgtccgggtgagtcatagcgtctggttgttttgccagattcagcagagtctgtgcaatgcggccgctgaccacatacgatttaggtgacactatagaacgcggccgccagctgaagcttcgtacgctgcaggtcgacggatccccgggttaattaaggcgcgccagatctgtttagcttgccttgtccccgccgggtcacccggccagcgacatggaggcccagaataccctccttgacagtcttgacgtgcgcagctcaggggcatgatgtgactgtcgcccgtacatttagcccatacatccccatgtataatcatttgcatccatacattttgatggccgcacggcgcgaagcaaaaattacggctcctcgctgcagacctgcgagcagggaaacgctcccctcacagacgcgttgaattgtccccacgccgcgcccctgtagagaaatataaaaggttaggatttgccactgaggttcttctttcatatacttccttttaaaatcttgctaggatacagttctcacatcacatccgaacataaacaaccgtcgaggaacgccaggttgcccactttctcactagtgacctgcagccggccaatcacatcacatccgaacataaacaaccatgggtaaaaagcctgaactcaccgcgacgtctgtcgagaagtttctgatcgaaaagttcgacagcgtctccgacctgatgcagctctcggagggcgaagaatctcgtgctttcagcttcgatgtaggagggcgtggatatgtcctgcgggtaaatagctgcgccgatggtttctacaaagatcgttatgtttatcggcactttgcatcggccgcgctcccgattccggaagtgcttgacattggggaattcagcgagagcctgacctattgcatctcccgccgtgcacagggtgtcacgttgcaagacctgcctgaaaccgaactgcccgctgttctgcagccggtcgcggaggccatggatgcgatcgctgcggccgatcttagccagacgagcgggttcggcccattcggaccgcaaggaatcggtcaatacactacatggcgtgatttcatatgcgcgattgctgatccccatgtgtatcactggcaaactgtgatggacgacaccgtcagtgcgtccgtcgcgcaggctctcgatgagctgatgctttgggccgaggactgccccgaagtccggcacctcgtgcacgcggatttcggctccaacaatgtcctgacggacaatggccgcataacagcggtcattgactggagcgaggcgatgttcggggattcccaatacgaggtcgccaacatcttcttctggaggccgtggttggcttgtatggagcagcagacgcgctacttcgagcggaggcatccggagcttgcaggatcgccgcggctccgggcgtatatgctccgcattggtcttgaccaactctatcagagcttggttgacggcaatttcgatgatgcagcttgggcgcagggtcgatgcgacgcaatcgtccgatccggagccgggactgtcgggcgtacacaaatcgcccgcagaagcgcggccgtctggaccgatggctgtgtagaagtactcgccgatagtggaaaccgacgccccagcactcgtccgagggcaaaggaataatcagtactgacaataaaaagattcttgtagggataacagggtaatcggacgcgccatctgtgcagacaaacgcatcaggatagagtcttttgtaacgaccccgtctccaccaacttggtatgcttgaaatctcaaggccattacacattcagttatgtgaacgaaaggtctttatttaacgtagcataaactaaataatacaggttccggttagcctgcaatgtgttaaatctaaaggagcatacccaaaatgaactgaagacaaggaaatttgcttgtccagatgtgattgagcatttgaacgttaataacataacatttttatacttaactatagaaagacttgtataaaaactggcaaacgagatattctgaatattggtgcatatttcaggtagaaaagcttacaaaacaatctaatcataatattgagatgaagagaaagataaaagaaaaaacgataagtcagatgagattatgattgtactttgaaatcgaggaacaaagtatatacggtagtagttccccgagttataacgggagatcatgtaaattgagaaaccagataaagatttggtatgcactctagcaagaaaataaaatgatgaatctatgatatagatcacttttgttccagcgtcgaggaacgccaggttgcccactttctcactagtgacctgcagccgggatcagatctttcaggaaagtttcggaggagatagtgttcggcagtttgtacatcatctgcgggatcaggtacggtttgatcaggttgtagaagatcaggtaagacatagaatcgatgtagatgatcggtttgtttttgttgatttttacgtaacagttcagttggaatttgttacgcagacccttaaccaggtattctacttcttcgaaagtgaaagactgggtgttcagtacgatcgatttgttggtagagtttttgttgtaatcccatttaccaccatcatccatgaaccagtatgccagagacatcggggtcaggtagttttcaaccaggttgttcgggatggtttttttgttgttaacgatgaacaggttagccagtttgttgaaagcttggtgtttgaaagtctgggcgccccaggtgattaccaggttacccaggtggttaacacgttcttttttgtgcggcggggacagtacccactgatcgtacagcagacatacgtggtccatgtatgctttgtttttccactcgaactgcatacagtaggttttaccttcatcacgagaacggatgtaagcatcacccaggatcagaccgatacctgcttcgaactgttcgatgttcagttcgatcagctgggatttgtattctttcagcagtttagagttcggacccaggttcattacctggttttttttgatgtttttcatatgcatggatccggggttttttctccttgacgttaaagtatagaggtatattaacaattttttgttgatacttttattacatttgaataagaagtaatacaaaccgaaaatgttgaaagtattagttaaagtggttatgcagtttttgcatttatatatctgttaatagatcaaaaatcatcgcttcgctgattaattaccccagaaataaggctaaaaaactaatcgcattatcatcctatggttgttaatttgattcgttcatttgaaggtttgtggggccaggttactgccaatttttcctcttcataaccataaaagctagtattgtagaatctttattgttcggagcagtgcggcgcgaggcacatctgcgtttcaggaacgcga"

    assert common_sub_strings.common_sub_strings(a, b, limit=29) == []

    a = "GGGCGCGGGCGGNNNNTATATCATATAAA"
    b = "TATATCATATAAAnnGGGCGCGGGCGG"
    lim = 12

    assert common_sub_strings.terminal_overlap(a, b, lim) == [(16, 0, 13), (0, 15, 12)]

    a, b = b, a

    assert common_sub_strings.terminal_overlap(a, b, lim) == [(0, 16, 13), (15, 0, 12)]

    # x,y,l = terminal_overlap(a, b,lim).pop()

    #    x='atctgaacgctttgaatgttgtctctattccacgaggcattcaaaaactggttaccgaacctcaagactaaaagattcttgaccaactctttacccaagtaatggtcaattctgtacaactcttcttctttaaagaggggccccaggtttttttgcagctccctggcagaggccaggtcgtggccgaaaggtttctctacgattacacgggtgatgccattctctgcgtacacacgactcttgatctgcttggccaccgtcaaaaaaacgcttggcggcaaggccagatagaagagacggtgtgggacatcgacgttggcacttttctcgaatttctcgatctgcgttcttaattcgtcgaagccttcatctgtgtcgtaatttcccgaaatgtagctgaccatcttgaagaactgttcgaccttagagtcatcggcttcaccgtgaggttttttcaagtggggtaggacacgggacttcaggtcctcctccatggacaatttggaccgggcataaccgaagatcttggtagatggatcaaggtaaccttctctgaaaagcccaaataaggcgggaaaagtcttcttctttgccagatcacctgacgcaccaaagacagatatgacggtatttttttcgaatttgacggggccttcactcatctgcagcccgggggatccactagttctagaa'
    #    y='atcgataagcttgatatcgaattcctgcagctaattatccttcgtatcttctggcttagtcacgggccaagcgtaagggtgcttttcgggcataacatacttgtgtttttggtaatggtcaattctgtacaactcttcatatattccttcaatccctttggacctcttgatccgtaggggtaaatttccggtgttggaccgtccggacgctctatgtgcttcagtaatggggtgaatatgccccaactgatatccaattcgtcatctctgacaaagttggaatggtcacccagtagggcgtctcttatcaacacctcgtaagcctctggaatccaaaagtcttggtacctgcttgcgtaagttagattcagatctgtgacttgggtagcatttgacagaccaggggtcttagcattaaactttaggtacacagcggcatcgggctgcactctgatgaccagttcgttatttggaatgtctttgaagacacccgatgcgaccgctttgtactgcagtctgatctccaccttggactcattcaaagccttaccggcacgcatcatgatggggacgccctcccaacgctcgttttcgatgttgaaagtcattgctgcaaaagtgacacatttagagtccttgtctacagtgtcatcatccacgtaggcgggcttagacccgtcctcagatttaccgtactggcccaagaggacgtcgtccgtgtcgatgatctgaacgctttgaatgttgtctctattccacgaggcattcaaaaaggggccacggcctttagaaccttaaccttttcgtcacgaatagattccgggtcaaaagacaccggtctttccatagtcaagagagtcatgatttgtaacagatggttctgcatcacgtctctgattatgcctatagagtcgaaatagccgccacggccttcggtgccgaacctctctttaaacgaaatctgaacgctttgaatgttgtctctattccacgaggcattcaaaaa'
    #    print common_sub_strings(x,y)
    # a,b = "taaatc","aaataa"
    # print common_sub_strings(a+a, b, limit = min(25, 25*(len(a)/25)+1))

    # 1404

    """
    (1, 1, 2)
    (2, 0, 2)
    (7, 1, 2)
    (8, 0, 2)
    (2, 4, 2)
    (8, 4, 2)

    (1, 0, 2)
    (1, 1, 2) 1
    (1, 4, 2)
    (2, 0, 2) 2
    (2, 1, 2)
    (2, 4, 2) 3
    (7, 0, 2)
    (7, 1, 2) 4
    (7, 4, 2)
    (8, 0, 2) 5
    (8, 1, 2)
    (8, 4, 2) 6
    """


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
