# MLHuaiNanzi

**Growth temperature prediction for Archaea and Bacteria from proteome sequences.**

Predicts minimum (T_min), optimal (T_opt), and maximum (T_max) growth temperatures
from a genome's protein sequences (.faa file) using Partial Least Squares (PLS)
regression on 420-dimensional amino acid and dipeptide composition features.

- **Author**: Ren Shijie (rsj99)
- **Email**: rsj1999@njtech.edu.cn
- **License**: MIT

## Installation

```bash
pip install mlhuainanzi
```

Or install from source:

```bash
git clone https://github.com/rsj99-dev/mlhuainanzi.git
cd mlhuainanzi
pip install .
```

## Quick Start

```bash
# Predict temperatures and save to file
mlhuainanzi -i genome.faa -o result.txt

# Print to stdout
mlhuainanzi -i genome.faa

# Show version
mlhuainanzi --version
```

## Input

A FASTA-formatted proteome file (**.faa**) containing all protein sequences of a genome.
Example (first few lines):

```fasta
>WP_001234567.1 hypothetical protein
MKYLLPTAAAGLLLLAAQPAMA...
>WP_001234568.1 DNA polymerase
MIVDIDYITEKGKPVRVFKK...
```

## Output

The output file contains predicted growth temperatures in degrees Celsius:

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

## Model Performance

4-component PLS regression, 5-fold × 10-repeat cross-validation, trained on 160 genomes (mean ± SD):

| Target | Train R² | CV R²           | CV RMSE (°C)    | CV MAE (°C)     |
|--------|----------|-----------------|-----------------|-----------------|
| T_min  | 0.875    | 0.795 ± 0.082  | 9.06 ± 1.57    | 6.88 ± 0.92    |
| T_opt  | 0.934    | 0.901 ± 0.044  | 6.73 ± 0.88    | 5.11 ± 0.71    |
| T_max  | 0.927    | 0.891 ± 0.045  | 7.09 ± 0.91    | 5.43 ± 0.80    |

## How It Works

1. **Feature extraction**: 420-dimensional vector (20 amino acid frequencies + 400 dipeptide frequencies)
2. **PLS regression** (4 components): Supervised dimensionality reduction + linear regression
3. **Separate models** for T_min, T_opt, T_max, each independently fitted

## License

MIT License. See [LICENSE](LICENSE) for details.

## Citation

If you use MLHuaiNanzi in your research, please cite:

> (https://github.com/rsj99-dev/mlhuainanzi)
# MLHuaiNanzi

**Growth temperature prediction for Archaea from proteome sequences.**

Predicts minimum (T_min), optimal (T_opt), and maximum (T_max) growth temperatures
from a genome's protein sequences (.faa file) using Partial Least Squares (PLS)
regression on 420-dimensional amino acid and dipeptide composition features.

## Installation

```bash
pip install mlhuainanzi
```

Or install from source:

```bash
git clone https://github.com/rsj99-dev/mlhuainanzi.git
cd mlhuainanzi
pip install .
```

## Quick Start

```bash
# Predict temperatures and save to file
mlhuainanzi -i genome.faa -o result.txt

# Print to stdout
mlhuainanzi -i genome.faa

# Show version
mlhuainanzi --version
```

## Input

A FASTA-formatted proteome file (**.faa**) containing all protein sequences of a genome.
Example (first few lines):

```fasta
>WP_001234567.1 hypothetical protein
MKYLLPTAAAGLLLLAAQPAMA...
>WP_001234568.1 DNA polymerase
MIVDIDYITEKGKPVRVFKK...
```

## Output

The output file contains predicted growth temperatures in degrees Celsius:

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

## Model Performance

4-component PLS regression, 5-fold × 10-repeat cross-validation (mean ± SD):

| Target | Train R² | CV R²           | CV RMSE (°C)    | CV MAE (°C)     |
|--------|----------|-----------------|-----------------|-----------------|
| T_min  | 0.875    | 0.795 ± 0.082  | 9.06 ± 1.57    | 6.88 ± 0.92    |
| T_opt  | 0.934    | 0.901 ± 0.044  | 6.73 ± 0.88    | 5.11 ± 0.71    |
| T_max  | 0.927    | 0.891 ± 0.045  | 7.09 ± 0.91    | 5.43 ± 0.80    |

## How It Works

1. **Feature extraction**: 420-dimensional vector (20 amino acid frequencies + 400 dipeptide frequencies)
2. **PLS regression** (4 components): Supervised dimensionality reduction + linear regression
3. **Separate models** for T_min, T_opt, T_max trained on 160 genomes of archaea and bacteria.

## License

MIT License

## Citation

If you use MLHuaiNanzi in your research, please cite:

> [(https://github.com/rsj99-dev/mlhuainanzi)]
