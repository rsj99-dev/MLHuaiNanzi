# MLHuaiNanzi 淮南子机器学习

**基于蛋白质组序列的古菌生长温度预测工具。**

利用偏最小二乘回归（PLS）对 420 维氨基酸组成特征（20 种氨基酸频率 + 400 种二肽频率）
进行建模，从基因组蛋白质序列（.faa 文件）预测最低生长温度 (T_min)、最适生长温度
(T_opt) 和最高生长温度 (T_max)。

- **作者**：任师杰 (rsj99)
- **邮箱**：rsj1999@njtech.edu.cn
- **许可证**：MIT

## 安装

```bash
pip install mlhuainanzi

```或者

```bash
pip install .

或从源码安装：

```bash
git clone https://github.com/rsj99-dev/mlhuainanzi.git
cd mlhuainanzi
pip install .
```

## 快速开始

```bash
# 预测温度并保存到文件
mlhuainanzi -i genome.faa -o result.txt

# 输出到终端
mlhuainanzi -i genome.faa

# 查看版本
mlhuainanzi --version
```

## 输入文件

输入的 .faa 文件为 FASTA 格式的蛋白质组文件，包含一个基因组的所有蛋白质序列。
示例（前几行）：

```fasta
>WP_001234567.1 hypothetical protein
MKYLLPTAAAGLLLLAAQPAMA...
>WP_001234568.1 DNA polymerase
MIVDIDYITEKGKPVRVFKK...
```

## 输出格式

输出文件包含三种预测生长温度（单位：°C）：

```
# MLHuaiNanzi Growth Temperature Prediction
# Version: 1.0.0
# Genome: Pyrococcus_furiosus
# Valid residues: 659,304
#
# Target     Temperature (°C)
# ---------- ----------------
T_min                   68.8
T_opt                  102.0
T_max                  109.9
```

## 模型性能

4 个 PLS 成分，5 折 × 10 次重复交叉验证，基于 160 个古菌和细菌基因组训练（均值 ± 标准差）：

| 目标   | 训练集 R² | CV R²           | CV RMSE (°C)    | CV MAE (°C)     |
|--------|-----------|-----------------|-----------------|-----------------|
| T_min  | 0.875     | 0.795 ± 0.082  | 9.06 ± 1.57    | 6.88 ± 0.92    |
| T_opt  | 0.934     | 0.901 ± 0.044  | 6.73 ± 0.88    | 5.11 ± 0.71    |
| T_max  | 0.927     | 0.891 ± 0.045  | 7.09 ± 0.91    | 5.43 ± 0.80    |

## 工作原理

1. **特征提取**：从蛋白质序列中提取 420 维特征向量（20 种氨基酸频率 + 400 种二肽频率）
2. **PLS 回归**（4 个成分）：有监督降维 + 线性回归，一步完成
3. **独立模型**：T_min、T_opt、T_max 各使用一个独立的 PLS 模型

## 许可证

MIT License。详见 [LICENSE](LICENSE)。

## 引用

如果您在研究中使用了 MLHuaiNanzi，请引用：

> https://github.com/rsj99-dev/mlhuainanzi
