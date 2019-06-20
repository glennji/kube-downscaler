from kube_downscaler.command import get_parser


def test_parse_args():
    parser = get_parser()
    config = parser.parse_args(['--dry-run'])

    assert config.dry_run
