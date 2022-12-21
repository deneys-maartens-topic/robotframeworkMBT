import os
import sys
import unittest
import robot

# Usage: python run_tests.py [utest] [atest]
#
#        When started without arguments, runs all unit and acceptance tests
#        In place of 'atest' any set of Robot Framework command line options can be used
#        Unit tests can also be executed by running their individually files as script

if __name__ == '__main__':
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    utest = False
    atest = True
    if len(sys.argv) == 1:
        print("No test folder provided. Running all unit and acceptance tests from", THIS_DIR)
        sys.argv.append(os.path.join(THIS_DIR, 'atest'))
        utest = True

    if 'utest' in sys.argv:
        sys.argv.remove('utest')
        utest = True
        atest = False if len(sys.argv) == 1 else True

    if utest:
        urun = unittest.main(module=None, argv=[__file__, 'discover', os.path.join(THIS_DIR, 'utest')], exit=False)
        if not urun.result.wasSuccessful():
            sys.exit(1)

    if 'atest' in sys.argv:
        sys.argv.remove('atest')
        sys.argv.append(os.path.join(THIS_DIR, 'atest'))

    if atest:
        OUTPUT_ROOT = os.path.join(THIS_DIR, 'atest', 'results')
            
        # Adding the robotframeworkMBT folder to the python path forces the development
        # version to be used instead of the one installed on your system. You will also
        # need to add this path to your IDE options when running from there.
        robot.run_cli(['--outputdir', OUTPUT_ROOT,
                       '--pythonpath', THIS_DIR]
                       + sys.argv[1:])
