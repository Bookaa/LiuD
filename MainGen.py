
# LiuTaoTao github.com/Bookaa/LiuD


#import lib
#import Re2
#lib.HowRe = Re2.HowRe_liud

def GenSource():
    import sys

    if len(sys.argv) != 3:
        return 0

    a1 = sys.argv[1]

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
    else:
        return 0

    a2 = sys.argv[2]

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
    if 0 == GenSource():
        print 'usage:'
        print '    MainGen LiuD py'
        print '    MainGen Python py'

