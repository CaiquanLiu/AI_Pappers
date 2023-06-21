|名称  |  来源   | 说明  |状态   | 备注  |
|  ----  | ----  |----  | ----  |----  |
|《ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models》| arxiv2023| ReWOO：一种大模型使用工具的优化框架<br/>1 对标ReAct框架，先整体规划执行步骤，然后，再分别调用外部接口，通过调用LLM两次就能获得最终结果；<br/>2 基于LLaMa-7B进行微调，在部分场景效果超过GPT-3.5<br/>3 随着工具变多，效果下降明显；<br/>4 整体的最终结果一般，最好的ACC也只有70%； | NULL | https://mp.weixin.qq.com/s/8cEBOwUyG0zGlC74IuFNeg |
| 《Delta Tuning: A Comprehensive Study of Parameter Efficient Methods for Pre-trained Language Models》| arxiv2022| 清华的Open Delta：<br/>1 关于Delta tuning的综述（大多数预训练参数不变，进行少量参数优化）；<br/>2 解决大模型低成本适配下游任务问题；<br/>3 讲方法总结为三类，Addition-based Methods、Specification-based Methods、Reparameterization-based Methods ；| NULL | GitHub - thunlp/OpenDelta: A plug-and-play library for parameter-efficient-tuning (Delta Tuning) |
| 《OpenPrompt: An Open-source Framework for Prompt-learning》 | arxiv2021 | 清华的OpenPrompt：<br/>1 Prompt Learning的工具包；<br/>2 和OpenDelta是一个团队（OpenPrompt更早）。OpenPrompt主要聚焦在prompt上，而OpenDelta主要聚焦在Delta-Tuning（大模型适配层或者中间层优化）； | NULL | https://zhuanlan.zhihu.com/p/607206925 |
| 《Augmented Language Models: a Survey》 | arxiv2023 | ALM：<br/>1 Yann LeCun参与的关于“增强语言模型”的综述;<br/>2 主要聚焦在Reason、Tools、Act；; | NULL | https://mp.weixin.qq.com/s/oCs4R-xYGS42iXIvgnDCCg |
| 《Check Your Facts and Try Again: Improving Large Language Models with External Knowledge and Automated Feedback》| arxiv2023| 微软的大模型增强框架：<br/>1 核心组成部分：<br/>-working memory：对话状态记录；<br/>-policy：执行动作生成，通过规则或则模型实现（文中用了基于强化学习的T5）；<br/>-utility：打分或者反馈，通过规则或者模型实现（文中没有特别声明这部分具体的实现）；<br/>-action executor：执行器，调用外部接口；<br/>2 整体设计感觉比较理想，特别是如果是模型实现policy和utility，不管是性能还是效果，感觉都难以保障；| NULL | NULL |
| 《LARGE LANGUAGE MODELS ARE HUMAN-LEVEL PROMPT ENGINEERS》| arxiv2022|APE方法：使用大模型来生成prompt<br/>1 在实践中可能速度比较慢，成本比较高（要多次调用大模型才能实现）|NULL |NULL |
| 《Learning by Distilling Context》| arxiv2022 | 上下文蒸馏：<br/>1 给大模型更多的输入提示，同时，要求大模型的输出理由和结果；<br/>2 给小模型输入较少的提示，直接输出最终结果；<br/>3 感觉核心就是通过提示让大模型输出的结果更置信，效果肯定没有纯人工构造的数据好（但机器的效率高）；| NULL | NULL |
| 《HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face》| arXiv2023| 基于ChatGPT和HuggingFace模型接口实现多模型中控（基于gpt-3.5-turbo 和 text-davinci-003模型）：<br/>1 核心目标，将用户原始query通过LLM转变成执行的任务，并最终汇总任务结果，产生回复；<br/>2 核心步骤，Task Planning、Model Selection、Task Execution、Response Generation；<br/>3 整体感觉和之前微软用语言模型控制机器人的设计思路是基本一致的；<br/>4 感觉过于理想，应用在工业场景不一定可靠（Limitations部分提到了不稳定，但感觉表述的还是有些轻描淡写了）； | NULL | NULL |
| 《REACT: SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS》| ICLR2023| 谷歌的ReAct：使用大模型作为控制中心（主要是基于3~6个few-shot的示例prompt引导后续的模型行为）：<br/>1 主要基于PaLM-540B进行的实验（也部分对比了GPT-3，text-davinci-002）；<br/>2 虽然摘要里提到相比模拟和强化学习的方案有34%和10%的提升，但最的结果也挺一般的；<br/>3 做了基于PaLM-8/62B的Finetuning，这个效果整体感觉还不错；| NULL | NULL |
| 《WebGPT: Browser-assisted question-answering with human feedback》| arxiv2022| OpenAI的WebGPT：<br/>1 基于GPT-3，借助搜索工具，提升模型的问答能力；<br/>2 核心方法：Behavior cloning（BC）、Reward modeling（RM）、Reinforcement learning（RL）、Reject sampling（best-of-n）；<br/>3 生成结果的引用是直接生成的，没有特别的处理(比如xxxx[1]，其中xxx来自文章1)| NULL | NULL |
| 《Tool Learning with Foundation Models》| arxiv2023| 大模型使用工具的综述文章：<br/>1 提出Tool Learning；<br/>2 主要聚焦在Tool-augmented Learning和Tool-oriented Learning两个方面；<br/>3 对比了text-davinci-003和ChatGPT工具使用的情况；| NULL | NULL |
| 《Toolformer: Language Models Can Teach Themselves to Use Tools》| arxiv2023| Meta的ToolFormer：<br/>1 模型自动选择API和填充API的输入，结合API结果获得最终的答案；<br/>2 主要完成类似完形填空的任务，对真实场景的任务感觉借鉴意义不大；<br/>3 结合语言模型的能力自动构建训练集，并实现模型的FineTuning（设计比较巧妙）；<br/>4 主要基于GPT-J进行试验（124M、355M、775M、1.6B），同时，对比了OPT-66B和GPT-3-175B的结果；| NULL | NULL |
| 《Unlimiformer: Long-Range Transformers with Unlimited Length Input》 | arxiv2023| 解决长文本输入的Unlimiformer：<br/>1 主要应用于Encoder-Decoder场景；<br/>2 先从长文本中检索相关信息，然后，再进行生成生成，过程是动态的；<br/>3 在测试集效果提升上不明显，主要原因是传统的评估手段不能很好的体现出优势（用Entity mentions等方法就比较明显了）； | NULL | NULL |
| 《LLMs for Knowledge Graph Construction and Reasoning: Recent Capabilities and Future Opportunities》| arxiv2023| 大模型在图谱领域的探索：<br/>1 对比评测大模型对图谱中基础任务的表现（理解类能力不如经典方法，推理能力更强。但文中也说了理解能力的评测不严谨）；<br/>2 评估大模型能力的来源，来自记忆，还是来自真正的理解能力？专门构造了一个大模型之前没见过的虚拟数据集，结论是大模型有真正的理解能力；<br/>3 提出了AutoKG框架，能够自动构建KG和进行推理（整体很模糊）；<br/>4 总体上感觉这篇文章太水了，没什么真正有价值的结论；| NULL | https://mp.weixin.qq.com/s/7DQfUUjCrMRMiPv13CYCpA |
| NULL  | NULL |NULL |NULL |NULL |
| NULL  | NULL |NULL |NULL |NULL |
| NULL  | NULL |NULL |NULL |NULL |
| NULL  | NULL |NULL |NULL |NULL |
| NULL  | NULL |NULL |NULL |NULL |
| NULL  | NULL |NULL |NULL |NULL |
