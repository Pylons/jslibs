
import sys
import os
import subprocess
import jslibs

def _concat_path(fname, *rnames):
    return os.path.join(os.path.dirname(fname), *rnames)

def module_path(mod, *rnames):
    return _concat_path(mod.__file__, *rnames)


def update_submodule(dir):
    # update submodules in this tree.
    current_dir = os.getcwd()
    os.chdir(dir)
    try:
        subprocess.call(('git', 'submodule', 'init'))
        subprocess.call(('git', 'submodule', 'update'))
    finally:
        os.chdir(current_dir)


def prep_jquery(dir):
    # from jQuery Makefile:
    #@@sed '/EXPOSE/r src/sizzle-jquery.js' ${SIZZLE_DIR}/sizzle.js | grep -v window.Sizzle > ${SRC_DIR}/selector.js
    outf = file(os.path.join(dir, 'src', 'selector.js'), 'w')
    for line in file(os.path.join(dir, 'src', 'sizzle', 'sizzle.js')):
        if 'EXPOSE' in line:
            outf.write(file(os.path.join(dir, 'src', 'sizzle-jquery.js')).read())
        elif 'window.Sizzle' not in line:
            outf.write(line)
    outf.close()


def prep_tinymce(dir):
    # run 'ant' in the source directory
    current_dir = os.getcwd()
    os.chdir(dir)
    try:
        subprocess.call(('ant', ))
    finally:
        os.chdir(current_dir)


def prepare_sources():
    # Need to update the submodules.
    # It also prepares the sources for jQuery.
    # (Other sources do not need this.)
    jslibs_gitroot = module_path(jslibs, '..')
    externals_dir = module_path(jslibs, 'externals')

    update_submodule(jslibs_gitroot)

    # jQuery 1.6.2
    # it has its own submodules that requires an update
    update_submodule(os.path.join(externals_dir, 'jquery', '1.6.2'))
    # it also requires some special preparation
    prep_jquery(os.path.join(externals_dir, 'jquery', '1.6.2'))

    # TinyMCE 3.4.7
    # needs its main js precompiled
    prep_tinymce(os.path.join(externals_dir, 'tinymce', '3.4.7'))


def main(argv=sys.argv):
    if len(argv) > 1:
        raise RuntimeError, 'jslibs_prepare_sources accepts no parameters.'

    prepare_sources()

    print "\n\n##### All sources prepared OK"

if __name__ == '__main__':
    main()
