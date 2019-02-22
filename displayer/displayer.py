#!/usr/bin/env python

import os
import sys
import glob
import shutil
import argparse


def gen_html(s):
    tag_begin = '<!DOCTYPE html>\n<html lang="en">'
    tag_end = '</html>'

    return tag_begin + s + tag_end


def gen_head():
    tag_begin = '<head>'
    tag_end = '</head>'

    contents = '<meta charset="UTF-8">\n<script src="./_miscs/lazysizes.min.js" async=""></script>'

    return tag_begin + contents + tag_end


def gen_body(s):
    return '<body>{}</body>'.format(s)


def gen_img(fname, width):
    if width:
        return '<img src="./_miscs/dummy.gif" data-src={} class="lazyload" width="{}" />'.format(fname, width)
    else:
        return '<img src="./_miscs/dummy.gif" data-src={} class="lazyload" />'.format(fname)


def gen_table(s):
    return '<table>{}</table>'.format(s)


def gen_tr(s):
    return '<tr>{}</tr>'.format(s)


def gen_td(s):
    return '<td>{}</td>'.format(s)


def gen_html_format(opts):
    ret = ''

    formated_fpaths = []
    for fn_format in opts.format:
        formated_fpaths.append(sorted(list(glob.glob(os.path.join(opts.dir, fn_format)))))

    for fpaths in zip(*formated_fpaths):
        imgs = ''
        names = ''
        for fpath in fpaths:
            fname = os.path.basename(fpath)
            imgs += gen_td(gen_img(fname, opts.width))
            names += gen_td(fname)
        ret += gen_table(gen_tr(imgs) + gen_tr(names))

    ret = gen_body(ret)
    head = gen_head()
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
    head = gen_head()
    ret = gen_html(head + ret)

    return ret


def displayer():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', '-d', type=str, required=True, help='Target directory')
    parser.add_argument('--format', '-f', type=str, nargs='*', help='Filename format')
    parser.add_argument('--width', '-w', type=int, help='Image width')
    opts = parser.parse_args()

    if opts.format:
        script = gen_html_format(opts)
    else:
        script = gen_html_naive(opts)

    with open(os.path.join(opts.dir, '_displayer.html'), 'w') as f:
        f.write(script)

    miscs = os.path.join(opts.dir, '_miscs')
    if not os.path.exists(miscs):
        os.makedirs(miscs)

    dir_ex = os.path.dirname(__file__)
    shutil.copyfile(os.path.join(dir_ex, 'lazysizes.min.js'), os.path.join(miscs, 'lazysizes.min.js'))
    shutil.copyfile(os.path.join(dir_ex, 'dummy.gif'), os.path.join(miscs, 'dummy.gif'))
