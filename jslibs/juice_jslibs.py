
import sys
import os
import subprocess
import jslibs

def _concat_path(fname, *rnames):
    return os.path.join(os.path.dirname(fname), *rnames)

def module_path(mod, *rnames):
    return _concat_path(mod.__file__, *rnames)

def run_juicer(resource, output="min/"):
    attrs = ('juicer', 'merge', '-i', '--force', 
        '-o', os.path.join(os.path.dirname(resource), output), resource)
    print '##### Will run: ' + ' '.join(attrs) 
    status = subprocess.call(attrs)
    if status != 0:
        print "\n\n##### ERROR: FAILED compression of " + resource
        print '\nTry to consolidate problems by running manually:\n\n' + ' '.join(attrs) + '\n'
        raise SystemExit, "Compression of " + resource + " failed"

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

def main(argv=sys.argv):
    if len(argv) > 1:
        raise RuntimeError, 'juice_jslibs accepts no parameters.'

    jslibs_gitroot = module_path(jslibs, '..')
    externals_dir = module_path(jslibs, 'externals')
    resources_dir = module_path(jslibs, 'resources')

    update_submodule(jslibs_gitroot)

    update_submodule(os.path.join(externals_dir, 'jquery', '1.6.2'))
    prep_jquery(os.path.join(externals_dir, 'jquery', '1.6.2'))
    run_juicer(os.path.join(externals_dir, 'jquery', 'jquery-1.6.2.js'), output=resources_dir) 

    print "\n\n##### All files compressed OK"

if __name__ == '__main__':
    main()
