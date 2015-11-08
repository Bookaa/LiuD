# LiuTaoTao github.com/Bookaa/LiuD

SynName = 'LiuD'

ignores = {
    'crlf'   : ( ' \t\n', [ '//.*', r'/\*(.|\n)*?\*/' ] ),
    'wspace' : ( ' \t', [ r'/\*(.|\n)*?\*/' ] ),
    'no'     : ( '', [] )
}

base_def = { 'NEWLINE' :    ('',   '\\n+'),
             'NAME'    :    ('Name',  '[A-Za-z_][A-Za-z0-9_]*'),
             'STRING'  :    ('String',  "'.*?'")
             }

s_tree = '''
.syntax wspace

iExpr {
taxvalue :: ( opt2(s,vlst*) : NAME '^-' '(' strings+ ')' )
    | ( choices(vlst*) : + taxone -(crlf) ^+ '|' )
    | ( MoreDef : '+' baseitem* )
    | ( OtherSyntax : '$NewSyntax' )
    strings :: ( stringchoice(slst*) : '(' STRING ^+ '|' ')' )
        | LitString
    taxone :: ( inline : '(' stmt_tax ')' )
        | ( serie(vlst*) : + baseitem+ )
        base0 :: ( bracegroup(vlst*) : '(' base0+ ')' )
            | ( bracechoice(vlst*) : '(' base0 ^+ '|' ')' )
            | ( BoolChoice : 'Bool(' STRING ',' STRING ')' )
            | ( BoolIf : 'Bool(' STRING ')' )
            | LitName
            | LitString
            | ( ident : ('+ident' | '=ident' | '-ident')$ )
        base1 :: ( basestrn : (strings | LitName) -(no) '$' )
            | base0
        baseitem :: syntaxdef
            | ( ifnext(slst*) : '-ifnext(' STRING ^+ '|' ')' )
            | ( ifnotnext(slst*) : '-ifnotnext(' STRING ^+ '|' ')' )
            | ( itemq : base1 -(no) '?' )
            | ( itemd : base1 -(no) '*' )
            | ( itemp : base0 -(no) '+' )
            | ( jiad(v1,v2q?,v3q?,v4) : base0 syntaxdef? '^*' syntaxdef? base1 )
            | ( jiap(v1,v2q?,v3q?,v4) : base0 syntaxdef? '^+' syntaxdef? base1 )
            | ( optgroup(vlst*) : '[' base0+ ']' )
            | base1
            syntaxdef : '-(' -(no) NAME -(no) ')'
        LitName : NAME
        LitString : STRING
}
stmt :: stmtone NEWLINE$
    stmtone :: ( dot_syntax : '.syntax' NAME )
        | stmt_inline
        | stmt_tax
        | protoGroup

stmt_inline(s, vargq?, v) : NAME ['(' arg ')'] '::' taxvalue
stmt_tax(s, vq?, v) : NAME ['(' args ')'] ':' taxvalue
    args(vlst*) : arg ^+ ',' -(no)
        arg(s, sq?) : NAME -(no) ('?' | '*')$?

.syntax crlf
protoGroup : NAME '{' stmt* '}'
Module(vlst*) : stmt* ENDMARKER$

'''

Out_self = '''
MoreDef : '+' - x*
OtherSyntax : '$NewSyntax'
protoGroup : x '{' NL (x NL)* '}'
opt2 : x '^-' '(' x* ')'
choices : x ^* '\n    |'
stringchoice : '(' x ^* '|' ')'
inline : '(' x ')'
serie : x*
bracegroup : '(' x* ')'
bracechoice : '(' x ^* '|' ')'
BoolChoice : 'Bool(' x ',' x ')'
BoolIf : 'Bool(' x ')'
ident : x
basestrn : x - '$'
LitName : x
LitString : x
ifnext : '-ifnext(' x ^* '|' ')'
ifnotnext : '-ifnotnext(' x ^* '|' ')'
itemq : x - '?'
itemd : x - '*'
itemp : x - '+'
jiad : x x? '^*' x? x
jiap : x x? '^+' x? x
optgroup : '[' x* ']'
syntaxdef : '-(' - x - ')'
dot_syntax : '.syntax' x
stmt_inline : x ['(' x ')'] '::' x
stmt_tax : x ['(' x ')'] ':' x
args : x ^* ','
arg : x [- x]
Module : (x NL)*
'''

s_sample = s_tree # describe myself

# if 'stmt : aa ^+ b' or 'stmt : aa*' , when aa occurs only once, then return a instead of [a]
# -(no) will change to - next version
# add -ifnext(NAME) support