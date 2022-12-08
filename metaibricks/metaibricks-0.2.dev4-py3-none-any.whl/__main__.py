from metaibricks import CLI, Pipeline

if __name__ == "__main__":
    cli = CLI()
    cli.parser.add_argument(
        "filename",
        help="Configuration file's name. Should be a JSON file.",
    )
    args = cli.parse_args()

    pipeline = Pipeline.load(filename=args.filename)

    pipeline.run()
