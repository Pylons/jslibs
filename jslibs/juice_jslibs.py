
import sys
import os
import subprocess
import jslibs
from jslibs.jslibs_prepare_sources import prepare_sources

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


def juice_jslibs():

    externals_dir = module_path(jslibs, 'externals')
    resources_dir = module_path(jslibs, 'resources')

    # jQuery 1.6.2
    run_juicer(os.path.join(externals_dir, 'jquery', 'jquery-1.6.2.js'), output=resources_dir) 

    # jquery-ui 1.9m5
    run_juicer(os.path.join(externals_dir, 'jquery-ui', 'jquery-ui-1.9m5.js'), output=resources_dir) 
    run_juicer(os.path.join(externals_dir, 'jquery-ui', 'jquery-ui-1.9m5-unthemed.css'), output=resources_dir) 
    run_juicer(os.path.join(externals_dir, 'jquery-ui', 'jquery-ui-1.9m5-smoothness-themeonly.css'), output=resources_dir) 
    run_juicer(os.path.join(externals_dir, 'jquery-ui', 'jquery-ui-1.9m5-smoothness.css'), output=resources_dir) 

    # jQuery 1.6.2 + jquery-ui 1.9m5 combo
    run_juicer(os.path.join(externals_dir, 'jquery-ui', 'jquery-1.6.2-jquery-ui-1.9m5.js'), output=resources_dir) 

    # SlickGrid v2.0a jslibrev1
    run_juicer(os.path.join(externals_dir, 'slickgrid', 'slickgrid-v2.0a-jslibrev1.js'), output=resources_dir) 
    run_juicer(os.path.join(externals_dir, 'slickgrid', 'slickgrid-v2.0a-jslibrev1.css'), output=resources_dir) 

    # TinyMCE 3.4.7, static version with selected plugins only
    run_juicer(os.path.join(externals_dir, 'tinymce', 'tinymce-3.4.7-jquery-static-plugins1.js'), output=resources_dir) 
    ##run_juicer(os.path.join(externals_dir, 'tinymce', 'tinymce-3.4.7-jquery-static-defaultskin.css'), output=resources_dir) 

    # TinyMCE 3.4.8, static version with selected plugins only
    run_juicer(os.path.join(externals_dir, 'tinymce', 'tinymce-3.4.8-jquery-static-plugins1.js'), output=resources_dir) 
    run_juicer(os.path.join(externals_dir, 'tinymce', 'tinymce-3.4.8-jquery-static-plugins2.js'), output=resources_dir) 
    run_juicer(os.path.join(externals_dir, 'tinymce', 'tinymce-3.4.8-popup-utils.js'), output=resources_dir) 
    ##run_juicer(os.path.join(externals_dir, 'tinymce', 'tinymce-3.4.8-jquery-static-defaultskin.css'), output=resources_dir) 

    # Bottlecap extra resources rev 0, contains jQuery 1.6.2 and ui.widget.js from jquery-ui 1.9m5
    run_juicer(os.path.join(externals_dir, 'bottlecap-extras', 'bottlecap-head-0-jquery-1.6.2.js'), output=resources_dir) 
    run_juicer(os.path.join(externals_dir, 'bottlecap-extras', 'bottlecap-tail-0.js'), output=resources_dir) 


def main(argv=sys.argv):
    if len(argv) > 1:
        raise RuntimeError, 'juice_jslibs accepts no parameters.'

    prepare_sources()

    juice_jslibs()

    print "\n\n##### All files compressed OK"

if __name__ == '__main__':
    main()
