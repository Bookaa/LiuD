
# LiuTaoTao github.com/Bookaa/LiuD


def GenSource(a1, a2):
    if a1 == 'Swift':
        import Syntax_Swift as SyntaxIn
    elif a1 == 'LiuD':
        import Syntax_LiuD as SyntaxIn
    elif a1 == 'Re':
        import Syntax_Re as SyntaxIn
    elif a1 == 'Out':
        import Syntax_Out as SyntaxIn
    elif a1 == 'Python':
        import Syntax_Python as SyntaxIn
    elif a1 == 'LangL':
        import Syntax_LangL as SyntaxIn
    elif a1 == 'Z':
        import Syntax_Z as SyntaxIn
    elif a1.endswith('.py'):
        SyntaxIn = __import__(a1[:-3])
    else:
        return 0

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

