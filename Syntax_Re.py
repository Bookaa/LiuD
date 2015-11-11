# LiuTaoTao github.com/Bookaa/LiuD

SynName = 'Re'

ignores = {
    'no' : ( '', [] )
}


base_def = { 'NAME'   : ('Name',     '[A-Za-z_][A-Za-z0-9_]*'),
             'NUMBER' : ('Int',         r'\d+'),
             'CHAR'   : ('String',      r'.')
             }

s_tree = '''
.syntax no

Module: stmt ENDMARKER$

stmt(vlst*) : items ^+ '|'

items(vlst*) : item+

item :: ( NodeProceed : '(?<!' items ')' )
    | ( IfProceed : '(?<=' items ')' )
    | ( IfNext : '(?=' stmt ')' )
    | ( IfNotNext : '(?!' stmt ')' )
    | ( YesOrNo(v, v1q?, v2q?) : '(?(' (LitName | LitNumber) ')' items? ['|' items] ')' )
    | ( RefName : '(?P=' NAME ')' )
    | ( SetFlags(slst*) : '(?' Char1+ ')' )
    | ( ZeroOrMoreNoGreedy : primeitem '*?' )
    | ( ZeroOrMore : primeitem '*' )
    | ( OneOrMore : primeitem '+' )
    | ( ZeroOrOne : primeitem '?' )
    | ( NumCtlNoGreedy(v1,v2) : primeitem '{' NumControl '}?' )
    | ( WithNumCtl(v1,v2) : primeitem '{' NumControl '}' )
    | primeitem
    | ( LineLead : '^' )
    | ( LineTail : '$' )

    LitName : NAME
    LitNumber : NUMBER

    Char1 :: -ifnotnext(')') CHAR
    Char2 :: -ifnotnext(')'|'*'|'+'|'?'|'|') CHAR
    Char3 :: -ifnotnext(']'|'-') CHAR

    primeitem :: sets
        | Escape
        | groups
        | ( Dot : '.' )
        | ( OneChar : Char2 )
        //| ( CharAsIs : ('-' | '+' | '!' | ':' | '{' | '}' | '>')$ )

        Escape : '\\' CHAR
        groups :: ( NonGroup : '(?:' stmt ')' )
            | ( NamedGroup(s, vq?) : '(?P<' NAME '>' stmt? ')' )
            | ( Group : '(' stmt ')' )

        sets :: ( SetCompl(vlst*) : '[^' groupitem+ ']' )
            | ( Set(vlst*) : '[' groupitem+ ']' )

            groupitem :: ( AtoB(s1,s2) : Char3 '-' Char3 )
                | Escape
                | ( CharItem : Char3 )
                // | ( CharAsIs2 : ('.' | '?' | '*' | '-' | '+' | '!' | ':' | ')' | '(' )$ )

    NumControl :: ( Num11(s1,s2) : NUMBER ',' NUMBER )
        | ( Num10 : NUMBER ',' )
        | ( Num01 : ',' NUMBER )
        | LitNumber


'''

Out_self = '''
Module: x
stmt : x ^* '|'
items : x*
NodeProceed : '(?<!' x ')'
IfProceed : '(?<=' x ')'
IfNext : '(?=' x ')'
IfNotNext : '(?!' x ')'
YesOrNo : '(?(' x ')' x ['|' x] ')'
RefName : '(?P=' x ')'
SetFlags : '(?' x* ')'
ZeroOrMoreNoGreedy : x '*?'
ZeroOrMore : x '*'
OneOrMore : x '+'
ZeroOrOne : x '?'
NumCtlNoGreedy : x '{' x '}?'
WithNumCtl : x '{' x '}'
LineLead : '^'
LineTail : '$'
Dot : '.'
OneChar : x
Escape : '\\' x
NonGroup : '(?:' x ')'
NamedGroup : '(?P<' x '>' x? ')'
Group : '(' x ')'
SetCompl : '[^' x* ']'
Set : '[' x* ']'
AtoB : x '-' x
CharItem : x
Num11 : x ',' x
Num10 : x ','
Num01 : ',' x
LitName : x
LitNumber : x
'''

s_sample = '[A-Za-z_][A-Za-z0-9_]*'


