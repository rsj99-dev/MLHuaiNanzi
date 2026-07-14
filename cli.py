"""
Command-line interface for MLHuaiNanzi.

Usage:
    mlhuainanzi -i protein.faa -o result.txt
    mlhuainanzi -i protein.faa
    mlhuainanzi --version
"""

import argparse
import sys
from . import __version__
from .predict import predict_temperatures


def main():
    parser = argparse.ArgumentParser(
        prog='mlhuainanzi',
        description=(
            'MLHuaiNanzi: Predict growth temperatures (T_min, T_opt, T_max) '
            'for Archaea from a proteome .faa file using PLS regression.'
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            'Examples:\n'
            '  mlhuainanzi -i genome.faa -o result.txt\n'
            '  mlhuainanzi -i genome.faa\n'
        ),
    )

    parser.add_argument(
        '-i', '--input', required=True, metavar='FILE',
        help='Input proteome file in FASTA format (.faa)',
    )
    parser.add_argument(
        '-o', '--output', default=None, metavar='FILE',
        help='Output file for prediction results (default: stdout)',
    )
    parser.add_argument(
        '-v', '--version', action='version',
        version=f'mlhuainanzi {__version__}',
    )

    args = parser.parse_args()

    try:
        results = predict_temperatures(args.input)
    except FileNotFoundError as e:
        sys.exit(f"Error: {e}")
    except ValueError as e:
        sys.exit(f"Error: {e}")
    except Exception as e:
        sys.exit(f"Error: prediction failed - {e}")

    lines = [
        f"# MLHuaiNanzi Growth Temperature Prediction",
        f"# Version: {__version__}",
        f"# Genome: {results['genome_name']}",
        f"# Valid residues: {results['valid_residues']:,}",
        f"#",
        f"# {'Target':<10} {'Temperature (°C)':>16}",
        f"# {'-'*10} {'-'*16}",
    ]
    for target in ['T_min', 'T_opt', 'T_max']:
        lines.append(f"{target:<10} {results[target]:>16.1f}")

    output_text = '\n'.join(lines) + '\n'

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output_text)
        sys.stdout.write(output_text)
        print(f"Results saved to: {args.output}", file=sys.stderr)
    else:
        sys.stdout.write(output_text)


if __name__ == '__main__':
    main()
