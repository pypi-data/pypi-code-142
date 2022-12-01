class DeepDanbooruModel(Module):
  __parameters__ = []
  __buffers__ = []
  training : bool
  _is_full_backward_hook : Optional[bool]
  n_Conv_0 : __torch__.torch.nn.modules.conv.Conv2d
  n_MaxPool_0 : __torch__.torch.nn.modules.pooling.MaxPool2d
  n_Conv_1 : __torch__.torch.nn.modules.conv.___torch_mangle_0.Conv2d
  n_Conv_2 : __torch__.torch.nn.modules.conv.___torch_mangle_1.Conv2d
  n_Conv_3 : __torch__.torch.nn.modules.conv.___torch_mangle_2.Conv2d
  n_Conv_4 : __torch__.torch.nn.modules.conv.___torch_mangle_3.Conv2d
  n_Conv_5 : __torch__.torch.nn.modules.conv.___torch_mangle_4.Conv2d
  n_Conv_6 : __torch__.torch.nn.modules.conv.___torch_mangle_5.Conv2d
  n_Conv_7 : __torch__.torch.nn.modules.conv.___torch_mangle_6.Conv2d
  n_Conv_8 : __torch__.torch.nn.modules.conv.___torch_mangle_7.Conv2d
  n_Conv_9 : __torch__.torch.nn.modules.conv.___torch_mangle_8.Conv2d
  n_Conv_10 : __torch__.torch.nn.modules.conv.___torch_mangle_9.Conv2d
  n_Conv_11 : __torch__.torch.nn.modules.conv.___torch_mangle_10.Conv2d
  n_Conv_12 : __torch__.torch.nn.modules.conv.___torch_mangle_11.Conv2d
  n_Conv_13 : __torch__.torch.nn.modules.conv.___torch_mangle_12.Conv2d
  n_Conv_14 : __torch__.torch.nn.modules.conv.___torch_mangle_13.Conv2d
  n_Conv_15 : __torch__.torch.nn.modules.conv.___torch_mangle_14.Conv2d
  n_Conv_16 : __torch__.torch.nn.modules.conv.___torch_mangle_15.Conv2d
  n_Conv_17 : __torch__.torch.nn.modules.conv.___torch_mangle_16.Conv2d
  n_Conv_18 : __torch__.torch.nn.modules.conv.___torch_mangle_17.Conv2d
  n_Conv_19 : __torch__.torch.nn.modules.conv.___torch_mangle_18.Conv2d
  n_Conv_20 : __torch__.torch.nn.modules.conv.___torch_mangle_19.Conv2d
  n_Conv_21 : __torch__.torch.nn.modules.conv.___torch_mangle_20.Conv2d
  n_Conv_22 : __torch__.torch.nn.modules.conv.___torch_mangle_21.Conv2d
  n_Conv_23 : __torch__.torch.nn.modules.conv.___torch_mangle_22.Conv2d
  n_Conv_24 : __torch__.torch.nn.modules.conv.___torch_mangle_23.Conv2d
  n_Conv_25 : __torch__.torch.nn.modules.conv.___torch_mangle_24.Conv2d
  n_Conv_26 : __torch__.torch.nn.modules.conv.___torch_mangle_25.Conv2d
  n_Conv_27 : __torch__.torch.nn.modules.conv.___torch_mangle_26.Conv2d
  n_Conv_28 : __torch__.torch.nn.modules.conv.___torch_mangle_27.Conv2d
  n_Conv_29 : __torch__.torch.nn.modules.conv.___torch_mangle_28.Conv2d
  n_Conv_30 : __torch__.torch.nn.modules.conv.___torch_mangle_29.Conv2d
  n_Conv_31 : __torch__.torch.nn.modules.conv.___torch_mangle_30.Conv2d
  n_Conv_32 : __torch__.torch.nn.modules.conv.___torch_mangle_31.Conv2d
  n_Conv_33 : __torch__.torch.nn.modules.conv.___torch_mangle_32.Conv2d
  n_Conv_34 : __torch__.torch.nn.modules.conv.___torch_mangle_33.Conv2d
  n_Conv_35 : __torch__.torch.nn.modules.conv.___torch_mangle_34.Conv2d
  n_Conv_36 : __torch__.torch.nn.modules.conv.___torch_mangle_35.Conv2d
  n_Conv_37 : __torch__.torch.nn.modules.conv.___torch_mangle_36.Conv2d
  n_Conv_38 : __torch__.torch.nn.modules.conv.___torch_mangle_37.Conv2d
  n_Conv_39 : __torch__.torch.nn.modules.conv.___torch_mangle_38.Conv2d
  n_Conv_40 : __torch__.torch.nn.modules.conv.___torch_mangle_39.Conv2d
  n_Conv_41 : __torch__.torch.nn.modules.conv.___torch_mangle_40.Conv2d
  n_Conv_42 : __torch__.torch.nn.modules.conv.___torch_mangle_41.Conv2d
  n_Conv_43 : __torch__.torch.nn.modules.conv.___torch_mangle_42.Conv2d
  n_Conv_44 : __torch__.torch.nn.modules.conv.___torch_mangle_43.Conv2d
  n_Conv_45 : __torch__.torch.nn.modules.conv.___torch_mangle_44.Conv2d
  n_Conv_46 : __torch__.torch.nn.modules.conv.___torch_mangle_45.Conv2d
  n_Conv_47 : __torch__.torch.nn.modules.conv.___torch_mangle_46.Conv2d
  n_Conv_48 : __torch__.torch.nn.modules.conv.___torch_mangle_47.Conv2d
  n_Conv_49 : __torch__.torch.nn.modules.conv.___torch_mangle_48.Conv2d
  n_Conv_50 : __torch__.torch.nn.modules.conv.___torch_mangle_49.Conv2d
  n_Conv_51 : __torch__.torch.nn.modules.conv.___torch_mangle_50.Conv2d
  n_Conv_52 : __torch__.torch.nn.modules.conv.___torch_mangle_51.Conv2d
  n_Conv_53 : __torch__.torch.nn.modules.conv.___torch_mangle_52.Conv2d
  n_Conv_54 : __torch__.torch.nn.modules.conv.___torch_mangle_53.Conv2d
  n_Conv_55 : __torch__.torch.nn.modules.conv.___torch_mangle_54.Conv2d
  n_Conv_56 : __torch__.torch.nn.modules.conv.___torch_mangle_55.Conv2d
  n_Conv_57 : __torch__.torch.nn.modules.conv.___torch_mangle_56.Conv2d
  n_Conv_58 : __torch__.torch.nn.modules.conv.___torch_mangle_57.Conv2d
  n_Conv_59 : __torch__.torch.nn.modules.conv.___torch_mangle_58.Conv2d
  n_Conv_60 : __torch__.torch.nn.modules.conv.___torch_mangle_59.Conv2d
  n_Conv_61 : __torch__.torch.nn.modules.conv.___torch_mangle_60.Conv2d
  n_Conv_62 : __torch__.torch.nn.modules.conv.___torch_mangle_61.Conv2d
  n_Conv_63 : __torch__.torch.nn.modules.conv.___torch_mangle_62.Conv2d
  n_Conv_64 : __torch__.torch.nn.modules.conv.___torch_mangle_63.Conv2d
  n_Conv_65 : __torch__.torch.nn.modules.conv.___torch_mangle_64.Conv2d
  n_Conv_66 : __torch__.torch.nn.modules.conv.___torch_mangle_65.Conv2d
  n_Conv_67 : __torch__.torch.nn.modules.conv.___torch_mangle_66.Conv2d
  n_Conv_68 : __torch__.torch.nn.modules.conv.___torch_mangle_67.Conv2d
  n_Conv_69 : __torch__.torch.nn.modules.conv.___torch_mangle_68.Conv2d
  n_Conv_70 : __torch__.torch.nn.modules.conv.___torch_mangle_69.Conv2d
  n_Conv_71 : __torch__.torch.nn.modules.conv.___torch_mangle_70.Conv2d
  n_Conv_72 : __torch__.torch.nn.modules.conv.___torch_mangle_71.Conv2d
  n_Conv_73 : __torch__.torch.nn.modules.conv.___torch_mangle_72.Conv2d
  n_Conv_74 : __torch__.torch.nn.modules.conv.___torch_mangle_73.Conv2d
  n_Conv_75 : __torch__.torch.nn.modules.conv.___torch_mangle_74.Conv2d
  n_Conv_76 : __torch__.torch.nn.modules.conv.___torch_mangle_75.Conv2d
  n_Conv_77 : __torch__.torch.nn.modules.conv.___torch_mangle_76.Conv2d
  n_Conv_78 : __torch__.torch.nn.modules.conv.___torch_mangle_77.Conv2d
  n_Conv_79 : __torch__.torch.nn.modules.conv.___torch_mangle_78.Conv2d
  n_Conv_80 : __torch__.torch.nn.modules.conv.___torch_mangle_79.Conv2d
  n_Conv_81 : __torch__.torch.nn.modules.conv.___torch_mangle_80.Conv2d
  n_Conv_82 : __torch__.torch.nn.modules.conv.___torch_mangle_81.Conv2d
  n_Conv_83 : __torch__.torch.nn.modules.conv.___torch_mangle_82.Conv2d
  n_Conv_84 : __torch__.torch.nn.modules.conv.___torch_mangle_83.Conv2d
  n_Conv_85 : __torch__.torch.nn.modules.conv.___torch_mangle_84.Conv2d
  n_Conv_86 : __torch__.torch.nn.modules.conv.___torch_mangle_85.Conv2d
  n_Conv_87 : __torch__.torch.nn.modules.conv.___torch_mangle_86.Conv2d
  n_Conv_88 : __torch__.torch.nn.modules.conv.___torch_mangle_87.Conv2d
  n_Conv_89 : __torch__.torch.nn.modules.conv.___torch_mangle_88.Conv2d
  n_Conv_90 : __torch__.torch.nn.modules.conv.___torch_mangle_89.Conv2d
  n_Conv_91 : __torch__.torch.nn.modules.conv.___torch_mangle_90.Conv2d
  n_Conv_92 : __torch__.torch.nn.modules.conv.___torch_mangle_91.Conv2d
  n_Conv_93 : __torch__.torch.nn.modules.conv.___torch_mangle_92.Conv2d
  n_Conv_94 : __torch__.torch.nn.modules.conv.___torch_mangle_93.Conv2d
  n_Conv_95 : __torch__.torch.nn.modules.conv.___torch_mangle_94.Conv2d
  n_Conv_96 : __torch__.torch.nn.modules.conv.___torch_mangle_95.Conv2d
  n_Conv_97 : __torch__.torch.nn.modules.conv.___torch_mangle_96.Conv2d
  n_Conv_98 : __torch__.torch.nn.modules.conv.___torch_mangle_97.Conv2d
  n_Conv_99 : __torch__.torch.nn.modules.conv.___torch_mangle_98.Conv2d
  n_Conv_100 : __torch__.torch.nn.modules.conv.___torch_mangle_99.Conv2d
  n_Conv_101 : __torch__.torch.nn.modules.conv.___torch_mangle_100.Conv2d
  n_Conv_102 : __torch__.torch.nn.modules.conv.___torch_mangle_101.Conv2d
  n_Conv_103 : __torch__.torch.nn.modules.conv.___torch_mangle_102.Conv2d
  n_Conv_104 : __torch__.torch.nn.modules.conv.___torch_mangle_103.Conv2d
  n_Conv_105 : __torch__.torch.nn.modules.conv.___torch_mangle_104.Conv2d
  n_Conv_106 : __torch__.torch.nn.modules.conv.___torch_mangle_105.Conv2d
  n_Conv_107 : __torch__.torch.nn.modules.conv.___torch_mangle_106.Conv2d
  n_Conv_108 : __torch__.torch.nn.modules.conv.___torch_mangle_107.Conv2d
  n_Conv_109 : __torch__.torch.nn.modules.conv.___torch_mangle_108.Conv2d
  n_Conv_110 : __torch__.torch.nn.modules.conv.___torch_mangle_109.Conv2d
  n_Conv_111 : __torch__.torch.nn.modules.conv.___torch_mangle_110.Conv2d
  n_Conv_112 : __torch__.torch.nn.modules.conv.___torch_mangle_111.Conv2d
  n_Conv_113 : __torch__.torch.nn.modules.conv.___torch_mangle_112.Conv2d
  n_Conv_114 : __torch__.torch.nn.modules.conv.___torch_mangle_113.Conv2d
  n_Conv_115 : __torch__.torch.nn.modules.conv.___torch_mangle_114.Conv2d
  n_Conv_116 : __torch__.torch.nn.modules.conv.___torch_mangle_115.Conv2d
  n_Conv_117 : __torch__.torch.nn.modules.conv.___torch_mangle_116.Conv2d
  n_Conv_118 : __torch__.torch.nn.modules.conv.___torch_mangle_117.Conv2d
  n_Conv_119 : __torch__.torch.nn.modules.conv.___torch_mangle_118.Conv2d
  n_Conv_120 : __torch__.torch.nn.modules.conv.___torch_mangle_119.Conv2d
  n_Conv_121 : __torch__.torch.nn.modules.conv.___torch_mangle_120.Conv2d
  n_Conv_122 : __torch__.torch.nn.modules.conv.___torch_mangle_121.Conv2d
  n_Conv_123 : __torch__.torch.nn.modules.conv.___torch_mangle_122.Conv2d
  n_Conv_124 : __torch__.torch.nn.modules.conv.___torch_mangle_123.Conv2d
  n_Conv_125 : __torch__.torch.nn.modules.conv.___torch_mangle_124.Conv2d
  n_Conv_126 : __torch__.torch.nn.modules.conv.___torch_mangle_125.Conv2d
  n_Conv_127 : __torch__.torch.nn.modules.conv.___torch_mangle_126.Conv2d
  n_Conv_128 : __torch__.torch.nn.modules.conv.___torch_mangle_127.Conv2d
  n_Conv_129 : __torch__.torch.nn.modules.conv.___torch_mangle_128.Conv2d
  n_Conv_130 : __torch__.torch.nn.modules.conv.___torch_mangle_129.Conv2d
  n_Conv_131 : __torch__.torch.nn.modules.conv.___torch_mangle_130.Conv2d
  n_Conv_132 : __torch__.torch.nn.modules.conv.___torch_mangle_131.Conv2d
  n_Conv_133 : __torch__.torch.nn.modules.conv.___torch_mangle_132.Conv2d
  n_Conv_134 : __torch__.torch.nn.modules.conv.___torch_mangle_133.Conv2d
  n_Conv_135 : __torch__.torch.nn.modules.conv.___torch_mangle_134.Conv2d
  n_Conv_136 : __torch__.torch.nn.modules.conv.___torch_mangle_135.Conv2d
  n_Conv_137 : __torch__.torch.nn.modules.conv.___torch_mangle_136.Conv2d
  n_Conv_138 : __torch__.torch.nn.modules.conv.___torch_mangle_137.Conv2d
  n_Conv_139 : __torch__.torch.nn.modules.conv.___torch_mangle_138.Conv2d
  n_Conv_140 : __torch__.torch.nn.modules.conv.___torch_mangle_139.Conv2d
  n_Conv_141 : __torch__.torch.nn.modules.conv.___torch_mangle_140.Conv2d
  n_Conv_142 : __torch__.torch.nn.modules.conv.___torch_mangle_141.Conv2d
  n_Conv_143 : __torch__.torch.nn.modules.conv.___torch_mangle_142.Conv2d
  n_Conv_144 : __torch__.torch.nn.modules.conv.___torch_mangle_143.Conv2d
  n_Conv_145 : __torch__.torch.nn.modules.conv.___torch_mangle_144.Conv2d
  n_Conv_146 : __torch__.torch.nn.modules.conv.___torch_mangle_145.Conv2d
  n_Conv_147 : __torch__.torch.nn.modules.conv.___torch_mangle_146.Conv2d
  n_Conv_148 : __torch__.torch.nn.modules.conv.___torch_mangle_147.Conv2d
  n_Conv_149 : __torch__.torch.nn.modules.conv.___torch_mangle_148.Conv2d
  n_Conv_150 : __torch__.torch.nn.modules.conv.___torch_mangle_149.Conv2d
  n_Conv_151 : __torch__.torch.nn.modules.conv.___torch_mangle_150.Conv2d
  n_Conv_152 : __torch__.torch.nn.modules.conv.___torch_mangle_151.Conv2d
  n_Conv_153 : __torch__.torch.nn.modules.conv.___torch_mangle_152.Conv2d
  n_Conv_154 : __torch__.torch.nn.modules.conv.___torch_mangle_153.Conv2d
  n_Conv_155 : __torch__.torch.nn.modules.conv.___torch_mangle_154.Conv2d
  n_Conv_156 : __torch__.torch.nn.modules.conv.___torch_mangle_155.Conv2d
  n_Conv_157 : __torch__.torch.nn.modules.conv.___torch_mangle_156.Conv2d
  n_Conv_158 : __torch__.torch.nn.modules.conv.___torch_mangle_157.Conv2d
  n_Conv_159 : __torch__.torch.nn.modules.conv.___torch_mangle_158.Conv2d
  n_Conv_160 : __torch__.torch.nn.modules.conv.___torch_mangle_159.Conv2d
  n_Conv_161 : __torch__.torch.nn.modules.conv.___torch_mangle_160.Conv2d
  n_Conv_162 : __torch__.torch.nn.modules.conv.___torch_mangle_161.Conv2d
  n_Conv_163 : __torch__.torch.nn.modules.conv.___torch_mangle_162.Conv2d
  n_Conv_164 : __torch__.torch.nn.modules.conv.___torch_mangle_163.Conv2d
  n_Conv_165 : __torch__.torch.nn.modules.conv.___torch_mangle_164.Conv2d
  n_Conv_166 : __torch__.torch.nn.modules.conv.___torch_mangle_165.Conv2d
  n_Conv_167 : __torch__.torch.nn.modules.conv.___torch_mangle_166.Conv2d
  n_Conv_168 : __torch__.torch.nn.modules.conv.___torch_mangle_167.Conv2d
  n_Conv_169 : __torch__.torch.nn.modules.conv.___torch_mangle_168.Conv2d
  n_Conv_170 : __torch__.torch.nn.modules.conv.___torch_mangle_169.Conv2d
  n_Conv_171 : __torch__.torch.nn.modules.conv.___torch_mangle_170.Conv2d
  n_Conv_172 : __torch__.torch.nn.modules.conv.___torch_mangle_171.Conv2d
  n_Conv_173 : __torch__.torch.nn.modules.conv.___torch_mangle_172.Conv2d
  n_Conv_174 : __torch__.torch.nn.modules.conv.___torch_mangle_173.Conv2d
  n_Conv_175 : __torch__.torch.nn.modules.conv.___torch_mangle_174.Conv2d
  n_Conv_176 : __torch__.torch.nn.modules.conv.___torch_mangle_175.Conv2d
  n_Conv_177 : __torch__.torch.nn.modules.conv.___torch_mangle_176.Conv2d
  n_Conv_178 : __torch__.torch.nn.modules.conv.___torch_mangle_177.Conv2d
  def forward(self: __torch__.deep_danbooru_model.DeepDanbooruModel,
    inputs: Tensor) -> Tensor:
    n_Conv_178 = self.n_Conv_178
    n_Conv_177 = self.n_Conv_177
    n_Conv_176 = self.n_Conv_176
    n_Conv_175 = self.n_Conv_175
    n_Conv_174 = self.n_Conv_174
    n_Conv_173 = self.n_Conv_173
    n_Conv_172 = self.n_Conv_172
    n_Conv_171 = self.n_Conv_171
    n_Conv_170 = self.n_Conv_170
    n_Conv_169 = self.n_Conv_169
    n_Conv_168 = self.n_Conv_168
    n_Conv_167 = self.n_Conv_167
    n_Conv_166 = self.n_Conv_166
    n_Conv_165 = self.n_Conv_165
    n_Conv_164 = self.n_Conv_164
    n_Conv_163 = self.n_Conv_163
    n_Conv_162 = self.n_Conv_162
    n_Conv_161 = self.n_Conv_161
    n_Conv_160 = self.n_Conv_160
    n_Conv_159 = self.n_Conv_159
    n_Conv_158 = self.n_Conv_158
    n_Conv_157 = self.n_Conv_157
    n_Conv_156 = self.n_Conv_156
    n_Conv_155 = self.n_Conv_155
    n_Conv_154 = self.n_Conv_154
    n_Conv_153 = self.n_Conv_153
    n_Conv_152 = self.n_Conv_152
    n_Conv_151 = self.n_Conv_151
    n_Conv_150 = self.n_Conv_150
    n_Conv_149 = self.n_Conv_149
    n_Conv_148 = self.n_Conv_148
    n_Conv_147 = self.n_Conv_147
    n_Conv_146 = self.n_Conv_146
    n_Conv_145 = self.n_Conv_145
    n_Conv_144 = self.n_Conv_144
    n_Conv_143 = self.n_Conv_143
    n_Conv_142 = self.n_Conv_142
    n_Conv_141 = self.n_Conv_141
    n_Conv_140 = self.n_Conv_140
    n_Conv_139 = self.n_Conv_139
    n_Conv_138 = self.n_Conv_138
    n_Conv_137 = self.n_Conv_137
    n_Conv_136 = self.n_Conv_136
    n_Conv_135 = self.n_Conv_135
    n_Conv_134 = self.n_Conv_134
    n_Conv_133 = self.n_Conv_133
    n_Conv_132 = self.n_Conv_132
    n_Conv_131 = self.n_Conv_131
    n_Conv_130 = self.n_Conv_130
    n_Conv_129 = self.n_Conv_129
    n_Conv_128 = self.n_Conv_128
    n_Conv_127 = self.n_Conv_127
    n_Conv_126 = self.n_Conv_126
    n_Conv_125 = self.n_Conv_125
    n_Conv_124 = self.n_Conv_124
    n_Conv_123 = self.n_Conv_123
    n_Conv_122 = self.n_Conv_122
    n_Conv_121 = self.n_Conv_121
    n_Conv_120 = self.n_Conv_120
    n_Conv_119 = self.n_Conv_119
    n_Conv_118 = self.n_Conv_118
    n_Conv_117 = self.n_Conv_117
    n_Conv_116 = self.n_Conv_116
    n_Conv_115 = self.n_Conv_115
    n_Conv_114 = self.n_Conv_114
    n_Conv_113 = self.n_Conv_113
    n_Conv_112 = self.n_Conv_112
    n_Conv_111 = self.n_Conv_111
    n_Conv_110 = self.n_Conv_110
    n_Conv_109 = self.n_Conv_109
    n_Conv_108 = self.n_Conv_108
    n_Conv_107 = self.n_Conv_107
    n_Conv_106 = self.n_Conv_106
    n_Conv_105 = self.n_Conv_105
    n_Conv_104 = self.n_Conv_104
    n_Conv_103 = self.n_Conv_103
    n_Conv_102 = self.n_Conv_102
    n_Conv_101 = self.n_Conv_101
    n_Conv_100 = self.n_Conv_100
    n_Conv_99 = self.n_Conv_99
    n_Conv_98 = self.n_Conv_98
    n_Conv_97 = self.n_Conv_97
    n_Conv_96 = self.n_Conv_96
    n_Conv_95 = self.n_Conv_95
    n_Conv_94 = self.n_Conv_94
    n_Conv_93 = self.n_Conv_93
    n_Conv_92 = self.n_Conv_92
    n_Conv_91 = self.n_Conv_91
    n_Conv_90 = self.n_Conv_90
    n_Conv_89 = self.n_Conv_89
    n_Conv_88 = self.n_Conv_88
    n_Conv_87 = self.n_Conv_87
    n_Conv_86 = self.n_Conv_86
    n_Conv_85 = self.n_Conv_85
    n_Conv_84 = self.n_Conv_84
    n_Conv_83 = self.n_Conv_83
    n_Conv_82 = self.n_Conv_82
    n_Conv_81 = self.n_Conv_81
    n_Conv_80 = self.n_Conv_80
    n_Conv_79 = self.n_Conv_79
    n_Conv_78 = self.n_Conv_78
    n_Conv_77 = self.n_Conv_77
    n_Conv_76 = self.n_Conv_76
    n_Conv_75 = self.n_Conv_75
    n_Conv_74 = self.n_Conv_74
    n_Conv_73 = self.n_Conv_73
    n_Conv_72 = self.n_Conv_72
    n_Conv_71 = self.n_Conv_71
    n_Conv_70 = self.n_Conv_70
    n_Conv_69 = self.n_Conv_69
    n_Conv_68 = self.n_Conv_68
    n_Conv_67 = self.n_Conv_67
    n_Conv_66 = self.n_Conv_66
    n_Conv_65 = self.n_Conv_65
    n_Conv_64 = self.n_Conv_64
    n_Conv_63 = self.n_Conv_63
    n_Conv_62 = self.n_Conv_62
    n_Conv_61 = self.n_Conv_61
    n_Conv_60 = self.n_Conv_60
    n_Conv_59 = self.n_Conv_59
    n_Conv_58 = self.n_Conv_58
    n_Conv_57 = self.n_Conv_57
    n_Conv_56 = self.n_Conv_56
    n_Conv_55 = self.n_Conv_55
    n_Conv_54 = self.n_Conv_54
    n_Conv_53 = self.n_Conv_53
    n_Conv_52 = self.n_Conv_52
    n_Conv_51 = self.n_Conv_51
    n_Conv_50 = self.n_Conv_50
    n_Conv_49 = self.n_Conv_49
    n_Conv_48 = self.n_Conv_48
    n_Conv_47 = self.n_Conv_47
    n_Conv_46 = self.n_Conv_46
    n_Conv_45 = self.n_Conv_45
    n_Conv_44 = self.n_Conv_44
    n_Conv_43 = self.n_Conv_43
    n_Conv_42 = self.n_Conv_42
    n_Conv_41 = self.n_Conv_41
    n_Conv_40 = self.n_Conv_40
    n_Conv_39 = self.n_Conv_39
    n_Conv_38 = self.n_Conv_38
    n_Conv_37 = self.n_Conv_37
    n_Conv_36 = self.n_Conv_36
    n_Conv_35 = self.n_Conv_35
    n_Conv_34 = self.n_Conv_34
    n_Conv_33 = self.n_Conv_33
    n_Conv_32 = self.n_Conv_32
    n_Conv_31 = self.n_Conv_31
    n_Conv_30 = self.n_Conv_30
    n_Conv_29 = self.n_Conv_29
    n_Conv_28 = self.n_Conv_28
    n_Conv_27 = self.n_Conv_27
    n_Conv_26 = self.n_Conv_26
    n_Conv_25 = self.n_Conv_25
    n_Conv_24 = self.n_Conv_24
    n_Conv_23 = self.n_Conv_23
    n_Conv_22 = self.n_Conv_22
    n_Conv_21 = self.n_Conv_21
    n_Conv_20 = self.n_Conv_20
    n_Conv_19 = self.n_Conv_19
    n_Conv_18 = self.n_Conv_18
    n_Conv_17 = self.n_Conv_17
    n_Conv_16 = self.n_Conv_16
    n_Conv_15 = self.n_Conv_15
    n_Conv_14 = self.n_Conv_14
    n_Conv_13 = self.n_Conv_13
    n_Conv_12 = self.n_Conv_12
    n_Conv_11 = self.n_Conv_11
    n_Conv_10 = self.n_Conv_10
    n_Conv_9 = self.n_Conv_9
    n_Conv_8 = self.n_Conv_8
    n_Conv_7 = self.n_Conv_7
    n_Conv_6 = self.n_Conv_6
    n_Conv_5 = self.n_Conv_5
    n_Conv_4 = self.n_Conv_4
    n_Conv_3 = self.n_Conv_3
    n_Conv_2 = self.n_Conv_2
    n_Conv_1 = self.n_Conv_1
    n_MaxPool_0 = self.n_MaxPool_0
    n_Conv_0 = self.n_Conv_0
    t_359 = torch.permute(inputs, [0, 3, 1, 2])
    input = torch.pad(t_359, [2, 3, 2, 3], "constant", 0.)
    t_361 = torch.relu((n_Conv_0).forward(input, ))
    input0 = torch.pad(t_361, [0, 1, 0, 1], "constant", -inf)
    _0 = torch.max_pool2d(input0, [3, 3], [2, 2], [0, 0], [1, 1])
    _1 = (n_Conv_1).forward(_0, )
    t_365 = torch.relu((n_Conv_2).forward(_0, ))
    input1 = torch.pad(t_365, [1, 1, 1, 1], "constant", 0.)
    input2 = torch.relu((n_Conv_3).forward(input1, ))
    input3 = torch.add((n_Conv_4).forward(input2, ), _1)
    input4 = torch.relu(input3)
    t_372 = torch.relu((n_Conv_5).forward(input4, ))
    input5 = torch.pad(t_372, [1, 1, 1, 1], "constant", 0.)
    input6 = torch.relu((n_Conv_6).forward(input5, ))
    input7 = torch.add((n_Conv_7).forward(input6, ), input4)
    input8 = torch.relu(input7)
    t_379 = torch.relu((n_Conv_8).forward(input8, ))
    input9 = torch.pad(t_379, [1, 1, 1, 1], "constant", 0.)
    input10 = torch.relu((n_Conv_9).forward(input9, ))
    input11 = torch.add((n_Conv_10).forward(input10, ), input8)
    input12 = torch.relu(input11)
    _2 = (n_Conv_11).forward(input12, )
    t_387 = torch.relu((n_Conv_12).forward(input12, ))
    input13 = torch.pad(t_387, [0, 1, 0, 1], "constant", 0.)
    input14 = torch.relu((n_Conv_13).forward(input13, ))
    input15 = torch.add((n_Conv_14).forward(input14, ), _2)
    input16 = torch.relu(input15)
    t_394 = torch.relu((n_Conv_15).forward(input16, ))
    input17 = torch.pad(t_394, [1, 1, 1, 1], "constant", 0.)
    input18 = torch.relu((n_Conv_16).forward(input17, ))
    input19 = torch.add((n_Conv_17).forward(input18, ), input16)
    input20 = torch.relu(input19)
    t_401 = torch.relu((n_Conv_18).forward(input20, ))
    input21 = torch.pad(t_401, [1, 1, 1, 1], "constant", 0.)
    input22 = torch.relu((n_Conv_19).forward(input21, ))
    input23 = torch.add((n_Conv_20).forward(input22, ), input20)
    input24 = torch.relu(input23)
    t_408 = torch.relu((n_Conv_21).forward(input24, ))
    input25 = torch.pad(t_408, [1, 1, 1, 1], "constant", 0.)
    input26 = torch.relu((n_Conv_22).forward(input25, ))
    input27 = torch.add((n_Conv_23).forward(input26, ), input24)
    input28 = torch.relu(input27)
    t_415 = torch.relu((n_Conv_24).forward(input28, ))
    input29 = torch.pad(t_415, [1, 1, 1, 1], "constant", 0.)
    input30 = torch.relu((n_Conv_25).forward(input29, ))
    input31 = torch.add((n_Conv_26).forward(input30, ), input28)
    input32 = torch.relu(input31)
    t_422 = torch.relu((n_Conv_27).forward(input32, ))
    input33 = torch.pad(t_422, [1, 1, 1, 1], "constant", 0.)
    input34 = torch.relu((n_Conv_28).forward(input33, ))
    input35 = torch.add((n_Conv_29).forward(input34, ), input32)
    input36 = torch.relu(input35)
    t_429 = torch.relu((n_Conv_30).forward(input36, ))
    input37 = torch.pad(t_429, [1, 1, 1, 1], "constant", 0.)
    input38 = torch.relu((n_Conv_31).forward(input37, ))
    input39 = torch.add((n_Conv_32).forward(input38, ), input36)
    input40 = torch.relu(input39)
    t_436 = torch.relu((n_Conv_33).forward(input40, ))
    input41 = torch.pad(t_436, [1, 1, 1, 1], "constant", 0.)
    input42 = torch.relu((n_Conv_34).forward(input41, ))
    input43 = torch.add((n_Conv_35).forward(input42, ), input40)
    input44 = torch.relu(input43)
    _3 = (n_Conv_36).forward(input44, )
    t_444 = torch.relu((n_Conv_37).forward(input44, ))
    input45 = torch.pad(t_444, [0, 1, 0, 1], "constant", 0.)
    input46 = torch.relu((n_Conv_38).forward(input45, ))
    input47 = torch.add((n_Conv_39).forward(input46, ), _3)
    input48 = torch.relu(input47)
    t_451 = torch.relu((n_Conv_40).forward(input48, ))
    input49 = torch.pad(t_451, [1, 1, 1, 1], "constant", 0.)
    input50 = torch.relu((n_Conv_41).forward(input49, ))
    input51 = torch.add((n_Conv_42).forward(input50, ), input48)
    input52 = torch.relu(input51)
    t_458 = torch.relu((n_Conv_43).forward(input52, ))
    input53 = torch.pad(t_458, [1, 1, 1, 1], "constant", 0.)
    input54 = torch.relu((n_Conv_44).forward(input53, ))
    input55 = torch.add((n_Conv_45).forward(input54, ), input52)
    input56 = torch.relu(input55)
    t_465 = torch.relu((n_Conv_46).forward(input56, ))
    input57 = torch.pad(t_465, [1, 1, 1, 1], "constant", 0.)
    input58 = torch.relu((n_Conv_47).forward(input57, ))
    input59 = torch.add((n_Conv_48).forward(input58, ), input56)
    input60 = torch.relu(input59)
    t_472 = torch.relu((n_Conv_49).forward(input60, ))
    input61 = torch.pad(t_472, [1, 1, 1, 1], "constant", 0.)
    input62 = torch.relu((n_Conv_50).forward(input61, ))
    input63 = torch.add((n_Conv_51).forward(input62, ), input60)
    input64 = torch.relu(input63)
    t_479 = torch.relu((n_Conv_52).forward(input64, ))
    input65 = torch.pad(t_479, [1, 1, 1, 1], "constant", 0.)
    input66 = torch.relu((n_Conv_53).forward(input65, ))
    input67 = torch.add((n_Conv_54).forward(input66, ), input64)
    input68 = torch.relu(input67)
    t_486 = torch.relu((n_Conv_55).forward(input68, ))
    input69 = torch.pad(t_486, [1, 1, 1, 1], "constant", 0.)
    input70 = torch.relu((n_Conv_56).forward(input69, ))
    input71 = torch.add((n_Conv_57).forward(input70, ), input68)
    input72 = torch.relu(input71)
    t_493 = torch.relu((n_Conv_58).forward(input72, ))
    input73 = torch.pad(t_493, [1, 1, 1, 1], "constant", 0.)
    input74 = torch.relu((n_Conv_59).forward(input73, ))
    input75 = torch.add((n_Conv_60).forward(input74, ), input72)
    input76 = torch.relu(input75)
    t_500 = torch.relu((n_Conv_61).forward(input76, ))
    input77 = torch.pad(t_500, [1, 1, 1, 1], "constant", 0.)
    input78 = torch.relu((n_Conv_62).forward(input77, ))
    input79 = torch.add((n_Conv_63).forward(input78, ), input76)
    input80 = torch.relu(input79)
    t_507 = torch.relu((n_Conv_64).forward(input80, ))
    input81 = torch.pad(t_507, [1, 1, 1, 1], "constant", 0.)
    input82 = torch.relu((n_Conv_65).forward(input81, ))
    input83 = torch.add((n_Conv_66).forward(input82, ), input80)
    input84 = torch.relu(input83)
    t_514 = torch.relu((n_Conv_67).forward(input84, ))
    input85 = torch.pad(t_514, [1, 1, 1, 1], "constant", 0.)
    input86 = torch.relu((n_Conv_68).forward(input85, ))
    input87 = torch.add((n_Conv_69).forward(input86, ), input84)
    input88 = torch.relu(input87)
    t_521 = torch.relu((n_Conv_70).forward(input88, ))
    input89 = torch.pad(t_521, [1, 1, 1, 1], "constant", 0.)
    input90 = torch.relu((n_Conv_71).forward(input89, ))
    input91 = torch.add((n_Conv_72).forward(input90, ), input88)
    input92 = torch.relu(input91)
    t_528 = torch.relu((n_Conv_73).forward(input92, ))
    input93 = torch.pad(t_528, [1, 1, 1, 1], "constant", 0.)
    input94 = torch.relu((n_Conv_74).forward(input93, ))
    input95 = torch.add((n_Conv_75).forward(input94, ), input92)
    input96 = torch.relu(input95)
    t_535 = torch.relu((n_Conv_76).forward(input96, ))
    input97 = torch.pad(t_535, [1, 1, 1, 1], "constant", 0.)
    input98 = torch.relu((n_Conv_77).forward(input97, ))
    input99 = torch.add((n_Conv_78).forward(input98, ), input96)
    input100 = torch.relu(input99)
    t_542 = torch.relu((n_Conv_79).forward(input100, ))
    input101 = torch.pad(t_542, [1, 1, 1, 1], "constant", 0.)
    input102 = torch.relu((n_Conv_80).forward(input101, ))
    input103 = torch.add((n_Conv_81).forward(input102, ), input100)
    input104 = torch.relu(input103)
    t_549 = torch.relu((n_Conv_82).forward(input104, ))
    input105 = torch.pad(t_549, [1, 1, 1, 1], "constant", 0.)
    input106 = torch.relu((n_Conv_83).forward(input105, ))
    input107 = torch.add((n_Conv_84).forward(input106, ), input104)
    input108 = torch.relu(input107)
    t_556 = torch.relu((n_Conv_85).forward(input108, ))
    input109 = torch.pad(t_556, [1, 1, 1, 1], "constant", 0.)
    input110 = torch.relu((n_Conv_86).forward(input109, ))
    input111 = torch.add((n_Conv_87).forward(input110, ), input108)
    input112 = torch.relu(input111)
    t_563 = torch.relu((n_Conv_88).forward(input112, ))
    input113 = torch.pad(t_563, [1, 1, 1, 1], "constant", 0.)
    input114 = torch.relu((n_Conv_89).forward(input113, ))
    input115 = torch.add((n_Conv_90).forward(input114, ), input112)
    input116 = torch.relu(input115)
    t_570 = torch.relu((n_Conv_91).forward(input116, ))
    input117 = torch.pad(t_570, [1, 1, 1, 1], "constant", 0.)
    input118 = torch.relu((n_Conv_92).forward(input117, ))
    input119 = torch.add((n_Conv_93).forward(input118, ), input116)
    input120 = torch.relu(input119)
    t_577 = torch.relu((n_Conv_94).forward(input120, ))
    input121 = torch.pad(t_577, [1, 1, 1, 1], "constant", 0.)
    input122 = torch.relu((n_Conv_95).forward(input121, ))
    input123 = torch.add((n_Conv_96).forward(input122, ), input120)
    input124 = torch.relu(input123)
    t_584 = torch.relu((n_Conv_97).forward(input124, ))
    input125 = torch.pad(t_584, [0, 1, 0, 1], "constant", 0.)
    input126 = torch.relu((n_Conv_98).forward(input125, ))
    input127 = torch.add((n_Conv_99).forward(input126, ), (n_Conv_100).forward(input124, ))
    input128 = torch.relu(input127)
    t_592 = torch.relu((n_Conv_101).forward(input128, ))
    input129 = torch.pad(t_592, [1, 1, 1, 1], "constant", 0.)
    input130 = torch.relu((n_Conv_102).forward(input129, ))
    input131 = torch.add((n_Conv_103).forward(input130, ), input128)
    input132 = torch.relu(input131)
    t_599 = torch.relu((n_Conv_104).forward(input132, ))
    input133 = torch.pad(t_599, [1, 1, 1, 1], "constant", 0.)
    input134 = torch.relu((n_Conv_105).forward(input133, ))
    input135 = torch.add((n_Conv_106).forward(input134, ), input132)
    input136 = torch.relu(input135)
    t_606 = torch.relu((n_Conv_107).forward(input136, ))
    input137 = torch.pad(t_606, [1, 1, 1, 1], "constant", 0.)
    input138 = torch.relu((n_Conv_108).forward(input137, ))
    input139 = torch.add((n_Conv_109).forward(input138, ), input136)
    input140 = torch.relu(input139)
    t_613 = torch.relu((n_Conv_110).forward(input140, ))
    input141 = torch.pad(t_613, [1, 1, 1, 1], "constant", 0.)
    input142 = torch.relu((n_Conv_111).forward(input141, ))
    input143 = torch.add((n_Conv_112).forward(input142, ), input140)
    input144 = torch.relu(input143)
    t_620 = torch.relu((n_Conv_113).forward(input144, ))
    input145 = torch.pad(t_620, [1, 1, 1, 1], "constant", 0.)
    input146 = torch.relu((n_Conv_114).forward(input145, ))
    input147 = torch.add((n_Conv_115).forward(input146, ), input144)
    input148 = torch.relu(input147)
    t_627 = torch.relu((n_Conv_116).forward(input148, ))
    input149 = torch.pad(t_627, [1, 1, 1, 1], "constant", 0.)
    input150 = torch.relu((n_Conv_117).forward(input149, ))
    input151 = torch.add((n_Conv_118).forward(input150, ), input148)
    input152 = torch.relu(input151)
    t_634 = torch.relu((n_Conv_119).forward(input152, ))
    input153 = torch.pad(t_634, [1, 1, 1, 1], "constant", 0.)
    input154 = torch.relu((n_Conv_120).forward(input153, ))
    input155 = torch.add((n_Conv_121).forward(input154, ), input152)
    input156 = torch.relu(input155)
    t_641 = torch.relu((n_Conv_122).forward(input156, ))
    input157 = torch.pad(t_641, [1, 1, 1, 1], "constant", 0.)
    input158 = torch.relu((n_Conv_123).forward(input157, ))
    input159 = torch.add((n_Conv_124).forward(input158, ), input156)
    input160 = torch.relu(input159)
    t_648 = torch.relu((n_Conv_125).forward(input160, ))
    input161 = torch.pad(t_648, [1, 1, 1, 1], "constant", 0.)
    input162 = torch.relu((n_Conv_126).forward(input161, ))
    input163 = torch.add((n_Conv_127).forward(input162, ), input160)
    input164 = torch.relu(input163)
    t_655 = torch.relu((n_Conv_128).forward(input164, ))
    input165 = torch.pad(t_655, [1, 1, 1, 1], "constant", 0.)
    input166 = torch.relu((n_Conv_129).forward(input165, ))
    input167 = torch.add((n_Conv_130).forward(input166, ), input164)
    input168 = torch.relu(input167)
    t_662 = torch.relu((n_Conv_131).forward(input168, ))
    input169 = torch.pad(t_662, [1, 1, 1, 1], "constant", 0.)
    input170 = torch.relu((n_Conv_132).forward(input169, ))
    input171 = torch.add((n_Conv_133).forward(input170, ), input168)
    input172 = torch.relu(input171)
    t_669 = torch.relu((n_Conv_134).forward(input172, ))
    input173 = torch.pad(t_669, [1, 1, 1, 1], "constant", 0.)
    input174 = torch.relu((n_Conv_135).forward(input173, ))
    input175 = torch.add((n_Conv_136).forward(input174, ), input172)
    input176 = torch.relu(input175)
    t_676 = torch.relu((n_Conv_137).forward(input176, ))
    input177 = torch.pad(t_676, [1, 1, 1, 1], "constant", 0.)
    input178 = torch.relu((n_Conv_138).forward(input177, ))
    input179 = torch.add((n_Conv_139).forward(input178, ), input176)
    input180 = torch.relu(input179)
    t_683 = torch.relu((n_Conv_140).forward(input180, ))
    input181 = torch.pad(t_683, [1, 1, 1, 1], "constant", 0.)
    input182 = torch.relu((n_Conv_141).forward(input181, ))
    input183 = torch.add((n_Conv_142).forward(input182, ), input180)
    input184 = torch.relu(input183)
    t_690 = torch.relu((n_Conv_143).forward(input184, ))
    input185 = torch.pad(t_690, [1, 1, 1, 1], "constant", 0.)
    input186 = torch.relu((n_Conv_144).forward(input185, ))
    input187 = torch.add((n_Conv_145).forward(input186, ), input184)
    input188 = torch.relu(input187)
    t_697 = torch.relu((n_Conv_146).forward(input188, ))
    input189 = torch.pad(t_697, [1, 1, 1, 1], "constant", 0.)
    input190 = torch.relu((n_Conv_147).forward(input189, ))
    input191 = torch.add((n_Conv_148).forward(input190, ), input188)
    input192 = torch.relu(input191)
    t_704 = torch.relu((n_Conv_149).forward(input192, ))
    input193 = torch.pad(t_704, [1, 1, 1, 1], "constant", 0.)
    input194 = torch.relu((n_Conv_150).forward(input193, ))
    input195 = torch.add((n_Conv_151).forward(input194, ), input192)
    input196 = torch.relu(input195)
    t_711 = torch.relu((n_Conv_152).forward(input196, ))
    input197 = torch.pad(t_711, [1, 1, 1, 1], "constant", 0.)
    input198 = torch.relu((n_Conv_153).forward(input197, ))
    input199 = torch.add((n_Conv_154).forward(input198, ), input196)
    input200 = torch.relu(input199)
    t_718 = torch.relu((n_Conv_155).forward(input200, ))
    input201 = torch.pad(t_718, [1, 1, 1, 1], "constant", 0.)
    input202 = torch.relu((n_Conv_156).forward(input201, ))
    input203 = torch.add((n_Conv_157).forward(input202, ), input200)
    input204 = torch.relu(input203)
    _4 = (n_Conv_158).forward(input204, )
    t_726 = torch.relu((n_Conv_159).forward(input204, ))
    input205 = torch.pad(t_726, [0, 1, 0, 1], "constant", 0.)
    input206 = torch.relu((n_Conv_160).forward(input205, ))
    input207 = torch.add((n_Conv_161).forward(input206, ), _4)
    input208 = torch.relu(input207)
    t_733 = torch.relu((n_Conv_162).forward(input208, ))
    input209 = torch.pad(t_733, [1, 1, 1, 1], "constant", 0.)
    input210 = torch.relu((n_Conv_163).forward(input209, ))
    input211 = torch.add((n_Conv_164).forward(input210, ), input208)
    input212 = torch.relu(input211)
    t_740 = torch.relu((n_Conv_165).forward(input212, ))
    input213 = torch.pad(t_740, [1, 1, 1, 1], "constant", 0.)
    input214 = torch.relu((n_Conv_166).forward(input213, ))
    input215 = torch.add((n_Conv_167).forward(input214, ), input212)
    input216 = torch.relu(input215)
    _5 = (n_Conv_168).forward(input216, )
    t_748 = torch.relu((n_Conv_169).forward(input216, ))
    input217 = torch.pad(t_748, [0, 1, 0, 1], "constant", 0.)
    input218 = torch.relu((n_Conv_170).forward(input217, ))
    input219 = torch.add((n_Conv_171).forward(input218, ), _5)
    input220 = torch.relu(input219)
    t_755 = torch.relu((n_Conv_172).forward(input220, ))
    input221 = torch.pad(t_755, [1, 1, 1, 1], "constant", 0.)
    input222 = torch.relu((n_Conv_173).forward(input221, ))
    input223 = torch.add((n_Conv_174).forward(input222, ), input220)
    input224 = torch.relu(input223)
    t_762 = torch.relu((n_Conv_175).forward(input224, ))
    input225 = torch.pad(t_762, [1, 1, 1, 1], "constant", 0.)
    input226 = torch.relu((n_Conv_176).forward(input225, ))
    input227 = torch.add((n_Conv_177).forward(input226, ), input224)
    input228 = torch.relu(input227)
    t_769 = torch.avg_pool2d((n_Conv_178).forward(input228, ), [4, 4], annotate(List[int], []), [0, 0])
    t_770 = torch.squeeze(t_769, 3)
    t_7700 = torch.squeeze(t_770, 2)
    return torch.sigmoid(t_7700)
