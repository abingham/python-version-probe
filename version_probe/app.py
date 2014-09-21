import baker

from version_probe import detect_version


@baker.command(
    params={
        'path': 'The file or directory to probe.',
    },
    default=True,
)
def detect(path):
    try:
        v = detect_version(path)
        print(v)
    except ValueError as e:
        print(e)


def main():
    baker.run()


if __name__ == '__main__':
    main()
