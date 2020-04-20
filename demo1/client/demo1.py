import os
import argparse
import datetime
import urllib.request


def download(url, filename, outpath):
    if outpath is None:
        outpath = filename
    return urllib.request.urlretrieve(os.path.join(url, filename), outpath)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--base-url', '-u', type=str,
        default='http://percy.barsand.dev',
        help='base URL for target server application.')
    parser.add_argument(
        '--url_filepath', '-f', type=str, default='desafio.tar',
        help='base URL for target server application.')
    parser.add_argument(
        '--outpath', '-o', type=str,
        default=str(int(datetime.datetime.utcnow().timestamp())),
        help='output file path.')
    args = parser.parse_args()
    try:
        download(args.base_url, args.url_filepath, args.outpath)
        print('successfully downloaded `%s` from %s as `%s`' %
              (args.url_filepath, args.base_url, args.outpath))
    except Exception as e:
        raise(e)
