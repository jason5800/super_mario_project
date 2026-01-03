# 基于强化学习的超级马里奥兄弟游戏 AI 设计

本项目为2025-2026学年秋季学期《大数据分析》课程大作业，基于强化学习算法设计超级马里奥兄弟游戏的 AI 智能体。项目基于 [DI-adventure](https://github.com/opendilab/DI-adventure) 框架实现。

项目依赖可通过DI-adventure的文档说明观看。具体在mario_dqn/README.md中。

## 成果
- 训练出能够同时通关1-1～1-4关卡的智能体
- 训练出1-1关卡中能够通过钻入管道，到达地下室，成功获得21个coin的智能体
- 训练出1-1关卡中能够获得蘑菇，并且进入地下室，获得18个coin的智能体。

这三者的智能体参数均在mario_dqn/pretrained_model目录下。分别为
- multi_stage_final_a12.pth.tar
- a12_coin_21.pth.tar
- a12_coin18_tall.pth.tar

通关视频可在eval_videos文件夹中看到。

评估脚本如下
```bash
cd mario_dqn
# 评估1-1关卡中能够通过钻入管道，到达地下室，成功获得21个coin的智能体
python evaluate.py -ckpt pretrained_model/a12_coin_21.pth.tar -a 12 -o 4 -v 0 

# 评估1-1关卡中能够获得蘑菇，并且进入地下室，获得18个coin的智能体
python evaluate.py -ckpt pretrained_model/a12_coin18_tall.pth.tar -a 12 -o 4 -v 0 

# 评估能够同时通关1-1～1-4关卡的智能体
python evaluate_multiple_stage.py -ckpt pretrained_model/multi_stage_final_a12.pth.tar -a 12 -o 4 -v 0 
```
## 项目结构
- 项目结构
```bash
mario_dqn_main.py 智能体训练入口，包含训练的逻辑
mario_dqn_config.py 智能体配置文件，包含参数信息
evaluate.py 智能体评估函数
model.py 神经网络结构定义文件
policy.py 策略逻辑文件，包含经验收集、智能体评估、模型训练的逻辑
README.md 项目说明文档
requirements.txt 项目依赖目录
wrapper.py 各式各样的装饰器实现
mario_dqn_main_multiple_stage.py 多关卡训练入口，包含训练的逻辑
evaluate_multiple_stage.py 多关卡评估函数
```

在Baseline基础上额外设计了mario_dqn_main_multiple_stage.py，用于训练能够同时通关1-1～1-4关卡的智能体, 评估脚本为evaluate_multiple_stage.py。使用方法与mario_dqn_main.py相同。

在训练入口中额外设计了断点续训功能，若训练过程中中断，可通过指定-ckpt参数继续训练。

额外设计的特征空间探索机制均在wrapper.py中实现。包括
- 吃硬币奖励
- 通关奖励
- 吃蘑菇、花朵奖励
- 卡住惩罚
- 背景消除

