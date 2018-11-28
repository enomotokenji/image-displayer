#!/usr/bin/env python

import os
import sys
import glob
import shutil


def gen_html(s, newline=False):
    tag_begin = '<!DOCTYPE html>\n<html lang="en">'
    tag_end = '</html>'
    if newline:
        tag_begin += '\n'
        tag_end = '\n' + tag_end + '\n'

    return tag_begin + s + tag_end


def gen_head(newline=False):
    tag_begin = '<head>'
    tag_end = '</head>'
    if newline:
        tag_begin += '\n'
        tag_end = '\n' + tag_end + '\n'

    contents = '<meta charset="UTF-8">\n<script src="./_miscs/lazysizes.min.js" async=""></script>'

    return tag_begin + contents + tag_end


def gen_body(s, newline=False):
    tag_begin = '<body>'
    tag_end = '</body>'
    if newline:
        tag_begin += '\n'
        tag_end = '\n' + tag_end + '\n'

    return tag_begin + s + tag_end


def gen_img(fname, newline=False):
    ret = '<img src="./_miscs/dummy.gif" data-src={} class="lazyload" />'.format(fname)

    return ret


def gen_table(s, newline=False):
    tag_begin = '<table>'
    tag_end = '</table>'
    if newline:
        tag_begin += '\n'
        tag_end = '\n' + tag_end + '\n'

    return tag_begin + s + tag_end


def gen_tr(s, newline=False):
    tag_begin = '<tr>'
    tag_end = '</tr>'
    if newline:
        tag_begin += '\n'
        tag_end = '\n' + tag_end + '\n'

    return tag_begin + s + tag_end


def gen_td(s, newline=False):
    tag_begin = '<td>'
    tag_end = '</td>'
    if newline:
        tag_begin += '\n'
        tag_end = '\n' + tag_end + '\n'

    return tag_begin + s + tag_end


def gen_html_format(dname, fn_formats):
    ret = ''

    formated_fpaths = []
    for fn_format in fn_formats:
        formated_fpaths.append(sorted(list(glob.glob(os.path.join(dname, fn_format)))))

    for fpaths in zip(*formated_fpaths):
        imgs = ''
        names = ''
        for fpath in fpaths:
            fname = os.path.basename(fpath)
            imgs += gen_td(gen_img(fname))
            names += gen_td(fname)
        ret += gen_table(gen_tr(imgs) + gen_tr(names))

    ret = gen_body(ret)
    head = gen_head()
    ret = gen_html(head + ret)

    return ret


def gen_html_naive(dname):
    ret = ''

    fnames = sorted(os.listdir(dname))
    for fname in fnames:
        img = gen_tr(gen_td(gen_img(fname)))
        name = gen_tr(gen_td(fname))
        ret += gen_table(img + name)

    ret = gen_body(ret)
    head = gen_head()
    ret = gen_html(head + ret)

    return ret


def displayer():
    if len(sys.argv) < 2:
        print('Specify a directory')
    else:
        dname = sys.argv[1]

    fn_formats = sys.argv[2:] if len(sys.argv) > 2 else None

    if fn_formats:
        script = gen_html_format(dname, fn_formats)
    else:
        script = gen_html_naive(dname)

    with open(os.path.join(dname, '_displayer.html'), 'w') as f:
        f.write(script)

    miscs = os.path.join(dname, '_miscs')
    if not os.path.exists(miscs):
        os.makedirs(miscs)

    dir_ex = os.path.dirname(__file__)
    shutil.copyfile(os.path.join(dir_ex, 'lazysizes.min.js'), os.path.join(miscs, 'lazysizes.min.js'))
    shutil.copyfile(os.path.join(dir_ex, 'dummy.gif'), os.path.join(miscs, 'dummy.gif'))
