import argparse
from cdc_ctt.graph.graph_generator import GraphGenerator


def main(number, output):
    graph_generator = GraphGenerator()
    graph_generator.generate(number)
    graph_generator.save(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--number",
        help="number of patients to generate",
        type=int,
        required=True,
        dest="number",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="output file path",
        type=str,
        required=True,
        dest="output",
    )
    args = parser.parse_args()
    main(number=args.number, output=args.output)
