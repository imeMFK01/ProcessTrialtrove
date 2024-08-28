character_mapping = {
  129: 'i', # _
  149: ' dot ', # u0095
  155: ' bracket ', # u009B        
  157: ' box ', # u009D
  159: 'Y', # u009D        
  160: ' ', #  
  161: '!', # ¡
  162: 'cents', # \u00A2
  163: 'Pound sterling ', # £
  164: 'Currency', # \u00A4
  165: 'Yen ', # ¥
  166: '|', # \u00A6
  167: 'Section', # §
  168: '\"', # ¨
  169: '', # ©
  170: 'a', # ª
  171: '<<', # «
  172: '-', # ¬
  173: '-', # ­­­-
  174: '', # ®
  175: 'bar', # \u00AF
  176: ' degrees', # °
  177: '+-', # ±
  178: ' squared', # ²
  179: ' cubed', # ³
  180: '\'', # ´
  181: 'mu', # µ
  182: 'paragraph break ', # \u00B6
  183: '.', # ·
  184: ',', # ¸
  185: '1', # ¹
  186: ' degrees', # º
  187: '', # » 
  188: '0.25', # ¼
  189: '0.5', # ½
  190: '0.75', # ¾
  191: '-', # ¿
  192: 'A', # \u00C0
  193: 'A', # Á
  194: 'A', # Â
  195: 'A', # Ã
  196: 'A', # Ä
  197: 'A', # \u00C5
  198: 'AE', # \u00C6
  199: 'C', # Ç
  200: 'E', # È
  201: 'E', # É
  202: 'E', # \u00CA
  203: 'E', # \u00CB
  204: 'I', # \u00CC
  205: 'I', # Í
  206: 'I', # Î
  207: 'I', # Ï
  208: 'Eth', # \u00D0
  209: 'N', # Ñ
  210: 'O', # \u00D2
  211: 'O', # Ó
  212: 'O', # \u00D4
  213: 'O', # \u00D5
  214: 'O', # Ö
  215: 'x', # ×
  216: 'None', # Ø
  217: 'U', # \u00D9
  218: 'U', # Ú
  219: 'U', # \u00DB
  220: 'U', # Ü
  221: 'Y', # Ý
  222: 'thorn', # \u00C6
  223: 'S', # ß
  224: 'a', # à
  225: 'a', # á
  226: 'a', # â
  227: 'a', # ã
  228: 'a', # ä
  229: 'a', # å
  230: 'ae', # æ
  231: 'c', # ç
  232: 'e', # è
  233: 'e', # é
  234: 'e', # ê
  235: 'e', # ë
  236: 'i', # ì
  237: 'i', # í
  238: 'i', # î
  239: 'i', # ï
  240: 'o', # ð
  241: 'n', # ñ
  242: 'o', # ò
  243: 'o', # ó
  244: 'o', # ô
  245: 'o', # \u00F5
  246: 'o', # ö
  247: '/', # ÷
  248: 'o', # ø
  249: 'u', # ù
  250: 'u', # ú
  251: 'u', # \u00FB
  252: 'u', # ü
  253: 'y', # ý
  254: 'thorn', # þ
  255: 'y', # u00FF
  256: 'A', # u0100
  257: 'a', # u0101  
  258: 'A', # u0102
  259: 'a', # u0103  
  260: 'A', # u0104
  261: 'a', # u0105
  262: 'C', # u0106
  263: 'c', # u0107
  264: 'C', # u0108
  265: 'c', # u0109 
  266: 'C', # u010A
  267: 'c', # u010B 
  268: 'C', # u010C
  269: 'c', # u010D 
  270: 'D', # u010E
  271: 'd', # u010F 
  272: 'D', # u0110  
  273: 'd', # u0111 
  274: 'E', # u0112  
  275: 'e', # u0113 
  276: 'E', # u0114  
  277: 'e', # u0115 
  278: 'E', # u0116  
  279: 'e', # u0117 
  280: 'E', # u0118  
  281: 'e', # u0119 
  282: 'E', # u011A  
  283: 'e', # u011B 
  284: 'G', # u011C  
  285: 'g', # u011D 
  286: 'G', # u011E  
  287: 'g', # u011F
  288: 'G', # u0120  
  289: 'g', # u0121
  290: 'G', # u0122
  291: 'g', # u0123
  292: 'H', # u0124
  293: 'h', # u0125
  294: 'H', # u0126  
  295: 'h', # u0127
  296: '~I', # u0128
  297: '~i', # u0129  
  298: 'I', # u012A
  299: 'i', # u012B
  300: 'I', # u012C
  301: 'i', # u012D
  302: 'I', # u012E
  303: 'i', # u012F
  304: 'I', # u0130
  305: 'i', # u0131  
  306: 'IJ', # u0132
  307: 'ij', # u0133  
  308: 'J', # u0134
  309: 'j', # u0135
  310: 'K', # u0136
  311: 'k', # u0137
  312: 'k', # u0138  
  313: 'L', # u0139
  314: 'l', # u013A
  315: 'L', # u013B
  316: 'l', # u013C
  317: 'L', # u013D  
  318: 'l', # u013E
  319: 'L', # u013F  
  320: 'l', # u0140
  321: 'L', # u0141  
  322: 'l', # u142
  323: 'N', # u143
  324: 'n', # u144
  325: 'N', # u145
  326: 'n', # u146
  327: 'N', # u147
  328: 'n', # u148
  329: '\'n', # u149
  332: 'O', # u14C
  333: 'O', # u14D
  334: 'O', # u14E  
  335: 'o', # u14F
  336: 'O', # u150
  337: 'o', # u0151
  338: 'oe', # u0152  
  339: 'oe', # u0153
  340: 'R', # u0154
  341: 'r', # u0155
  342: 'R', # u0156
  343: 'r', # u0157  
  344: 'R', # u0158  
  345: 'r', # u0159
  346: 'S', # u015  
  347: 's', # u015B
  348: 'S', # u015C  
  349: 's', # u015D  
  350: 'S', # u015E  
  351: 's', # u015F
  352: 'S', # Š
  353: 's', # u0161
  354: 'T', # u0162
  355: 't', # u0163
  356: 'T', # u0164
  357: 't', # u0165
  358: 'T', # u0166
  359: 't', # u0167
  360: 'U', # u0168
  361: 'u', # u0169
  362: 'U', # u016A
  363: 'u', # u016B
  364: 'U', # u016C
  365: 'u', # u016D
  366: 'U', # u016E
  367: 'u', # u016F
  368: 'U', # u0170
  369: 'u', # u0171  
  370: 'U', # u0172
  371: 'u', # u0173
  372: 'W', # u0174
  373: 'w', # u0175
  374: 'W', # u0176
  375: 'w', # u0177
  376: 'W', # u0178
  377: 'w', # u0179  
  378: 'Z', # u017A  
  379: 'Z', # u017B
  380: 'z', # u017C  
  381: 'Z', # u017D
  382: 'z', # u017E
  383: 'S', # u017F
  400: 'E', # u0190    
  402: 'f', # ƒ
  403: 'G', # u0193
  404: 'Gamma', # u0194  
  417: 'o', # u1A1
  436: 'y', # u1B4  
  450: ' Latin letter ', # u1C2      
  466: 'o', # u01D2
  537: 's', # u0219
  538: 'T', # u021A
  539: 't', # u021B
  593: 'alpha', #u0251  
  609: 'g',  # u0261
  611: 'gamma', #u0263
  612: 'gamma', #u0264      
  628: 'N',  # u0274
  671: 'L',  # u029F  
  688: 'h', # u2B0
  691: 'r',  # u02B3  
  697: '\'', # u2B9
  706: '&lt;', # u02C2
  707: '&gt;', # u02C3
  708: '^', # u02C4  
  710: '', # ˆ
  721: ' triangle ', # u02D1
  727: '-', #u02D7
  728: '', #u02D8
  729: '', #u02D9
  730: '', #u02DA
  731: '', #u02DB  
  732: '~', # ˜
  768: '\'', # u300
  769: '\`', # u301
  770: '', #u0302
  771: '~', #u0303
  772: '', #u0304
  773: '', #u0305
  774: '', #u0306 
  775: '', #u0307 
  776: '\"', # u308
  778: ' circle ', # u30A    
  822: '-', # u336  
  834: '~', # u342  
  835: '\'', # u343  
  894: '?', # \u037E 
  913: 'Alpha', #u0391
  914: 'Beta', #u0392
  915: 'Gamma', #u0393
  916: 'Delta', #u0394
  917: 'Epsilon', #u0395
  918: 'Zeta', #u0396
  919: 'Eta', #u0397
  920: 'Theta', #u0398
  921: 'Iota', #u0399
  922: 'Kappa', #u039A
  923: 'Lambda', #u039B
  924: 'Mu', #u039C
  931: 'Sigma', #u03A3    
  932: 'Tau', #u03A4
  934: 'Phi', #u03A6  
  935: 'Chi', #u03A7  
  943: 'iota', #u03AF  
  945: 'alpha', # u03B1  
  946: 'beta', # u03B2
  947: 'gamma', # u03B3
  948: 'delta', # u03B4
  949: 'epsilon', # u03B5
  950: 'zeta', # u03B6
  951: 'eta', # u03B7
  952: 'theta', # u03B8
  953: 'iota', # u03B9
  954: 'kappa', # u03BA
  955: 'lambda', # u03BB  
  956: 'mu', # u03BC
  957: 'nu', # u03BD
  958: 'xi', # u03BE
  959: 'omicron', # u03BF
  960: 'pi', # u03C0  
  961: 'rho', # u03C1
  962: 'sigma', # u03C2
  963: 'sigma', # u03C3
  964: 'tau', # u03C4
  965: 'upsilon', # u03C5
  966: 'phi', # u03C6
  967: 'chi', # u03C7
  968: 'psi', # u03C8
  969: 'omega', # u03C9
  981: 'phi', # u03D5
  1030: 'I', # u0406  
  1040: 'A', # u0410
  1042: 'A', # u0412    
  1045: 'E', # u0415    
  1048: 'I', # u0418
  1050: 'K', # u041A
  1051: 'JI', # u041B            
  1052: 'M', # u041C
  1053: 'H', # u041D
  1054: 'O', # u041E
  1055: 'PE', # u041F
  1056: 'P', # u0420      
  1057: 'C', # u0421
  1058: 'T', # u0422
  1064: ' Sha ', # u0428  
  1072: 'a', # u0430
  1075: 'Cyrillic letter', #u0433
  1077: 'Cyrillic letter', #u0435
  1083: 'Cyrillic letter', #u043B  
  1084: 'm', # u043C  
  1085: 'h', # u043D
  1086: 'o', # u043E
  1087: 'pe', # u043F
  1088: 'p', # u0440
  1089: 'c', # u0441
  1091: 'y', # u0443      
  1093: 'x', # u0445  
  1110: 'i', # u0456
  1111: 'yi', # u0457
  1179: 'Cyrillic letter', # u049B    
  1195: 'c', # u04AB
  1255: '0', # u04E7  
  1589: 'Arabic character', # u0635  
  1608: 'Arabic character', # u0648
  1776: 'Arabic zero', # u06f0
  1777: 'Arabic one', # u06f1
  1778: 'Arabic two', # u06f2  
  3640: 'Thai character', # u0E38
  7437: 'M', # u1D0D
  7475: 'G', # u1D33
  7481: 'M', # u1D39
  7488: 'T', # u1D40            
  7491: 'a', # u1D43
  7492: 'reverse a', # u1D44  
  7493: 'a', # u1D45
  7494: 'reverse ae', # u1D46
  7495: 'b', # u1D47
  7496: 'd', # u1D48  
  7497: 'e', # u1D49
  7498: 'schwa', # u1D4A  
  7499: 'member ', # u1D4B
  7500: 'turned e', # u1D4C
  7501: 'g', # u1D4D
  7504: 'g', # u1D50    
  7511: 't', # u1D57 
  7580: 'M', # u1D9C        
  7697: 'd', # u1E11  
  7716: 'H', # u1E24
  7830: 'h', # u1E96
  7847: 'a', # u1EA7
  7848: 'A', # u1EA8
  7849: 'a', # u1EA9
  7850: 'A', # u1EAA
  7851: 'a', # u1EAB
  7871: 'e', # u1EBF
  7897: 'o', # u1ED9
  7907: 'o', # u1EE3
  7929: 'y', # u1EF9    
  8194: '  ', # u2002  
  8195: '  ', # u2003
  8197: '  ', # u2005
  8198: '  ', # u2006      
  8199: '  ', # u2007
  8200: '  ', # u2008  
  8201: ' ', # u2009
  8202: ' ', # u200a
  8203: ' ', # u200b
  8204: ' ', # u200c
  8205: ' ', # u200d
  8206: ' ', # u200e
  8207: ' ', # u200f
  8208: '-', # u2010
  8209: '-', # u2011
  8210: '-', # u2012  
  8211: '-', # –
  8212: '-', # —
  8213: ' horizontal bar ', # u2015  
  8214: '\'', # u2016
  8215: ' double underline ', # u2017  
  8216: '\'', # ‘
  8217: '\'', # ’
  8218: '\`', # u201A
  8219: '\`', # u201B
  8220: '\"', # “
  8221: '\"', # ”
  8222: ',', # „
  8224: 'dagger', # †
  8225: 'doubledagger', # ‡
  8226: '-', # •
  8227: ' traingular bullet ', # u2023
  8230: '...', # …
  8231: ' circular bullet ', #u2027    
  8232: ' new line', #u2028
  8239: ' ', # u202f  
  8240: '0/00', # \u2030
  8242: ' prime  ', # u2032  
  8249: '<', # \u2039
  8250: '>', # \u203A
  8251: 'reference mark', #u203B
  8259: '-', # u2043  
  8260: '/', #u2044
  8275: '~', #u2053
  8277: ' flower ', # u2055    
  8304: '^0', # u2070
  8305: '^1', # u2071
  8306: '^2', # u2072
  8307: '^3', # u2073
  8308: '^4', # u2074
  8309: '^5', # u2075
  8310: '^6', # u2076
  8311: '^7', # u2077
  8312: '^8', # u2078
  8313: '^9', # u2079
  8314: '^+', # \u207A  
  8315: '^-', # \u207B  
  8317: '(', # \u207D
  8318: ')', # \u207E      
  8319: '^n', # \u207F  
  8320: '_0', # u2080
  8321: '_1', # u2081
  8322: '_2', # u2082
  8323: '_3', # u2083  
  8324: '_4', # u2084
  8325: '_5', # u2085  
  8326: '_6', # u2086
  8327: '_7', # u2087
  8328: '_8', # u2088
  8336: '_a', # u2090
  8337: '_e', # u2091
  8338: '_o', # u2092 
  8339: '_x', # u2093 
  8343: '_l', # u2097
  8344: '_m', # u2098
  8345: '_n', # u2099
  8346: '_p', # u209A  
  8347: '_s', # u209B
  8348: '_t', # u209C 
  8364: 'Euro', # €
  8451: 'degrees Celsius', # u2103
  8470: 'Numero sign', #u2116
  8480: ' Service Mark ', #u2120  
  8482: '', # ™
  8532: '2/3', # u2154    
  8544: 'I', # u2160
  8545: 'II', # u2161  
  8546: 'III', # u2162  
  8547: 'IV', # u2163
  8548: 'V', # u2164
  8549: 'VI', # u2165        
  8560: 'i', # \u2170
  8561: 'ii', # \u2171
  8562: 'iii', # \u2172
  8563: 'iv', # \u2173
  8564: 'v', # \u2174
  8569: 'x', # \u2179  
  8592: '<-', #u2190
  8593: '^', #u2191
  8594: '->', #u2192
  8595: '_', #u2193
  8658: ' right arrow ', #u21D2    
  8710: ' increment ', #u2206
  8721: ' Sum ', #u2211
  8722: '-', #u2212
  8725: '/', #u2215
  8727: '*', #u2217  
  8729: 'dot', #u2219
  8730: 'square root', #u221A
  8731: 'cube root', #u221B
  8732: 'fourth root', #u221C  
  8733: 'related to', #u221D
  8734: 'infinity', #u221E
  8741: ' logical or ', #u2225    
  8743: ' logical and ', #u2227
  8758: ':', #u2236
  8764: '~', #u223C
  8776: '~=', #u2248
  8800: 'not =', # u2260
  8804: '&lt;=', # u2264
  8805: '&gt;=', # u2265
  8806: '&lt;=', # u2266
  8807: '&gt;=', # u2267
  8815: ' not greater than ', #u226F
  8896: ' logical and ', #u22C0
  8901: 'dot', # u22C5
  9082: 'alpha', #u237A
  9134: '|', #u23AE    
  9135: '-', #u23AF
  9147: '-', #u23BB
  9148: '-', #u23BC  
  9312: '1', # u2460
  9313: '2', # u2461  
  9314: '3', # u2462
  9315: '4', # u2463
  9316: '5', # u2464
  9317: '6', # u2465
  9318: '7', # u2466
  9319: '8', # u2467
  9320: '9', # u2468
  9321: '10', # u2469
  9322: '11', # u246A
  9323: '12', # u246B
  9324: '13', # u246C
  9325: '14', # u246D
  9326: '15', # u246E
  9327: '16', # u246F
  9328: '17', # u2470
  9329: '18', # u2471
  9330: '19', # u2472
  9331: '20', # u2473
  9332: '1', # u2474
  9333: '2', # u2475
  9334: '3', # u2476
  9335: '4', # u2477
  9336: '5', # u2478
  9337: '6', # u2479
  9338: '7', # u2470
  9339: '8', # u2471
  9371: '20.', # u249B                                                    
  9415: ' trademark ', # u24C7
  9432: ' circled i ', # u24D8
  9472: '-', # u2500
  9474: '|', # u2502
  9587: 'times', #u2573
  9632: ' square ', #u25A0    
  9642: ' square ', #u25AA
  9644: ' rectangle ', #u25AC    
  9651: ' triangle ', #u25B3      
  9656: ' right pointer ', #u25B8  
  9658: ' right pointer ', #u25BA
  9660: ' downward pointer ', #u25BC
  9670: ' black diamond ', #u25C6  
  9674: 'lozenge ', # u25CA  
  9675: 'circle ', # u25CB  
  9678: ' bullseye ', #u25CE  
  9679: ' dot ', # u25CF
  9702: ' dot ', # u25E6
  9724: ' black square ', #u25FC
  9726: ' black square ', #u25FE    
  9733: ' star ', # u2605    
  9734: ' star ', # u2606
  9746: ' square with X ', #u2612        
  9758: ' right pointing index ', # u261E
  9830: ' diamond ', # u2666
  9899: ' black circle ', # u26AB        
  10003: ' check mark ', # u2713
  10004: ' check mark ', # u2714
  10006: ' multiplication symbol ', # u2716        
  10022: ' black four pointed star ', #u2726    
  10065: ' white square ', # u2751
  10070: ' diamond ', # u2756    
  10146: ' right arrowhead ', # u27A2
  10230: ' right arrow ', # u27F6
  10731: ' black lozenge ', # u29EB  
  10877: '&lt;=', # u2A7D  
  10878: '&gt;=', # u2A7E
  11389: 'V', # u2C7D
  11825: 'dot', # u2E31    
  12288: ' ', #u3000 
  12289: 'comma', #u3001
  12290: 'period', #u3002
  12298: 'left bracket', #u300A
  12299: 'right bracket', #u300B  
  12304: 'left bracket', #u3010
  12305: 'right bracket', #u3011
  12306: ' postal mark ', #u3012
  12308: ' left bracket ', #u3014  
  12309: ' right bracket ', #u3015
  12310: ' left bracket ', #u3016  
  12311: ' right bracket ', #u3017    
  12351: ' box with x ', #u303F
  12354: ' Hiragana letter ', #u3042              
  12426: ' Hiragana letter ', #u308A          
  12539: ' middle dot ', # u30FB  
  12540: 'sound mark', # u30FC
  12599: 'Hangul letter', # u3137 
  13197: 'mu g', # u338D
  13198: 'mg', # u338E 
  13205: 'mu l', # u3395  
  13217: 'm squared', #u33a1  
  19968: 'ideograph', #u4E00
  19978: 'Kanji character', # \u4E0A
  19994: ' Chinese character ', # \u4E1A    
  20008: ' Chinese character ', # \u4E28
  20013: ' Chinese character ', # \u4E2D
  20110: ' Chinese character ', # \u4E8E    
  20132: ' Chinese character ', # \u4EA4
  20140: ' Chinese character ', # \u4EAC
  20154: ' Chinese character ', # \u4EBA
  20161: ' Chinese character ', # \u4EC1
  20197: ' Chinese character ', # \u4EE5        
  20221: ' Chinese character ', # \u4EFD
  20248: ' Chinese character ', # \u4F18
  20304: ' Chinese character ', # \u4F50        
  20844: ' Chinese character ', # \u516C
  20849: ' Chinese character ', # \u5171
  20874: ' Chinese character ', # \u518A
  20934: ' Chinese character ', # \u51C6    
  20998: ' Chinese character ', # \u5206
  21271: ' Chinese character ', # \u5317
  21307: ' Chinese character ', # \u533B    
  21463: ' Chinese character ', # \u53D7
  21475: ' Chinese character ', # \u53E3
  21477: ' Chinese character ', # \u53E5    
  21496: ' Chinese character ', # \u53F8
  21513: ' Chinese character ', # \u5409
  21531: ' Chinese character ', # \u541B
  21578: ' Chinese character ', # \u544A
  21644: ' Chinese character ', # \u548C
  21697: ' Chinese character ', # \u54C1
  22235: ' Chinese character ', # u56DB
  22269: ' Chinese character ', # \u56FD
  22283: ' Chinese character ', # \u570B
  22374: ' Chinese character ', #
  22659: ' Chinese character ', # \u5883
  22763: ' Chinese character ', # u58EB
  22823: ' Chinese character ', # u5927
  22836: ' Chinese character ', # u5934
  22855: ' Chinese character ', # u5947    
  22987: ' Chinese character ', # \u59CB
  23398: ' Chinese character ', # u5B66    
  23416: ' Chinese character ', # u5B78
  23433: ' Chinese character ', # u5B89        
  23439: ' Chinese character ', #     
  23526: ' Chinese character ', # \u5BE6
  23545: ' Chinese character ', # \u5BF9        
  23567: ' Chinese character ', # \u5C0F
  23612: ' Chinese character ', #
  23660: ' Chinese character ', #
  24030: ' Chinese character ', # \u5DDE
  24120: ' Chinese character ', # \u5E38    
  24202: ' Chinese character ', # \u5E8A
  24247: ' Chinese character ', # u5EB7
  24320: ' Chinese character ', # 
  24378: ' Chinese character ', # \u5F3A
  24405: ' Chinese character ', # u5F55
  24471: ' Chinese character ', # u5F97     
  24489: ' Chinese character ', # uFA9
  24605: ' Chinese character ', # u601D
  24658: ' Chinese character ', # u6052
  25110: ' Chinese character ', # \u6216
  25209: ' Chinese character ', # 
  25216: ' Chinese character ', # \u6280
  25237: ' Chinese character ', # 
  25253: ' Chinese character ', #
  25991: ' Chinese character ', #u6587                
  26085: ' Chinese character ', #u65E5            
  26228: ' Chinese character ', #u6674 
  26354: ' Chinese character ', #u66F2  
  26360: ' Chinese character ', #u66F8
  26364: ' Chinese character ', #u66FC     
  26367: ' Chinese character ', #u66FF 
  26377: ' Chinese character ', # \u6709    
  26399: ' Chinese character ', #u671F
  26412: ' Chinese character ', #u672C        
  26469: ' Chinese character ', #
  26519: ' Chinese character ', #     
  26524: ' Chinese character ', #
  26631: ' Chinese character ', #u6807
  26862: ' Chinese character ', #u68EE    
  26989: ' Chinese character ', #u696D
  27425: ' Chinese character ', #u6B21 
  27665: ' Chinese character ', #u6C11
  27721: ' Chinese character ', #u6C49
  27827: ' Chinese character ', #u6CB3    
  27801: ' Chinese character ', #u6C99
  27827: ' Chinese character ', #u6C99    
  27861: ' Chinese character ', #u6CD5
  27888: ' Chinese character ', #u6CF0
  27931: ' Chinese character ', #u6D1B
  27941: ' Chinese character ', #u6D25         
  28023: ' Chinese character ', # \u6D77
  28450: ' Chinese character ', #
  28639: ' Chinese character ', # u6FDF   
  29031: ' Chinese character ', # u7167    
  29289: ' Chinese character ', # \u7269            
  29305: ' Chinese character ', #     
  29702: ' Chinese character ', #     
  29983: ' Chinese character ', # \u751F
  30244: ' Chinese character ', #u7624
  30465: ' Chinese character ', #u7701
  30591: ' Chinese character ', #u777F
  30693: ' Chinese character ', #
  30782: ' Chinese character ', #
  30844: ' Chinese character ', #
  31070: ' Chinese character ', #         
  31185: ' Chinese character ', # \u79D1
  31243: ' Chinese character ', # 
  31310: ' Chinese character ', # 
  31481: ' Chinese character ', # 
  31532: ' Chinese character ', #  u7B2C   
  31561: ' Chinese character ', # u7B49
  31649: ' Chinese character ', #
  31859: ' Chinese character ', #             
  32463: ' Chinese character ', #
  32467: ' Chinese character ', #
  32476: ' Chinese character ', #             
  32593: ' Chinese character ', #
  32752: ' Chinese character ', #u7FF0                 
  32763: ' Chinese character ', #             
  32929: ' Chinese character ', # \u80A1
  33131: ' Chinese character ', #
  33145: ' Chinese character ', #    
  33256: ' Chinese character ', #
  33258: ' Chinese character ', #
  33267: ' Chinese character ', #
  33487: ' Chinese character ', #u82CF
  33521: ' Chinese character ', # u82F1            
  33647: ' Chinese character ', #u836F
  33775: ' Chinese character ', #                 
  34277: ' Chinese character ', # \u85E5
  34311: ' Chinese character ', #
  34907: ' Chinese character ', #u885B                     
  35069: ' Chinese character ', #                 
  35387: ' Chinese character ', # \u8A3B
  35430: 'test, try, experiment', # \u8A66
  35657: ' Chinese character ', # \u8B49
  35793: ' Chinese character ', #
  35997: ' Chinese character ', #                 
  36164: ' Chinese character ', #
  36562: ' Chinese character ', #
  36880: ' Chinese character ', #
  36890: ' Chinese character ', #
  36947: ' Chinese character ', #
  37030: ' Chinese character ', #u90A6                     
  37200: ' Chinese character ', #                 
  37291: ' Chinese character ', # \u91AB
  38271: ' Chinese character ', #    
  38283: ' Chinese character ', # \u958B
  38468: ' Chinese character ', #             
  38480: ' Chinese character ', # \u9650
  38498: ' Chinese character ', #
  38678: ' Chinese character ', #
  39064: ' Chinese character ', # u9898        
  39443: ' Chinese character ', # 
  39511: ' Chinese character ', # \u9A57
  41226: ' Yi syllable ', # uA10A
  41266: ' Yi syllable ', # uA132
  42999: ' sideways I ', # \uA7F7  
  45716: ' Hangul letter ', # uB294
  46608: ' Hangul letter ', # uB610
  57441: ' private character ', # \uE061
  57442: ' private character ', # \uE062
  58908: ' private character ', # \uE61C                    
  58909: ' private character ', # \uE61D                
  58910: ' private character ', # \uE61E            
  58911: ' private character ', # \uE61F        
  61483: ' private character ', # \uF02B
  61485: ' private character ', # \uF02D      
  61500: ' private character ', # \uF03C
  61502: ' private character ', # \uF03E
  61537: ' private character ', # \uF061
  61538: ' private character ', # \uF062
  61543: ' private character ', # \uF067
  61548: ' private character ', # \uF06C    
  61549: ' private character ', # F06D
  61550: ' private character ', # \uF06E    
  61551: ' private character ', # \uF06F
  61552: ' private character ', # \uF070    
  61553: ' private character ', # \uF071
  61556: ' private character ', # \uF074
  61558: ' private character ', # F076
  61559: ' private character ', # \uF077
  61566: ' private character ', # \uF07D        
  61572: ' private character ', # \uF084    
  61591: ' private character ', # \uF097
  61592: ' private character ', # \uF098        
  61599: ' private character ', # \uF09F
  61600: ' private character ', # \uF0A0    
  61601: ' private character ', # uF0A1
  61603: ' private character ', # \uF0A3  
  61607: ' private character ', # \uF0A7
  61608: ' private character ', # \uF0A8    
  61610: ' private character ', # \uF0AA
  61616: ' private character ', # \uF0B0        
  61619: ' private character ', # \uF0B3
  61620: ' private character ', # \uF0B4  
  61623: ' private character ', # uF0B7
  61630: ' private character ', # uF0BE    
  61650: ' private character ', # \uF0D2                    
  61656: ' private character ', # \uF0D8                
  61664: ' private character ', # \uF0E0
  61666: ' private character ', # uF0E2
  61690: ' private character ', # \uF0FA      
  61692: ' private character ', # \uF0FC
  61694: ' private character ', # uF0FE
  64256: 'ff', # \uFB00
  64257: 'fi', # \uFB01
  64258: 'fI', # \uFB02
  64259: 'ffi', # \uFB03  
  65038: '', #uFE0E
  65039: '', #uFE0F  
  65072: ':', #uFE30  
  65073: '|', #uFE31
  65122: '-', #uFE62    
  65123: '-', #uFE63
  65124: '<', # \uFE64
  65125: '>', # \uFE65
  65279: ' ', # \uFEFF
  65281: '!', # \uFF01      
  65285: '%', #uFF05
  65286: '\&', # \uFF06  
  65288: '(', # \uFF08
  65289: ')', # \uFF09
  65290: '*', # uFF0A
  65291: '+', # uFF0B 
  65292: ',', # \uFF0C
  65293: '-', # uFF0D 
  65294: '-', # uFF0D 
  65295: ' period ', # uFF0E 
  65306: ' dot ', # \uFF1A
  65307: ';', # \uFF1B
  65308: '<', # \uFF1C  
  65309: '>', # \uFF1D  
  65310: '=', # \uFF1E  
  65311: '?', # \uFF1F
  65326: 'N', # \uFF2E    
  65339: '[', # \uFF3B  
  65341: ']', # \uFF3D
  65342: ' ^ ', # \uFF3E
  65345: 'a', # \uFF41
  65368: 'x', # uFF58    
  65371: '{', # uFF5B
  65372: '|', # uFF5C
  65373: '}', # uFF5D  
  65374: '~', # \uFF5E
  65381: ' square ', # \uFF65
  65532: ' object replacement ', # \uFFFC    
  65533: '?', # \uFFFD
  120514: 'alpha', # \u1D6C2  
  120572: 'alpha', # \u1D6FC
  120583: 'Mu', # \u1D707  
}
