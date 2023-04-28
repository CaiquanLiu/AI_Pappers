|名称  |  来源   | 说明  |状态   | 备注  |
|  ----  | ----  |----  | ----  |----  |
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
| NULL  | NULL |NULL |NULL |NULL |
| NULL  | NULL |NULL |NULL |NULL |
| NULL  | NULL |NULL |NULL |NULL |
| NULL  | NULL |NULL |NULL |NULL |
| NULL  | NULL |NULL |NULL |NULL |
| NULL  | NULL |NULL |NULL |NULL |
