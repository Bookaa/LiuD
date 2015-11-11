# LiuTaoTao github.com/Bookaa/LiuD

SynName = 'Python'

ignores = {
    'crlf'   : ( ' \t\n', [ r'\#.*', r'/\*(.|\n)*?\*/' ] ),
    'wspace' : ( ' \t', [ r'\#.*', r'/\*(.|\n)*?\*/' ] ),
}


base_def = { 'NEWLINE' :    ('',    '\\n+'),
             'EMPTYLINE' :  ('',    '[ \\t]*\\n+'),
             'NAME' :       ('Name',  '[A-Za-z_][A-Za-z0-9_]*'),
             'STRING' :     ('String',  '".*?"' + '|' + "'.*?'"),
             'NUMBER_INT' : ('Int',     r'0|[1-9]\d*'),
             'NUMBER_DOUBLE' :  ('Double',  r'\d+\.\d+')
             }

s_tree = '''
.syntax wspace

iExpr {
value04(v1,s,v2): item0 ^- (('*'|'/') ('+'|'-') ('>'|'<'|'!='|'=='))
value05 : +value04 'if' value04 'else' value04
value : value05
item0 :: funccall
    | adotb
    | ( LitDouble : NUMBER_DOUBLE )
    | ( LitInt : NUMBER_INT )
    | ( LitString: STRING )
    | ( Array(vlst*) : '[' value ^* ',' ']' )
    | ( Tuple(vlst*): '(' value ^* ',' ')' )
    | ( Dict(vlst*): '{' Key ^* ',' '}' )

    funccall(v, vlst*) : adotb '(' value ^* ',' ')'
    Key(v1,v2) : value ':' value

adotb :: ( trailer_adotb(v,s) : adotb '.' NAME )
    | ( trailer_subscript(v,v2) : adotb '[' value ']' )
    | VarRef

VarRef : NAME
}
iStmt {
stmts :: stmtone ^+ =ident
    stmtone :: ( stmt_print(vlst*) : 'print' value ^* ',' )
        | ( IfStmt(v1,v2,vq?) : 'if' value ':' bodyif [=ident 'else' ':' bodyif] )
        | ( ForStmt(v1,v2,v3) : 'for' VarRef 'in' value ':' bodyif )
        | ( WhileStmt(v1,v2,vq?) : 'while' value ':' bodyif [=ident 'else' ':' bodyif] )
        | ( FuncDef(sname, slst*, vbody) : 'def' NAME '(' NAME ^* ',' ')' ':' bodyns )
        | ( Return(vq?) : 'return' value? )
        | ( ClassDef(sname,vbaseq?,vbody) : 'class' NAME classbase? ':' bodyns )
        | ( stmt_continuebreak : ('continue' | 'break')$ )
        | ( stmt_global(slst*) : 'global' NAME ^+ ',' )
        | ( stmt_call : funccall )
        | ( AugAssign(v1,s,v2) : adotb ('+=' | '-=' | '*=' | '/=' | '%=' | '&=' | '|=' | '^=' | '<<=' | '>>=' | '**=' | '//=')$ value )
        | stmt_assign
        | import_stmt

        stmt_assign :: ( Assign(v1,v2) : adotb '=' value )
            | ( AssignIdx(v1,v2,v3) : adotb '[' value ']' '=' value )
        import_stmt :: import_name | import_from
            import_name(vlst*) : 'import' dotted_as_name ^+ ','
            import_from(v1,v2) : 'from' ( dotname1 | dotted_name ) 'import' (importstar | import_as_names)
}
iExpr {
        bodyif(vlst*) : +ident stmtone ^+ =ident -ident
        bodyns(vlst*) : +ident stmtone ^+ =ident -ident
        classbase(vlst*) : '(' adotb ^+ ',' ')'


    // import_name
            dotted_as_name(v,sq?) : dotted_name ['as' NAME]
    // import_from
        importstar : '*'
        dotname1(vq?) : '.' dotted_name?
        import_as_names(vlst*): import_as_name ^+ ','
            import_as_name(s,sq?): NAME ['as' NAME]
    dotted_name(slst*): NAME ^+ '.'
}

.syntax crlf
Module(vlst*) : stmts ENDMARKER$
'''

Out_self = '''
import_name : 'import' x ^* ','
dotted_as_name : x ['as' x]
import_from : 'from' x 'import' x
importstar : '*'
dotname1 : '.' x?
import_as_names : x ^* ','
import_as_name : x ['as' x]
dotted_name : x ^* '.'
trailer_subscript : x '[' x ']'

Module : (x NL)*
stmt_print : 'print' x - ^* ','
IfStmt : 'if' x ':' x ['else :' x]
ForStmt : 'for' x 'in' x ':' x
WhileStmt : 'while' x ':' x ['else :' x]
FuncDef : 'def' x '(' x ^* ',' ')' ':' x
Return : 'return' x?
ClassDef : 'class' x x? ':' x
stmt_continuebreak : x
stmt_global : 'global' x ^* ','
stmt_call : x
AugAssign : x x x
Assign : x '=' x
AssignIdx : x '[' x ']' '=' x
bodyif : +ident (x NL)* -ident
bodyns : +ident (x NL)* -ident
classbase : '(' x ^* ',' ')'
VarRef : x
value04 : x x x
value05 : x 'if' x 'else' x
value : x
funccall : x '(' x ^* ',' ')'
trailer_adotb : x - '.' - x
LitDouble : x
LitInt : x
LitString : '"' - x '"'
Array : '[' x ^* ',' ']'
Tuple : '(' x ^* ',' ')'
Dict : '{' x ^* ',' '}'
Key : x ':' x
'''

s_sample = '''
X = 5
z = [3,5,"good"]
z[0] = "aha"
x1 = { 2 : "ga", "la" : 5 }
X = 2 + 3
S = "hello world"
if X > 4:
    X = 2 + X
print X, z
'''

s_sample2 = '''
def f1(n):
    if n > 3:
        k = n + 5
    else:
        k = n - 1
    return k

print f1(5), f1(3)
'''

s_sample = '''
def f1():
    print 'this is f1'
    return 3

print 'step 1'
class cls:
    v1 = f1()

print 'step 2'
v2 = cls.v1

print 'v2 is', v2
'''

s_sample = '''
a = [2,3]
b = a
s = 'good'
a.append(5)
def fn(lst):
	lst.append(7)

fn(a)
print 'should be [2, 3, 5, 7] [2, 3, 5, 7]'
print a,b,s

b = 2+3 if 5 > 1 else 5+2
'''

s_sample2 = '''
q = 7
def f1(n):
    # k = 66
    global q, q1
    q = 2
    q1 = 55
    if n > 3:
        k = n + 5 + q
    else:
        k = n - 1
    return k

print f1(5), f1(3), q, q1

lst3 = [3,5,7]
item1 = lst3[2]
print item1

'''

s_sample2 = '''
a1 = {"hello","world"}
b1 = a1
a1.add("OK")
print 'should be:'
print "set(['world', 'OK', 'hello']) set(['world', 'OK', 'hello'])"
print a1,b1
'''