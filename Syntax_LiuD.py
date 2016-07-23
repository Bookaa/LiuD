# LiuTaoTao github.com/Bookaa/LiuD

s_tree = r'''
.name_prefix LiuD
.set_linecomment '\/\/'
// this is comment
.set_blockcomment '/\*' '\*/'
/* comment again */

.syntax wspace

// .string STRING1 strtype1 '\$liud\$((.|\n)*?)\$duil\$'
// .string STRING2 strtype1 '\$liut\$((.|\n)*?)\$tuil\$'
// .string STRING3 strtype3 $liud$'([^'\\]*(?:\\.[^'\\]*)*)'$duil$
// .string STRING4 strtype4 $liud$'([^'\\]*(?:\\.[^'\\]*)*)'$duil$

// STRING :: STRING1 | STRING2 | STRING3

string_def : '.string' NAME NAME STRING

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
            | ( bracechoice(vlst*) : '(' base1 ^+ '|' ')' )
            | ( BoolChoice : 'Bool(' STRING ',' STRING ')' )
            | ( BoolIf : 'Bool(' STRING ')' )
            | LitName
            | LitString
            | ( ident : ('+ident' | '=ident' | '-ident')$ )
        base1 :: ( basestrn : (strings | LitName) - '$' )
            | base0
        baseitem :: ( ifnext(slst*) : '-ifnext(' STRING ^+ '|' ')' )
            | ( ifnotnext(slst*) : '-ifnotnext(' STRING ^+ '|' ')' )
            | skipdef
            | ( itemq : base1 - '?' )
            | ( itemd : base1 - '*' )
            | ( itemp : base0 - '+' )
            | ( jiad(v1,v2q?,v3q?,v4) : base0 skipdef? '^*' skipdef? base1 )
            | ( jiap(v1,v2q?,v3q?,v4) : base0 skipdef? '^+' skipdef? base1 )
            | ( optgroup(vlst*) : '[' base0+ ']' )
            | base1
            skipdef :: ( syntaxdef : '-(' - NAME - ')' )
                | ( noskip : '-' )
        LitName : NAME
        LitString : STRING
}
stmt :: stmtone NEWLINE$
    stmtone :: ( dot_syntax : '.syntax' (NAME | '-'$) )
        | ( set_linecomment : '.set_linecomment' STRING )
        | ( set_blockcomment : '.set_blockcomment' STRING STRING )
        | ( name_prefix : '.name_prefix' NAME )
        | output_rules
        | string_def
        | ( sample_text : 'Sample' 'Text' '=' STRING )
        | stmt_inline
        | stmt_tax
        | protoGroup

stmt_inline(s, vargq?, v) : NAME ['(' arg ')'] '::' taxvalue
stmt_tax(s, vq?, v) : NAME ['(' args ')'] ':' taxvalue
    args(vlst*) : arg ^+ ','
        arg(s, sq?) : NAME - ('?' | '*')$?

output_rules : 'Output' 'Rules' '{' NEWLINE$? orule* '}'

    orule(s, vlst*) : NAME ':' oitem* NEWLINE$

    oitem :: ( oJiad(v1,vq?,v2) : oX olnk? '^*' (oString | oX) )
        | ( oString : STRING4 )
        | ( ooptgroup(vlst*) : '[' oitem+ ']' )
        | ( oitemd(vlst*) : '(' oitem+ ')*' )
        | ( oident : ('+ident' | '-ident')$ )
        | ( onewline : 'NL' )
        | ( olnk : '-' )
        | ( oXlst : 'x*' )
        | ( oXchoice : 'x?(' STRING ',' STRING ')' )
        | ( oXif : 'x?(' STRING ')' )
        | ( oXq : 'x?' )
        | ( oX : 'x' )

.syntax crlf
protoGroup : NAME '{' stmt* '}'
Module(vlst*) : stmt* ENDMARKER$

Output Rules {
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
    noskip : '-'
    dot_syntax : '.syntax' x
    set_linecomment : '.set_linecomment' x
    set_blockcomment : '.set_blockcomment' x x
    name_prefix : '.name_prefix' x
    string_def : '.string' x x x
    sample_text : 'Sample Text =' x
    stmt_inline : x ['(' x ')'] '::' x
    stmt_tax : x ['(' x ')'] ':' x
    args : x ^* ','
    arg : x [- x]
    Module : (x NL)*
    output_rules : 'OutPut' 'Rules' '{' NL x* '}'
    orule : x ':' x* NL
    oJiad : x x? '^*' x
    oString : x
    ooptgroup : '[' x* ']'
    oitemd : '(' x* ')*'
    oident : x
    onewline : 'NL'
    olnk : '-'
    oXlst : 'x*'
    oXchoice : 'x?(' x ',' x ')'
    oXif : 'x?(' x ')'
    oXq : 'x?'
    oX : 'x'
}


'''

s_tree = s_tree + '''

Sample Text = $liut$
%s
$tuil$

''' % s_tree

# s_sample = s_tree # describe myself
