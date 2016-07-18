# LiuTaoTao github.com/Bookaa/LiuD

s_tree = r'''
.name_prefix Out
.set_linecomment '\/\/'

.syntax wspace

stmt :: stmtone NEWLINE$
    stmtone(s, vlst*) : NAME ':' item*

    item :: ( Jiad(v1,vq?,v2) : X lnk? '^*' (String | X) )
        | ( String : STRING )
        | ( optgroup(vlst*) : '[' item+ ']' )
        | ( itemd(vlst*) : '(' item+ ')*' )
        | ( ident : ('+ident' | '-ident')$ )
        | ( newline : 'NL' )
        | ( lnk : '-' )
        | ( Xlst : 'x*' )
        | ( Xchoice : 'x?(' STRING ',' STRING ')' )
        | ( Xif : 'x?(' STRING ')' )
        | ( Xq : 'x?' )
        | ( X : 'x' )


.syntax crlf
Module(vlst*) : stmt* ENDMARKER$
'''

Out_self = '''
Module : (x NL)*
stmtone : x ':' x*
Jiad : x x? '^*' x
String : x
optgroup : '[' x* ']'
itemd : '(' x* ')*'
ident : x
newline : 'NL'
lnk : '-'
Xlst : 'x*'
Xchoice : 'x?(' x ',' x ')'
Xif : 'x?(' x ')'
Xq : 'x?'
X : 'x'
'''

s_sample = Out_self