#!/usr/bin/env python

import os
import glob
import shutil
import argparse
import string

misc_files = ['lazysizes.min.js', 'jquery-3.3.1.min.js', 'okzoom.min.js', 'dummy.gif']


def gen_html(s):
    return '<!DOCTYPE html>\n<html lang="en">\n{}\n</html>\n'.format(s)


def gen_head(opts):
    ret = string.Template('''
        <head>
        <meta charset="UTF-8">
        <script src="./_miscs/lazysizes.min.js"></script>
        <script src="./_miscs/jquery-3.3.1.min.js"></script>
        <script src="./_miscs/okzoom.min.js"></script>
        <script>
            $(function(){
                $('img').okzoom({
                    width: $size,
                    height: $size,
                    scaleWidth: $scale_width,
                    round: true,
                    border: "1px solid black",
                    shadow: "0 0 5px #ffffff"
                });
            });
        </script>
        </head>
        ''').safe_substitute(size=opts.width//2, scale_width=opts.width * 4)

    return ret


def gen_body(s):
    return '<body>\n{}\n</body>\n'.format(s)


def gen_img(fname, width):
    if width:
        return '<img src="./_miscs/dummy.gif" data-src={0} class="lazyload" width="{1}" />\n'.format(fname, width)
    else:
        return '<img src="./_miscs/dummy.gif" data-src={0} class="lazyload" />\n'.format(fname)


def gen_table(s):
    return '<table>{}</table>\n'.format(s)


def gen_tr(s):
    return '<tr>{}</tr>\n'.format(s)


def gen_td(s):
    return '<td>{}</td>\n'.format(s)


def gen_html_format(opts):
    ret = ''

    formated_fpaths = []
    for fn_format in opts.format:
        formated_fpaths.append(sorted(list(glob.glob(os.path.join(opts.dir, fn_format)))))

    for fpaths in zip(*formated_fpaths):
        imgs = ''
        names = ''
        for fpath in fpaths:
            fname = os.path.relpath(fpath, start=opts.dir)
            imgs += gen_td(gen_img(fname, opts.width))
            names += gen_td(fname)
        ret += gen_table(gen_tr(imgs) + gen_tr(names))

    ret = gen_body(ret)
    head = gen_head(opts)
    ret = gen_html(head + ret)

    return ret


def gen_html_naive(opts):
    ret = ''

    fnames = sorted(os.listdir(opts.dir))
    for fname in fnames:
        img = gen_tr(gen_td(gen_img(fname, opts.width)))
        name = gen_tr(gen_td(fname))
        ret += gen_table(img + name)

    ret = gen_body(ret)
    head = gen_head(opts)
    ret = gen_html(head + ret)

    return ret


def copy_miscs(opts):
    miscs = os.path.join(opts.dir, '_miscs')
    if not os.path.exists(miscs):
        os.makedirs(miscs)

    dname = os.path.dirname(__file__)
    for file in misc_files:
        shutil.copyfile(os.path.join(dname, file), os.path.join(miscs, file))


class Dict2attr(object):
    def __init__(self, opts):
        self.opts = opts

    def __getattr__(self, key):
        if key in self.opts:
            return self.opts[key]
        else:
            raise AttributeError(key)

    def __getitem__(self, key):
        return self.opts[key]


def displayer(opts):
    if isinstance(opts, argparse.Namespace):
        pass
    elif isinstance(opts, dict):
        opts = Dict2attr(opts)
    else:
        raise NotImplementedError

    if opts.format:
        script = gen_html_format(opts)
    else:
        script = gen_html_naive(opts)

    with open(os.path.join(opts.dir, '_displayer.html'), 'w') as f:
        f.write(script)

    copy_miscs(opts)


def displayer_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', '-d', type=str, required=True, help='Target directory')
    parser.add_argument('--format', '-f', type=str, nargs='*', help='Filename format')
    parser.add_argument('--width', '-w', type=int, default=128, help='Image width')
    opts = parser.parse_args()

    displayer(opts)
