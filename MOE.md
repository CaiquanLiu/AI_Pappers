|名称  |  来源   | 说明  |状态   | 备注  |
|  ----  | ----  |----  | ----  |----  |
| NULL  | NULL |NULL |NULL |NULL |
| 《GLaM: Efficient Scaling of Language Models with Mixture-of-Experts》 | arxiv2022| Google的MOE模型：Decoder-only<br/>1 模型结果主要参考GShard MoE Transformer（Encoder-decoder，2021）；<br/>2 卖点：MoE Decoder-only，参数1.2T/96.6B（之前的工作Switch-C，MoE Encoder-decoder，1.5T/1.5B）;<br/>3 效果上超过GPT-3，同时，在训练和推理的能量消耗更小；<br/>4 一共64个专家，每次选中2个；| NULL | NULL |
