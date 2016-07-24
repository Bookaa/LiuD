#!/usr/bin/env python

# LiuTaoTao github.com/Bookaa/LiuD


def GenSource(a1, a2):
    fi = open(a1)
    if not fi:
        return 0
    SyntaxIn = fi.read()
    fi.close()

    if a2 == 'py':
        from GenPythonSrc import GenPythonSrc
        GenPythonSrc(SyntaxIn)
    elif a2 == 'swift':
        from GenSwiftSrc import GenSwiftSrc
        GenSwiftSrc(SyntaxIn)
    else:
        return 0
    return 1

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print 'usage:'
        print '    MainGen LiuD py'
        print '    MainGen Python py'
    else:
        GenSource(sys.argv[1], sys.argv[2])

